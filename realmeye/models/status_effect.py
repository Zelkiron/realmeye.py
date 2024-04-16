from pydantic import BaseModel, field_validator
from typing import List, Optional

class StatusEffect(BaseModel):
    """A StatusEffect object to represent retrieved status effects."""
    name: str
    description: List[str]

    @field_validator('name')
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError('Status effect name must not be empty')
        return v
