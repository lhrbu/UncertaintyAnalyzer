import importlib
from WorkflowConfig import WorkflowConfig

class WorkflowSerivce:
    def Start(self,workflowConfig:WorkflowConfig):
        module = importlib.import_module(workflowConfig.ModuleConfig.ModuleName)
        entryMethod = getattr(module,workflowConfig.ModuleConfig.EntryMethod)
        return entryMethod(workflowConfig.DbConfigs)