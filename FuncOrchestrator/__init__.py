# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    
    result1 = yield context.call_activity('FuncActivity', "Blood Count")
    result2 = yield context.call_activity('FuncActivity', "Metabolic Panel")
    result3 = yield context.call_activity('FuncActivity', "Lipid Panel")
    return [result1, result2, result3]
    '''
    parallel_task = []
    parallel_task.append(context.call_activity('FuncActivity', "Blood Count"))
    parallel_task.append(context.call_activity('FuncActivity', "Metabolic Panel"))
    parallel_task.append(context.call_activity('FuncActivity', "Lipid Panel"))
    
    results = yield context.task_all(parallel_task)
    return results
    
    '''
main = df.Orchestrator.create(orchestrator_function)