from uuid import uuid4
from datetime import datetime
from schemas.user import User 
from schemas.course import Course
from schemas.enrollment import Enrollment

users: dict[str, User] = {}
courses: dict[str, Course] = {}
enrollments: dict[str, Enrollment] = {}
# enrolled_users: dict[str, EnrolledUsers] = {}

# User data sample

user_data = [
    {"name": "Ifedolapo Ojo", "email": "ifedolapoojow@gmail.com"},
    {"name": "Bob Marley", "email": "bob@example.com"}
]


# Course data sample

course_data = [
    {"title": "Python Basics", "description": "Learn Python"},
    {"title": "JavaScript Basics", "description": "Learn JavaScript"}
]