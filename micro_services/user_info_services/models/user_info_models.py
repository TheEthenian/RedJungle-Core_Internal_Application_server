from pydantic import BaseModel

class User_Object(BaseModel):
    user_object_id: str
    tenant_id: str
    role_id: str
    created_at: str
    updated_at: str

class User_Profile_Object(BaseModel):
    user_profile_id: str
    profile_picture: str 
    first_name: str
    last_name: str
    email: str
    phone_number: int 


class Log_Entry_Object(BaseModel):
    source_service: str
    event_type: str
    user_object_id: str
    tenant_id: str
    details: str















