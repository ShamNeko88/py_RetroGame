import sqlalchemy 

USER_NAME:str = "postgres"
PASSWORD:str = "postgres"
LOCAL_HOST:str = "localhost:5432"
DATABASE_NAME:str = "retoro_db"
ENGIN:str = f"postgresql://{USER_NAME}:{PASSWORD}@{LOCAL_HOST}/{DATABASE_NAME}"

engin = sqlalchemy.create_engine(ENGIN)
with engin.begin() as connection:
    sql = sqlalchemy.text("SELECT * FROM test_users")
    result = connection.execute(sql)
    for i in result:
        print(i)
class ConnectDatabase:
    def __init__(self, database=None):
        self.database = database
    
    def connect_database(self):
        pass