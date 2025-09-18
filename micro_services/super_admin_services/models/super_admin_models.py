from pydantic import BaseModel


class Log_Entry_Object(BaseModel):
    log_id: str
    timestamp: str
    source_service: str
    event_type: str
    user_id: str
    tenant_id: str
    details: str


class Tenant_Object(BaseModel):
    tenant_id: str
    tenant_name: str
    subscription_plan: str
    status: str
    created_at: str


class Super_Admin_Object(BaseModel):
    super_admin_id: str
    user_id: str
    created_at: str
    last_login_at: str


class Billing_Info_Object(BaseModel):
    billing_info_id: str
    super_admin_id: str
    tenant_id: str
    next_payment_in_days: int
    total_amount: float
    payment_transaction_id: str
    


