
class register_event_business:

    def __init__(self, operation):
        self.operations = operation

    def insert(self, document):
        self.operations.insert(document)
        return True

    def get_find_mongo_collection(self):
        find_result = self.operations.get_find_mongo_collection()
        return {"result": find_result}

