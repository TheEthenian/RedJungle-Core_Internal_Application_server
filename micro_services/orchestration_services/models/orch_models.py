from pydantic import BaseModel

# INGRESS & EGRESS DATASTRACTURES

class Data_Zero(BaseModel):
    task_name: str
    task_payload: dict


class Log_Entry_Object(BaseModel):
    log_id: str
    timestamp: str
    source_service: str
    event_type: str
    user_id: str
    tenant_id: str
    details: str



# DATABASE DATASTRUCTURE FOR VARIOUS SCHEMAS

class Workflow_Object(BaseModel):
    workflow_id: str
    workflow_name:str
    steps: list


class Step_Object(BaseModel):
    step_id: str
    service_id: str
    workflow_id: str
    relative_url:str
    execution_order: int
    workflows: list
    services: list


class Sub_Workflow_Object(BaseModel):
    sub_workflow_id: str
    master_workflow_id: str
    assistance_workflow_id: str
    execution_order: int


class Service_Object(BaseModel):
    service_id: str
    service_name: str
    endpoint: str
    steps: list


class Progress_Object(BaseModel):
    progress_id: str
    workflow_id: str
    current_service_id: str
    progress_status: str
    complete_status: str


