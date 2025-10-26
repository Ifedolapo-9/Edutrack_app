from uuid import uuid4

def test_create_user(test_client):
    payload = {"name": "Ife", "email": "ife@gmail.com"}
    response = test_client.post("/users/create", json=payload)
    assert response.status_code == 201
    assert response.json()["data"]["email"] == "ife@gmail.com"


def test_get_user_by_id(test_client):
    payload = {"name": "Ife", "email": "ife@gmal.com"}
    create_res = test_client.post("/users/create", json=payload)
    user_id = create_res.json()["data"]["id"] 
    response = test_client.get(f"/users/details/{user_id}")
    
    assert response.status_code == 200
    assert response.json()["data"]["name"] == "Ife"

def test_deactivate_user(test_client):
    payload = {"name": "Ife", "email": "ie@gmail.com"}
    create_res = test_client.post("/users/create", json=payload)
    user_id = create_res.json()["data"]["id"]
    response = test_client.patch(f"/users/deactivate/{user_id}")
    data = response.json()
    assert response.status_code == 200
    assert data["data"]["is_active"] is False
    assert data["message"] == "User deactivated successfully"

def test_delete_user(test_client):
    payload = {"name": "Ife", "email": "if@gmail.com"}
    create_res = test_client.post("/users/create", json=payload)
    user_id = create_res.json()["data"]["id"]
    response = test_client.delete(f"/users/delete/{user_id}")
    data = response.json()
    assert response.status_code == 200
    assert data["message"] == "User was deleted successfully"


    