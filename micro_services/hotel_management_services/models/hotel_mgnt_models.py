from pydantic import BaseModel

class Room_Object(BaseModel):
    room_id: str
    room_no: int
    room_pictures: list(str)
    hotel_id: str
    room_type_id: str
    status: str
    price: float
    amenities: list


class Room_Type_Object(BaseModel):
    room_type_id: str
    hotel_id: str
    name: str
    description: str
    max_occupancy: int


class Staff_User_Object(BaseModel):
    staff_id: str
    hotel_id: str
    first_name: str
    last_name: str
    email: str
    role: str
    status: str


class Service_Object(BaseModel):
    service_id: str
    hotel_id: str
    name: str
    description: str
    price: float
    operation_schedule: list(str)


class Maintenance_Request_Object(BaseModel):
    request_id: str
    hotel_id: str
    room_id: str
    description: str
    price: float
    reported_by_staff_id: str
    status: str


class Log_Entry_Object(BaseModel):
    log_id: str
    timestamp: str
    source_service: str
    event_type: str
    user_id: str
    tenant_id: str
    details: str





