from pydantic import BaseModel


class Event_Log_Object(BaseModel):
    event_id: str
    timestamp: str
    service_id: str
    user_id: str
    tenant_id: str
    metadata: dict


class Metric_Object(BaseModel):
    metric_id: str
    metric_name: str
    tenant_id: str
    value: float
    timestamp: str
    filters: dict








