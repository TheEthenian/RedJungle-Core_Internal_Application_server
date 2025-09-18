from pydantic import BaseModel


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
    salt: str
    mfa_secret: str
    last_login_at: str
    failed_login_attempts: int

    reset_tokens: list


class Session_Object(BaseModel):
    session_id: str
    credential_id: str
    token_hash: str
    expires_at: str
    ip_address: str


class Password_Reset_Token(BaseModel):
    token: str
    expires_at: str
    is_used: bool
    credentials: list





