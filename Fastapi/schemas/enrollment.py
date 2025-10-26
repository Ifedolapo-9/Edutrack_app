from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Enrollment(BaseModel):
    id: str
    user_id: str
    course_id: str
    registration_date: datetime
    completed: bool = False
    is_registered: bool = True

class EnrollmentCreate(BaseModel):
    user_id: str
    course_id: str
    registration_date: datetime


class EnrollmentUpdate(BaseModel):
    user_id: str
    course_id: str
    registration_date: datetime

class Response(BaseModel):
    success: bool = True
    message: Optional [str] = None
    data: Optional[Enrollment | list [Enrollment]] = None

