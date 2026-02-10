import pytest
from flask import Flask
from src.flask import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Welcome to the minimal Flask project!"

def test_echo_route(client):
    test_data = {"key": "value", "number": 42}
    response = client.post('/echo', json=test_data)
    assert response.status_code == 200
    assert response.get_json() == test_data

def test_echo_route_empty_payload(client):
    response = client.post('/echo', json={})
    assert response.status_code == 200
    assert response.get_json() == {}

def test_echo_route_invalid_json(client):
    response = client.post('/echo', data='invalid json')
    assert response.status_code == 415

def test_health_route(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}

def test_echo_route_get_method(client):
    response = client.get('/echo')
    assert response.status_code == 405

def test_echo_route_non_json_payload(client):
    response = client.post('/echo', data='plain text')
    assert response.status_code == 415

def test_echo_route_mixed_types(client):
    test_data = {"string": "text", "number": 123, "boolean": True, "null": None, "array": [1, 2, 3]}
    response = client.post('/echo', json=test_data)
    assert response.status_code == 200
    assert response.get_json() == test_data

def test_echo_route_nested_json(client):
    test_data = {"nested": {"key": "value"}, "list": [{"item": 1}, {"item": 2}]}
    response = client.post('/echo', json=test_data)
    assert response.status_code == 200
    assert response.get_json() == test_data

def test_health_route_content_type(client):
    response = client.get('/health')
    assert response.content_type == 'application/json'

def test_index_route_content_type(client):
    response = client.get('/')
    assert response.content_type == 'text/html; charset=utf-8'

def test_echo_route_content_type(client):
    response = client.post('/echo', json={})
    assert response.content_type == 'application/json'
