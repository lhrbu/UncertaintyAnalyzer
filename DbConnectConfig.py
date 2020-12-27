class DbConnectConfig:
    def __init__(self,databaseName:str,tableName:str,keyColumnName:str,valueColumnName:str):
        self.DatabaseName = databaseName
        self.TableName = tableName
        self.KeyColumnName = keyColumnName
        self.ValueColumnName = valueColumnName
    DatabaseName:str
    TableName:str
    KeyColumnName:str
    ValueColumnName:str
