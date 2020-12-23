class DatabaseConnectConfig:
    def __init__(self,testId:int,databaseName:str,tableName:str):
        self.TestId = testId
        self.DatabaseName = databaseName
        self.TableName = tableName
    TestId:int
    DatabaseName:str
    TableName:str
