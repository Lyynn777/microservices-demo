from pydantic import BaseModel, Field

class User(BaseModel):
    id: str | None = None
    name: str = Field(..., example="Alice")
    credit: float = Field(..., ge=0, example=100.0)
    status: str = Field("active", example="active")  # active | suspended
