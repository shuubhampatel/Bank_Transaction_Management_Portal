"""This tests are for auth pages test"""


def test_register_page(client):
    """This makes the ci/cd page"""
    response = client.get("/register")
    assert response.status_code == 200
    assert b"Register" in response.data


def test_login_page(client):
    """This makes the ci/cd page"""
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Login Page" in response.data
