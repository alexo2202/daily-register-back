from src.db.db_connection import connection
from src.db.db_operation import operations

def get_operation():
    connect = connection("dailyregister").get_collection()
    operation = operations(connect)
    return operation

