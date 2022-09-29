from pydantic import BaseModel


class UserInput(BaseModel):
    user_name: str
    hashed_password: str
    is_active: str
    email: str
    day_of_birth: int
    month_of_birth: int
    year_of_birth: int
    city_of_birth: str


class AdminInput(BaseModel):
    user_id: int
    is_admin: bool
