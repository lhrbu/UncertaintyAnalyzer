class TaskDispatchMessage:
    def __init__(self,databaseName,tableName,testId,
        calculateModuleName,calculateMethodName):
        self.DatabaseName = databaseName
        self.TableName = tableName
        self.TestId = testId
        self.CalculateModuleName = calculateModuleName
        self.CalculateMethodName = calculateMethodName

    DatabaseName:str
    TableName:str
    TestId:int
    CalculateModuleName:str
    CalculateMethodName:str