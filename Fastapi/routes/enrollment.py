from uuid import UUID
from fastapi import APIRouter, HTTPException
from schemas.enrollment import EnrollmentCreate, EnrollmentUpdate, Response
from services.enrollment import enrollment_service

enrollment_router = APIRouter()

@enrollment_router.post("/", status_code=201, response_model=Response, summary="Enroll a user for a course")
def enroll_for_course(enrollment_data: EnrollmentCreate):
    enrolled = enrollment_service.create_user_enrollment(enrollment_data)
    return Response(message="Enrollment was successfully done", data= enrolled)

@enrollment_router.patch("/mark-completed/{enrollment_id}", status_code=200, response_model=Response, summary="Mark a course completion")
def complete_enrollment(enrollment_id: UUID):
    enrollment_completed = enrollment_service.mark_completed(enrollment_id)
    if not enrollment_completed:
        raise HTTPException(
            status_code=404,
            detail=f"Enrollment with id: {enrollment_id} not found"
        )
    return Response(message= "Enrollment has been completed", data=enrollment_completed)

@enrollment_router.get("/user/{user_id}", status_code=200, response_model=Response, summary="View all enrollments for a specific user")
def view_user_enrollments(user_id: UUID):
    return enrollment_service.get_all_user_enrollments(user_id)


@enrollment_router.get("/", status_code=200, response_model=Response, summary="View all enrollments")
def view_all_enrollments():
    return enrollment_service.get_all_enrollments()
