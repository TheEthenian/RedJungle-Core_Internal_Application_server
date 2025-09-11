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
    status: str
    subscription_plan: str
    billing_info_id: str
    created_at: str


class Super_Admin_Object(BaseModel):
    super_admin_id: str
    user_id: str
    tenant_id: str
    role: str
    status: str
    last_login_at: str


class Global_Configuration_Object(BaseModel):
    config_id: str
    config_name: str
    config_value: str
    tenant_id: str
    last_updated: str















