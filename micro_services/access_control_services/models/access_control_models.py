from pydantic import BaseModel


class Policy_Object(BaseModel):
    policy_id: str
    policy_name: str
    description: str


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










