from WorkflowService import WorkflowSerivce
from WorkflowConfig import WorkflowConfig
from ast import Num
from ModuleConfig import ModuleConfig
import json
import argparse
import os
import sys
from json import *
from collections import namedtuple
import jsonpickle
from types import SimpleNamespace


class JsonSerializerHook:
    @classmethod
    def FromDict(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj

def LoadArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f",type=str,help="workflow config json file")
    return parser.parse_args() 



def main():
    args = LoadArgs()
    workflowFilePath = "workflow.json" if not args.f else args.f
    with open(workflowFilePath) as file:
        workflowConfig:WorkflowConfig  = json.load(file,object_hook=JsonSerializerHook.FromDict)
        workflowService = WorkflowSerivce()
        value = workflowService.Start(workflowConfig)
        print(value)

if __name__ == "__main__":
    main()


