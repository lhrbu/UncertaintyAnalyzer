from flask import Flask
from flask import request
from WorkflowConfig import WorkflowConfig
from WorkflowService import WorkflowSerivce
from JsonSerializerHook import JsonSerializerHook
import json
from flask.json import jsonify
app = Flask(__name__)




@app.route('/',methods=['POST'])
def hello_world():
    workflowConfig = json.loads(request.get_data(),object_hook=JsonSerializerHook.FromDict)
    workflowService= WorkflowSerivce()
    result = workflowService.Start(workflowConfig)
    return jsonify(result)