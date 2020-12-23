from TaskDispatchMessage import *
import psycopg2
import json

class DatabaseLinkService:
    TestIdColumnName:str ="TestId"
    DataColumnName:str="Value"

    def FetchData(self,taskDispatchMessage:TaskDispatchMessage):
        host = None
        user = None
        password = None
        with open("postgresqlconfig.json","r") as configFile:
            config = json.load(configFile)
            host = config["Host"]
            user = config["User"]
            password = config["Password"]
        with psycopg2.connect(user=user,host=host,
            password=password,
            database=taskDispatchMessage.DatabaseName) as conn:
            curr = conn.cursor()
            sql="SELECT {1} FROM {0} Where {2} = {3}".format(
                taskDispatchMessage.TableName,
                self.DataColumnName,
                self.TestIdColumnName,
                taskDispatchMessage.TestId)
            curr.execute(sql)
            data = curr.fetchall()
            return tuple(map(lambda item:item[0],data))

if __name__ == "__main__":
    taskDispatchMessage =  TaskDispatchMessage("postgres","",1,"cm","cmn")
    service = DatabaseLinkService()
    service.FetchData(taskDispatchMessage)

    