from TaskDispatchMessage import *
import psycopg2

class DatabaseLinkService:
    TestIdColumnName:str ="TestId"
    DataColumnName:str="Value"

    def FetchData(self,taskDispatchMessage:TaskDispatchMessage):
        with psycopg2.connect(user="postgres",host="localhost",
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



    