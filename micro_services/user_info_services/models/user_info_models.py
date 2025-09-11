from pydantic import BaseModel

class User_Object(BaseModel):
    user_id: str
    tenant_id: str
    role_id: str
    status: str
    created_at: str
    updated_at: str

class User_Profile_Object(BaseModel):
    user_id: str
    profile_picture: str = null
    first_name: str
    last_name: str
    email: str
    phone_number: str

class Role_Object(BaseModel):
    role_id: str
    role_name: str
    description: str


class Log_Entry_Object(BaseModel):
    log_id: str
    timestamp: str
    source_service: str
    event_type: str
    user_id: str
    tenant_id: str
    details: str















