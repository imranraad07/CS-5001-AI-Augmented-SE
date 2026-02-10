import pytest
from src.app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_app_creation(app):
    assert app is not None
    assert app.name == 'src.app'

def test_blueprint_registered(app):
    assert 'main' in app.blueprints

def test_app_context(app):
    with app.app_context():
        assert True

def test_client_get(client):
    response = client.get('/')
    assert response.status_code == 200

def test_client_post(client):
    response = client.post('/')
    assert response.status_code == 200

def test_client_put(client):
    response = client.put('/')
    assert response.status_code == 200

def test_client_delete(client):
    response = client.delete('/')
    assert response.status_code == 200

def test_app_run(app, mocker):
    mocker.patch('src.app.app.run')
    app.run(debug=True)
    app.run.assert_called_once_with(debug=True)
