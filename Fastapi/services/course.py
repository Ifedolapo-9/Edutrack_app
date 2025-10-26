from uuid import UUID, uuid4
from fastapi import HTTPException
from database import courses
from schemas.course import Course, CourseUpdate, CourseCreate

class CourseService:

    @staticmethod
    def get_course_by_id(course_id):
        course = courses.get(str(course_id))
        if not course:
            return None
        return course
    
    @staticmethod
    def create_course(course_data: CourseCreate):
        course = Course(id=str(uuid4()), **course_data.model_dump())
        courses[course.id] = course
        return course

    @staticmethod
    def update_course(course_id: UUID, course_data: CourseUpdate):
        course = courses.get(str(course_id))
        if not course:
            return None

        course.title = course_data.title
        course.description = course_data.description
        return course       
    
    @staticmethod
    def delete_course(course_id: UUID):
        course = courses.get(str(course_id))
        if not course:
            return None
        
        del courses[course.id]
        return course
    
    @staticmethod
    def unenroll_course(course_id:UUID):
        course = courses.get(str(course_id))
        if not course:
            return None
        
        course.is_open = False
        return course
    

    # @staticmethod
    # def get_assigned_users_for_course(course_id: UUID):
    #     course = courses.get(str(course_id))
    #     if not course:
    #         raise HTTPException(
    #             status_code=404,
    #             detail=f"Course with ID: {course_id} doesn't exist"
    #         )
        

    #     enrolled_users = course
    #     return True
    
    
course_service = CourseService()
