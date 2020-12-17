from TaskDispatchMessage import *
from DatabaseLinkService import *
import importlib
import sys

def Dispatch(taskDispatchMessage:TaskDispatchMessage)->float:
    databaseLinkService = DatabaseLinkService()
    data = databaseLinkService.FetchData(taskDispatchMessage)
    calculateModule=importlib.import_module(taskDispatchMessage.CalculateModuleName)
    calculateMethod = getattr(calculateModule,taskDispatchMessage.CalculateMethodName)
    return calculateMethod(data)