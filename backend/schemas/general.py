from pydantic import BaseModel


class SuccessResponse(BaseModel):
    ok: bool = True


class PhoneHashCode(BaseModel):
    phone_code_hash: str