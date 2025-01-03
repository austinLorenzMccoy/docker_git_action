from app import app

def test_base_route():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'