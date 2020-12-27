from typing import Dict
from DbConnectConfig import DbConnectConfig
from ModuleConfig import ModuleConfig

class WorkflowConfig:
    ModuleConfig:ModuleConfig
    DbConfigs:Dict[str,DbConnectConfig] = {}