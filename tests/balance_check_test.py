""" test for balance check before and after uploading csv file"""


def test_balance_before(client, application):
    """ checks balance before upload"""
    with application.app_context():
        email = 'test@test.com'
        password = 'test1234'
        csv_test_file = 'tests/csvtest.csv'
        response = client.post("/register", data=dict(email=email, password=password, confirm=password),
                               follow_redirects=True)
        response = client.post("/login", data=dict(email=email, password=password, confirm=password),
                               follow_redirects=True)
        response = client.get("/transactions")
        assert b'Current Balance: $0' in response.data


def test_balance_after(client, application):
    """ checks balance after upload"""
    with application.app_context():
        email = 'test@test.com'
        password = 'test1234'
        csv_test_file = 'tests/csvtest.csv'
        response = client.post("/register", data=dict(email=email, password=password, confirm=password),
                               follow_redirects=True)
        response = client.post("/login", data=dict(email=email, password=password, confirm=password),
                               follow_redirects=True)
        response = client.post("/transactions/upload", data=dict(file=open(csv_test_file, 'rb')), follow_redirects=True)
        assert response.status_code == 200
        response = client.get("/transactions")
        assert b'Current Balance: $1900' in response.data
