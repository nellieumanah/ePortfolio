from pymongo import MongoClient
from bson.objectid import ObjectId

class mycrud(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:50282' % (username, password))
        self.database = self.client['AAC']

# Create method.
    def mycreate(self, data):
        if data is not None:
                result = self.database.animals.insert(data)  # data should be dictionary            
                return True
        else:
            print("Nothing to save, because data parameter is empty")
            return False
# Read Method.
    def myread(self, data):
        if data is not None:
                return self.database.animals.find(data, {"_id": False})  # data should be dictionary            
        else:
            print("Nothing to read, because data parameter is empty")
            return False

    # Update Method.   
    def myupdate(self, lookup, data):
        if lookup is not None:
            self.database.animals.update_one(lookup, {"$set": data})
            return True
        else:
            print("Nothing to update, because lookup parameter was empty")
            return False

     # Delete Method.   
    def mydelete(self, data):
        if data is not None:
            self.database.animals.delete_one(data)
            return True
        else:
            print("Nothing to delete, because data parameter was empty")
            return False