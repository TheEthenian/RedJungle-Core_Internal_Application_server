from pydantic import BaseModel

class Review_Object(BaseModel):
    review_id: str
    user_id: str
    tenant_id: str
    date_created: str
    date_updated: str


class Picture_Object(BaseModel):
    picture_id: str
    picture_url: str
    date_created: str


class Message_Object(BaseModel):
    message_id: str
    message_text: str
    date_created: str
    date_updated: str
    

class Log_Entry_Object(BaseModel):
    log_id: str
    timestamp: str
    source_service: str
    event_type: str
    user_id: str
    tenant_id: str
    details: str





