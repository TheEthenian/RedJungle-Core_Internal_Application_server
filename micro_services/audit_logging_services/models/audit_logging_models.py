from pydantic import BaseModel


class Log_Object(BaseModel):
    log_id: str
    source_service: str
    service_uri: str
    action_crud: str
    user_id: str
    tenant_id: str
    created_at: str
    details: list


class Detail_Object(BaseModel):
    detail_id: str
    detail_name: str
    detail_description: str


class Incoming_Data(BaseModel):
    source_service: str
    action: str
    user_id: str
    tenant_id: str
    details: dict







