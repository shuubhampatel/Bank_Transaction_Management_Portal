"""This tests are for auth pages test"""
from app import User


def test_register_page(client):
    """This makes the register test page"""
    response = client.get("/register")
    assert response.status_code == 200
    assert b"Register" in response.data


def test_register_user(application, client):
    """this test is for to check registration process"""
    with application.app_context():
        email = 'test@test.com'
        password = 'test1234'
        user = User.query.filter_by(email=email).first()
        assert user is None

        response = client.post("/register", data=dict(email=email, password=password, confirm=password),
                               follow_redirects=True)

        user = User.query.filter_by(email=email).first()
        assert user is not None
        assert response.status_code == 200


def test_login_page(client):
    """This makes the login test page"""
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Login Page" in response.data


def test_user_login(application, client):
    """this test is for to check login process"""
    with application.app_context():
        email = 'test@test.com'
        password = 'test1234'
        user = User.query.filter_by(email=email).first()
        assert user is None

        response = client.post("/register", data=dict(email=email, password=password, confirm=password),
                               follow_redirects=True)

        user = User.query.filter_by(email=email).first()
        assert user is not None
        assert response.status_code == 200

        response = client.post("/login", data=dict(email=email, password=password, confirm=password),
                               follow_redirects=True)

        user = User.query.filter_by(email=email).first()
        assert user is not None
        assert response.status_code == 200
