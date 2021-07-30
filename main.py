from src.utils.configuration import get_operation
from src.business.register_event_business import register_event_business
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_data_connection():
    connection = get_operation()
    event_business = register_event_business(connection)
    return event_business

business = get_data_connection()

@app.route('/registerevent', methods=["POST"])
def registerevent():
    state = False
    try:
        register = request.json
        business.insert(register)
        state = True
    except:
        print("error")
    finally:
        return {"status": state}


@app.route('/getregisters')
def getregisters():
    return business.get_find_mongo_collection()

