class ModuleConfig:
    def __init__(self,testId:int,
        moduleName:str,methodName:str):
        self.TestId = testId
        self.ModuleName = moduleName
        self.MethodName = methodName
    TestId:int
    ModuleName:str
    MethodName:str