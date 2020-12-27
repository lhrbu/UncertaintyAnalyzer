from DbConnectConfig import DbConnectConfig
import psycopg2

class DbLinkService:
    def __init__(self,host:str="localhost",user="postgres"):
        self.__host = host
        self.__user = user
    __host:str
    __user:str
    
    def FetchData(self,keyValue,dbConnectConfig:DbConnectConfig):
        with psycopg2.connect(user=self.__user,host=self.__host,
            database=dbConnectConfig.DatabaseName) as conn:
            curr = conn.cursor()
            sql = "SELECT {0} FROM {1} WHERE {2}={3}".format(
                dbConnectConfig.ValueColumnName,
                dbConnectConfig.TableName,
                dbConnectConfig.KeyColumnName,
                keyValue)
            curr.execute(sql)
            data = curr.fetchall()
            return tuple(map(lambda item:item[0],data))



    