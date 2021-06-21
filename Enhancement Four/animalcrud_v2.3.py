#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId

__author__ = "Nellie Umanah"
__license__ = "GPL"
__version__ = "2.2"
__maintainer__ = "Nellie Umanah"
__email__ = "nellie.umanah@snhu.edu"
__status__ = "Development"

class mycrud(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, host, port, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@%s:%s' % (username, password, host, port))
        self.database = self.client['AAC']

# Create method.
    def mycreate(self, data):
        if data is not None:
                result = self.database.animals.insert(data)  # data should be dictionary
                print("Record was successfully inserted.")         
                return True
        else:
            print("Nothing to save, because data parameter is empty")
            return False
# Read Method.
    def myread(self, data):
        if data is not None:
                return self.database.animals.find(data, {"_id": False})  # data should be dictionary
                print("Record was successfully displayed.")            
        else:
            print("Nothing to read, because data parameter is empty")
            return False

    # Update Method.   
    def myupdate(self, lookup, data):
        if lookup is not None:
            self.database.animals.update_one(lookup, {"$set": data})
            print("Record was successfully updated.") 
            return True
        else:
            print("Nothing to update, because lookup parameter was empty")
            return False

     # Delete Method.   
    def mydelete(self, data):
        if data is not None:
            self.database.animals.delete_one(data)
            print("Record was successfully deleted.") 
            return True
        else:
            print("Nothing to delete, because data parameter was empty")
            return False