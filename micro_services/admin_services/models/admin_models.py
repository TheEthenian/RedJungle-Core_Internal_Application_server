from pydantic import BaseModel


class Hotel_Object(BaseModel):
    hotel_id: str 
    hotel_name: str 
    tenant_id: str 
    address: str 
    city: str 
    country: str 
    contact_info: dict 


class Admin_User_Object(BaseModel):
    admin_user_id: str
    user_id: str
    hotel_id: str
    tenant_id: str
    role: str


class Hotel_Configuration_Object(BaseModel):
    config_id: str
    hotel_id: str
    config_name: str
    config_value: dict
    last_updated_admin_id: str
    last_updated_timestamp: str




