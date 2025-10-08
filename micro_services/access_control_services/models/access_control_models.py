from pydantic import BaseModel


class Policy_Object(BaseModel):
    policy_id: str
    service_id: str
    uri: str
    action: str
    roles: list


class Role_Object(BaseModel):
    role_id: str
    role_name: str
    policies: list


class Decision_Log_Object(BaseModel):
    decision_id: str
    service_id: str
    user_id: str
    tenant_id: str
    resource_targeted: str
    action_crud: str
    allowed: bool 
    policy_based_reason: str
    timestamp: str


class Send_Log_Data(BaseModel):
    source_service: str
    service_uri: str
    action_crud: str
    user_id: str
    tenant_id: str
    details: dict


class Authorization_Incoming_Data(BaseModel):
    service_id: str
    service_uri: str
    object_details: dict
    action: str
    payload: dict


class Incoming_Data(BaseModel):
    server_authorization_token: str
    payload: dict









