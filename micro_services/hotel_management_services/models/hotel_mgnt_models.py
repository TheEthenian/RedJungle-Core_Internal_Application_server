from pydantic import BaseModel

class Room_Object(BaseModel):
    room_id: str
    room_no: int
    hotel_id: str
    status: str
    price: float
    amenity_id: str
    pictures: list
    amenities: list


class Room_Picture_Object(BaseModel):
    picture_id: str
    room_id: str
    picture_url: str
    date_created: str
    rooms: list


class Room_Amenity_Object(BaseModel):
    amenity_id: str
    amenity_name: str
    amenity_description: str
    max_occupancy: int
    rooms: list


class Maintenance_Request_Object(BaseModel):
    request_id: str
    hotel_id: str
    room_id: str
    maintenance_description: str
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





