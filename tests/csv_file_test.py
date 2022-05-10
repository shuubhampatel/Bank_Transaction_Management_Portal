""" this tests are for upload directory check and csv upload check"""


def test_csv_upload(client, application):
    """ checks csv upload"""
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
        assert b"2000" in response.data
        assert b"CREDIT" in response.data
        assert b"-100" in response.data
        assert b"DEBIT" in response.data
