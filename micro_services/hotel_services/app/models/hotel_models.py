from pydantic import BaseModel


class Hotel_Object(BaseModel):
    hotel_id: str 
    hotel_name: str 
    tenant_id: str 
    admin_user_id: str
    location: str
    contact_number: int 
    configs: list
    services:list


class Hotel_Service_Object(BaseModel):
    service_id: str
    service_name: str
    service_description: str
    price: float
    operation_schedule: str
    hotels: list


class Hotel_Configuration_Object(BaseModel):
    config_id: str
    config_name: str
    config_value: str
    last_updated_admin_id: str
    last_updated_timestamp: str
    hotels: list


class Send_Log_Data(BaseModel):
    source_service: str
    service_uri: str
    action_crud: str
    user_id: str
    tenant_id: str
    details: dict


class Incoming_Data(BaseModel):
    server_authorization_token: str
    payload: dict


class Delete_Data(BaseModel):
    server_authorization_token: str
    target_object_id: str
    JWT: str










