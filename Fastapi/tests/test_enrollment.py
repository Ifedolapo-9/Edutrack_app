import uuid 

def test_enroll_for_course(test_client):
    payload = {
        "user_id":str(uuid.uuid4()),
        "course_id": str(uuid.uuid4())              
    }
    response = test_client.post("/enrollments/", json=payload)
    data = response.json()
    assert response.status_code == 201
    assert data["success"] is True
    assert "Enrollment was successfully done" in data["message"]

def test_mark_enrollment_completed(test_client):
    enrollment_id = str(uuid.uuid4())
    response = test_client.patch(f"/enrollments/mark-completed/{enrollment_id}")
    data = response.json()


    if response.status_code == 404:
        assert "does not exist" in data["detail"].lower()
    else:
        assert response.status_code == 200
        assert "Enrollment has been completed" in data["message"]


def test_view_user_enrollments(test_client):
    user_id = str(uuid.uuid4())
    response = test_client.get(f"/enrollments/user/{user_id}")
    data = response.json()
    assert response.status_code == 200
    if data == []:
        assert response.status_code == 200
    assert "data" in data


def test_view_all_enrollments(test_client):
    user_id = str(uuid.uuid4())
    response = test_client.get(f"/enrollments/user/{user_id}")
    data = response.json()
    assert response.status_code == 200
    assert "data" in data

def test_view_all_enrollments(test_client):
    response = test_client.get("/enrollments/")
    data = response.json()
    assert response.status_code == 200
    assert "data" in data
    assert data["success"] is True
