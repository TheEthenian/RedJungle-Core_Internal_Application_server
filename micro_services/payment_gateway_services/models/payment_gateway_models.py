from pydantic import BaseModel

class Transaction_Object(BaseModel):
    transaction_id: str
    user_id: str
    tenant_id: str
    amount: float
    status: str
    bank_id: str
    card_brand: str 
    card_last_four_digits: int
    created_at: str


class Bank_Object(BaseModel):
    bank_id: str
    user_id: str
    card_brand: str
    card_number: str
    card_expiration_date: str
    account_balance: float
    updated_at: str


class Send_Log_Data(BaseModel):
    source_service: str
    service_uri: str
    action_crud: str
    user_id: str
    tenant_id: str
    details: dict


class Incoming_Data(BaseModel):
    workflow_id: str
    step_number: int
    authorization_token: str
    payload: dict





