"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="dropdown-item" href="/git">Git</a>' in response.data
    assert b'<a class="dropdown-item" href="/docker">Docker</a>' in response.data
    assert b'<a class="dropdown-item" href="flask">Python/ Flask</a>' in response.data
    assert b'<a class="dropdown-item" href="cicd">CI/ CD</a>' in response.data
    assert b'<a class="dropdown-item" href="/pylint">Pylint' in response.data
    assert b'<a class="dropdown-item" href="/aaa">AAA Testing</a>' in response.data
    assert b'<a class="dropdown-item" href="/oops">OOPs</a>' in response.data
    assert b'<a class="dropdown-item" href="/solid">SOLID</a>' in response.data


def test_request_home(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"IS601 Project4" in response.data


def test_pylint_page(client):
    """This makes the pylint page"""
    response = client.get("/pylint")
    assert response.status_code == 200
    assert b"Lets read about Pylint" in response.data


def test_aaa_page(client):
    """This makes the AAA page"""
    response = client.get("/aaa")
    assert response.status_code == 200
    assert b"Lets read about AAA testing" in response.data


def test_oops_page(client):
    """This makes the OOPs page"""
    response = client.get("/oops")
    assert response.status_code == 200
    assert b"Lets read about OOPs concepts" in response.data


def test_solid_page(client):
    """This makes the SOLID page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b"Lets read about SOLID" in response.data


def test_git_page(client):
    """This makes the git page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Lets read about Git" in response.data


def test_docker_page(client):
    """This makes the docker page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Lets read about Docker" in response.data


def test_flask_page(client):
    """This makes the flask page"""
    response = client.get("/flask")
    assert response.status_code == 200
    assert b"Lets read about Python/ Flask" in response.data


def test_cicd_page(client):
    """This makes the ci/cd page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"Lets read about CI/CD" in response.data


def test_about_page(client):
    """This makes the ci/cd page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"Introduction about My Self" in response.data
