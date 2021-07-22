from bson.json_util import _json_convert, dumps, loads

class operations:
    def __init__(self, collection):
        self.collection = collection

    def insert(self, document):
        self.collection.insert_one(document)
        return True

    def getdatabase(self):
        result = self.collection.find()
        json_string = dumps(result)
        back_to_dict = loads(json_string)
        print(back_to_dict.split)
        return {'intento': 'respuesta'}

    def get_find_mongo_collection(self):
        result_collection = self.collection.find()
        return {"result": _json_convert(result_collection)}
