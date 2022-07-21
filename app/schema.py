from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    id: Optional[int] = Field(...)
    nome: str = Field(...)
    idade: int = Field(...)
    email: EmailStr = Field(...)
    
    class Config:
        orm_mode = True

