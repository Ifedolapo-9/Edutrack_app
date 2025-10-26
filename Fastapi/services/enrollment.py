from uuid import UUID, uuid4
from fastapi import HTTPException
from database import users, courses, enrollments
from schemas.enrollment import Enrollment, EnrollmentCreate, EnrollmentUpdate

class EnrollmentService:

    # @staticmethod
    # def get_enrollment_by_id(enrollment_id):
    #     user = users.get(str(user_id))
    #     if not user:
    #         return None
    #     return user
    
    @staticmethod
    def create_user_enrollment(data: EnrollmentCreate):
        
        # Check if user is active
        if not EnrollmentService.is_user_active(data.user_id):
                raise HTTPException(status_code=422, details="This user is not active")

        # Check if course is open
        if not EnrollmentService.is_course_open(data.course_id):
                raise HTTPException(status_code=422, details="This course is not open")


        # Check if user has already enrolled for the course
        for enrollment in enrollments.values():
            if enrollment.user_id == data.user_id and enrollment.course_id == data.course_id:
                raise HTTPException(status_code=422, details="This user is not active")


        enrolled_for_course = Enrollment(id=str(uuid4()), **data.model_dump())
        enrollments[enrolled_for_course.id] = enrolled_for_course
        return enrolled_for_course

    @staticmethod
    def get_all_enrollments():
        enrollment_data = {}

        for enrollment in enrollments.values():
            course = courses.get(enrollment.course_id)
            user = users.get(enrollment.user_id)


            if not course or not user:
                continue
            if enrollment.course_id not in enrollment_data:
                    enrollment_data[enrollment.course_id] = {
                    "enrollment_id": enrollment.id,
                    "course_id": course.id,
                    "course_title": course.title,
                    "enrolled_date": enrollment.registration_date,
                    "course_is_completed": enrollment.completed,
                    "enrollments": []     
                    }
            

            enrollment_data[enrollment.course_id]["enrollments"].append({
                "enrollment_id": enrollment.id,
                "user_id":user.id,
                "user_name": user.name,
                "user_email":user.email,
                "course_title": course.title,
                "enrolled_date": enrollment.registration_date,
                "course_is_completed": enrollment.completed     
            })

        return {
             "success": True,
             "message": "Data fetched successfully",
             "data": list(enrollment_data.values())
        }

    @staticmethod
    def mark_completed(enrollment_id:UUID):
        enrollment = enrollments.get(str(enrollment_id))

        if not enrollment:
            raise HTTPException(status_code=404, detail=f"Enrollment with id: {enrollment_id} does not exist")
        enrollment.completed == True    
        return enrollment

    @staticmethod
    def get_all_user_enrollments(user_id:UUID):
        all_user_enrollments = []

        for enrollment in enrollments.values():
             if enrollment.user_id == str(user_id):
                course = courses.get(enrollment.course_id)
                if course:
                    all_user_enrollments.append({
                        "enrollment_id":enrollment.id,
                        "enrolled_date": enrollment.registration_date,
                        "course_id": course.id,
                        "course_title": course.title,
                        "course_is_open": course.is_open,
                        "course_is_completed": enrollment.completed,
                    })
        
        return {
             "success": True,
             "message": "Data fetched successfully",
             "data": all_user_enrollments
        }

    @staticmethod
    def list_all_users_who_enrolled_for_a_course(course_id: UUID):
        course_specific_user_enrollments = []

        for enrollment in enrollments.values():
             if course_id == courses.get(enrollment.course_id) and enrollment.is_registered:
                course = courses.get(enrollment.course_id)
                user = users.get(enrollment.user_id)

                if not course or not user:
                    continue

                if enrollment.user_id not in course_specific_user_enrollments:
                        course_specific_user_enrollments[enrollment.user_id] = {
                        "user_id": enrollment.id,
                        "name": course.id,
                        "email": course.title,
                        "user_is_active":user.is_active,
                        "courses": []     
                        }
                

                course_specific_user_enrollments[enrollment.course_id]["enrollments"].append({
                    "id": course.id,
                    "title":course.title,
                    "description": course.description,
                    "course_title": course.title,
                    "enrolled_date": enrollment.registration_date,
                    "course_is_completed": enrollment.completed     
                })

        return {
            "success": True,
            "message": "Data fetched successfully",
            "data": course_specific_user_enrollments
        }

    
    @staticmethod
    def is_user_active(user_id:str):
        user = users.get(str(user_id))
        if not user:
            raise HTTPException(status_code=404, detail=f"User with id: {user_id} does not exist")
        return user.is_active == True
    
    @staticmethod
    def is_course_open(course_id:str):
        course = courses.get(str(course_id))
        if not course:
            raise HTTPException(status_code=404, detail=f"Course with id: {course_id} does not exist")
        return course.is_open == True

enrollment_service = EnrollmentService()