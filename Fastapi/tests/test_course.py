from uuid import uuid4

def test_create_course(test_client):
    payload = {
        "title": "JS Basics",
        "description": "Basics of JS",
        "is_open": True,
        }
    response = test_client.post("/courses/create/", json=payload)
    data = response.json()
    assert response.status_code == 201
    assert data["success"] is True
    assert data["data"]["title"] == "JS Basics"
    assert "id" in data["data"]

def test_get_course_by_id(test_client):
    payload = {
        "title": "JS Basics",
        "description": "Basics of JS",
        "is_open": True,
        }
    create_res= test_client.post("/courses/create", json=payload)
    course_id = create_res.json()["data"]["id"]

    response = test_client.get(f"/courses/details/{course_id}")
    data = response.json()

    assert response.status_code == 200
    assert data["data"]["title"] == "JS Basics"

def test_update_course(test_client):
    payload = {
    "title": "JS Basics",
    "description": "Basics of JS",
    "is_open": True,
    }
    create_res = test_client.post("/courses/create", json=payload)
    course_id = create_res.json()["data"]["id"]
    update_payload = {"description": "Updated description for data structures"}
    response = test_client.patch(f"/courses/update/{course_id}", json=update_payload)
    data = response.json()
    assert response.status_code == 200
    assert "Updated description" in data["data"]["description"]

def test_deactivate_course(test_client):
    payload = {
    "title": "JS Basics",
    "description": "Basics of JS",
    "is_open": True,
    }
    create_res = test_client.post("/courses/create", json=payload)
    course_id = create_res.json()["data"]["id"]
    response = test_client.patch(f"/courses/deactivate/{course_id}", json=payload)
    data = response.json()
    assert response.status_code == 200
    assert data["message"] == "Course deactivated successfully"
    assert data["data"]["is_open"] is False

def test_delete_course(test_client):
    payload = {
    "title": "JS Basics",
    "description": "Basics of JS",
    "is_open": True,
    }
    create_res = test_client.post("/courses/create", json=payload)
    course_id = create_res.json()["data"]["id"]
    response = test_client.delete(f"/courses/delete/{course_id}")
    data = response.json()

    assert response.status_code == 200
    assert data["message"] == "Course was deleted successfully"

def test_view_users_enrolled_for_course(test_client):
    course_payload = {
        "title": "JS Basics",
        "description": "Learn JS",
        "is__open": True
    }

    create_course = test_client.post("/courses/create", json=course_payload)
    course_id = create_course.json()["data"]["id"]

    user_payload = {
        "name": "ife",
        "email": "ife@gmail.com",
        "is__active": True
    }

    create_user = test_client.post("/users/create", json=user_payload)
    user_id = create_user.json()["data"]["id"]
    
    enrollment_payload = {"user_id": user_id, "course_id": course_id}
    test_client.post("/enrollments/", json=enrollment_payload)

    response = test_client.get(f"/courses/users/{course_id}")
    data = response.json()
    assert response.status_code == 200
    assert "data" in data
    assert isinstance(data["data"], list)
    assert any(u["id"] == user_id for u in data["data"])