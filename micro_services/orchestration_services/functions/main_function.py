from databank.orchestration_schema_data.workflow_data import workflow_object
from databank.orchestration_schema_data.service_data import service_object
from databank.orchestration_schema_data.step_data import step_object
from databank.orchestration_schema_data.sub_workflow_data import sub_workflow_object

import yaml


########################################################################

workflow_progress= []

for workflow_item in workflow_object:
    for step_item in step_object:
        if step_item['workflow_id'] == workflow_item['workflow_id']:
            workflow_item['steps'].append(step_item)
        


for workflow_item in workflow_object:
    for sub_workflow in sub_workflow_object:
       if sub_workflow['master_workflow_id']  == workflow_item["workflow_id"]:
            workflow_item['sub_workflows'].append(sub_workflow)


def step_detail_info(list_step):
    enumeration_list = []

    for step in list_step:
        for service in service_object:
            if step['service_id'] == service['service_id']:
                step_order = step['execution_order']
                step_relative = step['relative_url']
                service_url = service['endpoint']
                service_name = service['service_name']

                enumeration_list.append([f'Execution_order: {step_order}',f'Service: {service_name}','full_url: ',f'{service_url}{step_relative}'])

    return enumeration_list


def assistant_workflow_enumeration(list_sub_workflow):
    sub_workflow_data = []

    for sub in list_sub_workflow:
        execution_order = sub['execution_order']
        for workflow in workflow_object:
            if workflow['workflow_id'] == sub['assistance_workflow_id']:

                workflow_name = workflow['workflow_name']
                steps_enumeration = step_detail_info(workflow['steps'])
                sub_workflow_enumeration = assistant_workflow_enumeration(workflow['sub_workflows'])
                
                sub_workflow_data.append(['Execution_order: ',execution_order,'assistance_workflow_name: ',workflow_name,'Sub_workflows: ',sub_workflow_enumeration,'Steps: ',steps_enumeration])
                
                return sub_workflow_data


workflow_location_number = 29

print('//////////// START ENUMERATION ///////////////////')
print('Workflow_name: ',workflow_object[workflow_location_number]['workflow_name'])
print('-----------------------------------------------------------')
print('Sub_Workflows: ',assistant_workflow_enumeration(workflow_object[workflow_location_number]['sub_workflows']))
print('-----------------------------------------------------------')
print('Steps: ',step_detail_info(workflow_object[workflow_location_number]['steps']))
print('-----------------------------------------------------------')




#########################################################################

def load_yaml_config(filepath):
    with open(filepath, 'r') as f:
        config = yaml.safe_load(f)
    return config


def task_name_lookup(given_name):

    for workflow in workflow_object:

        if workflow['workflow_name'] == given_name:

            steps_list = workflow['steps']
            total_steps_count = len(steps_list)
            print(total_steps_count)

            current_step_count = 1
            step_iteration = 0

            while step_iteration < total_steps_count:
                for singular_step in steps_list:
                    if singular_step['execution_order'] == current_step_count:

                        for service in service_object:
                            if service['service_id'] == singular_step['service_id']: 
                                print(service['service_name'], service['endpoint'],singular_step['relative_url'], singular_step['execution_order'])

                step_iteration += 1
                current_step_count += 1

                
#task_name_lookup('delete_tenant')



def workflow_complete_execution_order(workflow_list,steps_list):
    pass






















