from pymongo import MongoClient

class connection:
    def __init__(self, collection_name):
        client = MongoClient(
            "mongodb+srv://dev:1!QAZ2wsx.@cluster0.clvxd.mongodb.net/techapp?retryWrites=true&w=majority")
        db = client.documentation
        self.collection = db[collection_name]

    def get_collection(self):
        return self.collection

