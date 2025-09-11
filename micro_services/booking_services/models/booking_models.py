from pydantic import BaseModel

class Log_Entry_Object(BaseModel):
    log_id: str
    timestamp: str
    source_service: str
    event_type: str
    user_id: str
    tenant_id: str
    details: str


class Booking_Object(BaseModel):
    booking_id: str
    guest_id: str
    tenant_id: str
    hotel_id: str
    room_id: str
    check_in_date: str
    check_out_date: str
    status: dict
    total_price: float
    payment_transaction_id: str
    created_at: str


class Guest_Object(BaseModel):
    guest_id: str
    user_id: str = None
    booking_id: str
    first_name: str = None
    last_name: str = None
    email: str = None
    phone_number:str = None
    created_at: str = None


class Invoice_Object(BaseModel):
    invoice_id: str
    booking_id: str
    invoice_number: int
    amount_due: str
    status: str
    created_at:str












