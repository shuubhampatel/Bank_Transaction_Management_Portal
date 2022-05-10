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
        response = client.post("/login", data=dict(email=email, password=password, confirm=password),
                               follow_redirects=True)
        user = User.query.filter_by(email=email).first()
        assert user is not None
        assert response.status_code == 200


def test_dashboard_page(client, application):
    """This makes the dashboard page"""
    with application.app_context():
        email = 'test@test.com'
        password = 'test1234'
        response = client.post("/register", data=dict(email=email, password=password, confirm=password),
                               follow_redirects=True)
        response = client.post("/login", data=dict(email=email, password=password, confirm=password),
                               follow_redirects=True)
        response = client.get("/dashboard")
        assert response.status_code == 200
        assert b'Welcome: test@test.com' in response.data


def test_dashboard_buttons(client, application):
    """This makes the dashboard buttons test"""
    with application.app_context():
        email = 'test@test.com'
        password = 'test1234'
        response = client.post("/register", data=dict(email=email, password=password, confirm=password),
                               follow_redirects=True)
        response = client.post("/login", data=dict(email=email, password=password, confirm=password),
                               follow_redirects=True)
        response = client.get("/dashboard")
        assert b'<button class="dt-button buttons-copy buttons-html5" tabindex="0" aria-controls="DataTables_Table_0" type="button"><span>Copy</span></button>'
        assert b'<button class="dt-button buttons-csv buttons-html5" tabindex="0" aria-controls="DataTables_Table_0" type="button"><span>CSV</span></button>'
        assert b'<button class="dt-button buttons-excel buttons-html5" tabindex="0" aria-controls="DataTables_Table_0" type="button"><span>Excel</span></button>'
        assert b'<button class="dt-button buttons-pdf buttons-html5" tabindex="0" aria-controls="DataTables_Table_0" type="button"><span>PDF</span></button>'
        assert b'<button class="dt-button buttons-print" tabindex="0" aria-controls="DataTables_Table_0" type="button"><span>Print</span></button>'
        assert response.status_code is not 400
        assert response.status_code is 200

