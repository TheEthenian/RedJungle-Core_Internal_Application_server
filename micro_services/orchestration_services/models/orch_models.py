from pydantic import BaseModel

class Log_Entry_Object(BaseModel):
    log_id: str
    timestamp: str
    source_service: str
    event_type: str
    user_id: str
    tenant_id: str
    details: str


class Workflow_Excecution_Object(BaseModel):
    workflow_id: str
    user_id: str
    tenant_id: str
    status: str
    data_payload: str
    step_history: list(str)


class Workflow_Definition_Object(BaseModel):
    workflow_id: str
    workflow_name: str
    steps: list(str)


class Workflow_Step_Object(BaseModel):
    step_id: str
    step_name: str
    service_id: str


class Workflow_Service_Object(BaseModel):
    service_id: str
    service_name: str
    api_base_url: str
    http_method: str
    data_payload: dict = null
    authentication_details: dict











