import json
import TaskDispatchService
from TaskDispatchMessage import *
import argparse
import os
import sys
from json import *
from collections import namedtuple
from types import SimpleNamespace

def CreateTaskDispatchMessage():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d",type=str,help="database name")
    parser.add_argument("-t",type=str,help="table name")
    parser.add_argument("-i",type=int,help="test id")
    parser.add_argument("-md",type=str,help="module name")
    parser.add_argument("-mt",type=str,help="method name in module")
    args = parser.parse_args()
    SimpleNamespace()
    return TaskDispatchMessage(databaseName=args.d,
        tableName=args.t, testId=args.i,
        calculateModuleName=args.md, calculateMethodName=args.mt)

def main():
    taskDispatchMessage = None
    if len(sys.argv)>=5:
        taskDispatchMessage = CreateTaskDispatchMessage()
    else:
        with open("msg.json","rb") as file:
            dictValues = json.load(file)
            taskDispatchMessage = SimpleNamespace(**dictValues)
            # taskDispatchMessage = namedtuple("TaskDispatchMessage",dictValues.keys())(*dictValues.values())
        
    print(TaskDispatchService.Dispatch(taskDispatchMessage))
    os.system("pause")

if __name__ == "__main__":
    main()


