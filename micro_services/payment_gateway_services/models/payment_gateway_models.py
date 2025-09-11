from pydantic import BaseModel


class Log_Entry_Object(BaseModel):
    log_id: str
    timestamp: str
    source_service: str
    event_type: str
    user_id: str
    tenant_id: str
    details: str


class Transaction_Object(BaseModel):
    transaction_id: str
    booking_id: str = 'null'
    user_id: str
    tenant_id: str
    amount: float
    status: str
    payment_method: str
    gateway_response: dict
    created_at: str


class Paymenet_Method_Object(BaseModel):
    method_id: str
    user_id: str
    gateway_token: str
    card_brand: str
    last_four_digits: int
    card_expiration_date: str
    is_default: str
    created_at: str





