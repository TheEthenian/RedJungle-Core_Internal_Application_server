from pydantic import BaseModel

class Log_Entry_Object(BaseModel):
    log_id: str
    timestamp: str
    source_service: str
    event_type: str
    user_id: str
    tenant_id: str
    details: str


class Workflow_Object(BaseModel):
    workflow_id: str
    workflow_name:str
    steps: list


class Step_Object(BaseModel):
    step_id: str
    service_id: str
    workflow_id: str
    step_execution_order: int
    workflows: list
    services: list


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








