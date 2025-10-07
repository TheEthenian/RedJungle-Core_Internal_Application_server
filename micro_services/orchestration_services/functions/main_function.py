from databank.orchestration_schema_data.workflow_data import workflow_object
from databank.orchestration_schema_data.service_data import service_object
from databank.orchestration_schema_data.step_data import step_object
from databank.orchestration_schema_data.sub_workflow_data import sub_workflow_object

import yaml
import httpx 

############################# GLOABAL VARIABLES #############################

final_ordered_steps_collection = []




#########################################################################

def load_yaml_config(filepath):
    with open(filepath, 'r') as f:
        config = yaml.safe_load(f)
    return config

########################################################################

for workflow_item in workflow_object:
    for step_item in step_object:
        if step_item['workflow_id'] == workflow_item['workflow_id']:
            workflow_item['steps'].append(step_item)
        
#########################################################################

for workflow_item in workflow_object:
    for sub_workflow in sub_workflow_object:
       if sub_workflow['master_workflow_id']  == workflow_item["workflow_id"]:
            workflow_item['sub_workflows'].append(sub_workflow)

#########################################################################

def steps_detail_info(list_step):
    enumeration_list = []

    for step in list_step:
        for service in service_object:
            if step['service_id'] == service['service_id']:
                step_order = step['execution_order']
                step_relative = step['relative_url']
                step_request_type = step['request_type']
                service_url = service['endpoint']
                service_name = service['service_name']

                enumeration_list.append({
                    'execution_order': step_order,
                    'service': service_name,
                    'uri': f'{service_url}{step_relative}',
                    'request_type': step_request_type
                    })

    return enumeration_list

#########################################################################

# get all sub workflows
def find_sub_workflows_details(list_sub_workflow):
    sub_workflow_data_initial = []
    sub_workflow_data_arranged = []
    steps_arranged = []

    for sub in list_sub_workflow:

        execution_order = sub['execution_order']

        for workflow in workflow_object:
            if workflow['workflow_id'] == sub['assistance_workflow_id']:

                sub_name = workflow['workflow_name']
                sub_steps = steps_detail_info(workflow['steps'])
                sub_workflow_enumeration_data = find_sub_workflows_details(workflow['sub_workflows'])
                
                sub_workflow_data_initial.append({
                    'execution_order':execution_order,
                    'assistance_workflow_name':sub_name,
                    'steps':sub_steps,
                    'sub_workflows': sub_workflow_enumeration_data
                    })
                    
    
    return sub_workflow_data_initial

#########################################################################

def workflow_name_to_ordered_steps_linkage(given_name):
    steps_amalgamation = []

    for workflow in workflow_object:
        if workflow['workflow_name'] == given_name:
            
            master_steps = steps_detail_info(workflow['steps'])
            master_sub_workflows = find_sub_workflows_details(workflow['sub_workflows'])

            transform_into_ordered_step_list(master_steps, master_sub_workflows)
    
    return final_ordered_steps_collection
    

#########################################################################

def transform_into_ordered_step_list(main_steps,main_sub_workflows):
    main_total_operational_steps = len(main_steps) + len(main_sub_workflows)
    ordered_steps_collection = []

    count = 0

    while count < main_total_operational_steps:
        for step in main_steps:
            if step['execution_order'] == count + 1:
                ordered_steps_collection.append(step)

        for sub_work in main_sub_workflows:
            if sub_work['execution_order'] == count + 1:
                transform_into_ordered_step_list(sub_work['steps'], sub_work['sub_workflows'])


        count += 1

    final_ordered_steps_collection.append(ordered_steps_collection)
    return 

#########################################################################

config_general = load_yaml_config('../config_general.yaml')
base_url = config_general['api_network_base_url']

def full_transactional_api_communication(structured_step_list,initial_payload):

    next_api_transaction_data = ''
    response_data_bank = []
    current_step_index = 0

    while current_step_index < len(structured_step_list):

        current_target_uri = structured_step_list[current_step_index][0]['uri']
        http_request_type = structured_step_list[current_step_index][0]['request_type']

        complete_url = f'{base_url}:{current_target_uri}'

        if current_step_index == 0:
            response_data_from_api = singular_api_data_communication(http_request_type,complete_url,current_target_uri,initial_payload)
            print(response_data)
            next_api_transaction_data = response_data_from_api['data']
            print('This in under iteration',current_step_index,next_api_transaction_data)
            response_data_bank.append(response_data_from_api)

        if current_step_index > 0:
            response_data_from_api = singular_api_data_communication(http_request_type,complete_url,current_target_uri, next_api_transaction_data)
            print(response_data)
            next_api_transaction_data = response_data_from_api['data']
            print('This in under iteration',current_step_index,next_api_transaction_data)
            response_data_bank.append(response_data_from_api)

        current_step_index += 1

    return response_data_bank


#########################################################################

def singular_api_data_communication(http_request_type,complete_url,api_uri,payload):

    if http_request_type == 'get':
        data = httpx.get(complete_url, params=payload)

        response_data = {
            'sender': api_uri,
            'data': data
        }
        return response_data


    if http_request_type == 'post':
        data = httpx.post(complete_url, data=payload)

        response_data = {
            'sender': api_uri,
            'data': data
        }
        return response_data


    if http_request_type == 'put':
        data = httpx.put(complete_url, data=payload)

        response_data = {
            'sender': api_uri,
            'data': data
        }
        return response_data


    if http_request_type == 'delete':
        data = httpx.delete(complete_url, data=payload)

        response_data = {
            'sender': api_uri,
            'data': data
        }
        return response_data


#########################################################################













