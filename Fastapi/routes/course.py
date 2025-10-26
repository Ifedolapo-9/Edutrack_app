from uuid import UUID
from fastapi import APIRouter, HTTPException
from schemas.course import CourseCreate, CourseUpdate, Response
from services.course import course_service
from services.enrollment import enrollment_service

course_router = APIRouter()

@course_router.get("/details/{course_id}", status_code=200, response_model=Response, summary="Get a course by ID")
def get_course_by_id(course_id: UUID):
    course = course_service.get_course_by_id(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="course does not exist")
    return Response(message="Success", data=course)

@course_router.post("/create", status_code=201, response_model=Response, summary="Create a new course")
def create_course(course_data: CourseCreate):
    course = course_service.create_course(course_data)
    return Response(message="Course was successfully created", data=course)

@course_router.patch("/update/{course_id}", status_code=200, response_model=Response, summary="Update a course")
def update_course(course_id: UUID, course_data: CourseUpdate):
    course = course_service.update_course(course_id, course_data)
    if not course:
        raise HTTPException(
            status_code=404,
            detail=f"Course with id: {course_id} not found"
        )
    return Response(message= "Course was updated successfully", data=course)


@course_router.delete("/delete/{course_id}", status_code=200, response_model=Response, summary="Delete course's details")
def delete_course(course_id: UUID):
    course = course_service.delete_course(course_id)
    if not course:
        raise HTTPException(
            status_code=404,
            detail=f"Course with id: {course_id} not found"
        )
    return Response(message= "Course was deleted successfully", data=course)


@course_router.patch("/deactivate/{course_id}", status_code=200, response_model=Response, summary="Deactivate a course")
def unenroll_course(course_id: UUID):
    updated_course = course_service.unenroll_course(course_id)
    if not updated_course:
        raise HTTPException(
            status_code=404,
            detail=f"Course with id: {course_id} not found"
        )
    return Response(message= "Course deactivated successfully", data=updated_course)


@course_router.get("/users/{course_id}", status_code=200, response_model=Response, summary="View all users enrolled for a particular course")
def view_specific_user_enrollments(course_id: UUID):
    return enrollment_service.list_all_users_who_enrolled_for_a_course(course_id)