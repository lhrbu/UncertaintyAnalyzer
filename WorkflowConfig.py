from typing import Dict
from DbConnectConfig import DbConnectConfig
from ModuleConfig import ModuleConfig

class WorkflowConfig:
    Name:str
    ModuleConfig:ModuleConfig
    DbConfigs:Dict[str,DbConnectConfig] = {}