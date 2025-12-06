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
    bank_name: str
    customers: list


class Bank_Customer_Object(BaseModel):
    bank_customer_id: str
    user_id: str
    card_brand: str
    card_number: str
    card_expiration_date: str
    account_balance: float
    updated_at: str
    banks: list


class Incoming_Data(BaseModel):
    server_authorization_token: str
    payload: dict





