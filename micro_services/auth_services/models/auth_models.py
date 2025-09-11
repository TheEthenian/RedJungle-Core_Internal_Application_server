from pydantic import 


class Log_Entry_Object(BaseModel):
    log_id: str
    timestamp: str
    source_service: str
    event_type: str
    user_id: str
    tenant_id: str
    details: str


class Credential_Object(BaseModel):
    credential_id: str
    user_id: str
    email: str
    hashed_password: str
    mfa_secret: str
    last_login_at: str
    failed_login_attempts: int
    password_reset_token: str


class Session_Object(BaseModel):
    token_id: str
    user_id: str
    token: str
    status: str
    issued_at: str
    expires_at: str






