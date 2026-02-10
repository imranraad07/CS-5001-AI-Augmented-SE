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
    assert response.status_code == 400

def test_health_route(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}

def test_echo_route_get_method(client):
    response = client.get('/echo')
    assert response.status_code == 405

def test_echo_route_non_json_payload(client):
    response = client.post('/echo', data='plain text')
    assert response.status_code == 400

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

def test_echo_route_large_payload(client):
    large_data = {"data": [i for i in range(1000)]}
    response = client.post('/echo', json=large_data)
    assert response.status_code == 200
    assert response.get_json() == large_data

def test_echo_route_unicode_data(client):
    unicode_data = {"text": "Hello 世界 🌍"}
    response = client.post('/echo', json=unicode_data)
    assert response.status_code == 200
    assert response.get_json() == unicode_data

def test_echo_route_special_characters(client):
    special_data = {"text": "!@#$%^&*()"}
    response = client.post('/echo', json=special_data)
    assert response.status_code == 200
    assert response.get_json() == special_data

def test_echo_route_float_numbers(client):
    float_data = {"pi": 3.14159, "e": 2.71828}
    response = client.post('/echo', json=float_data)
    assert response.status_code == 200
    assert response.get_json() == float_data

def test_echo_route_negative_numbers(client):
    negative_data = {"temp": -40, "depth": -1000}
    response = client.post('/echo', json=negative_data)
    assert response.status_code == 200
    assert response.get_json() == negative_data

def test_echo_route_zero_values(client):
    zero_data = {"count": 0, "balance": 0.0}
    response = client.post('/echo', json=zero_data)
    assert response.status_code == 200
    assert response.get_json() == zero_data

def test_echo_route_empty_string(client):
    empty_string_data = {"message": ""}
    response = client.post('/echo', json=empty_string_data)
    assert response.status_code == 200
    assert response.get_json() == empty_string_data

def test_echo_route_boolean_false(client):
    false_data = {"flag": False}
    response = client.post('/echo', json=false_data)
    assert response.status_code == 200
    assert response.get_json() == false_data

def test_echo_route_empty_list(client):
    empty_list_data = {"items": []}
    response = client.post('/echo', json=empty_list_data)
    assert response.status_code == 200
    assert response.get_json() == empty_list_data

def test_echo_route_empty_dict(client):
    empty_dict_data = {"nested": {}}
    response = client.post('/echo', json=empty_dict_data)
    assert response.status_code == 200
    assert response.get_json() == empty_dict_data

def test_echo_route_deeply_nested(client):
    deeply_nested = {"level1": {"level2": {"level3": {"level4": "deep"}}}}
    response = client.post('/echo', json=deeply_nested)
    assert response.status_code == 200
    assert response.get_json() == deeply_nested

def test_echo_route_mixed_nested(client):
    mixed_nested = {
        "array": [1, {"nested": True}, [2, 3]],
        "object": {"a": 1, "b": {"c": 2}}
    }
    response = client.post('/echo', json=mixed_nested)
    assert response.status_code == 200
    assert response.get_json() == mixed_nested

def test_echo_route_put_method(client):
    response = client.put('/echo', json={})
    assert response.status_code == 405

def test_echo_route_delete_method(client):
    response = client.delete('/echo')
    assert response.status_code == 405

def test_echo_route_patch_method(client):
    response = client.patch('/echo', json={})
    assert response.status_code == 405

def test_health_route_get_only(client):
    response = client.post('/health')
    assert response.status_code == 405

def test_index_route_get_only(client):
    response = client.post('/')
    assert response.status_code == 405

def test_echo_route_no_content_type(client):
    response = client.post('/echo')
    assert response.status_code == 400

def test_echo_route_malformed_json(client):
    response = client.post('/echo', data='{"incomplete":')
    assert response.status_code == 400

def test_echo_route_extra_commas_json(client):
    response = client.post('/echo', data='{"key": "value",}')
    assert response.status_code == 400

def test_echo_route_trailing_comma_json(client):
    response = client.post('/echo', data='{"key": "value", "key2": "value2",}')
    assert response.status_code == 400

def test_echo_route_duplicate_keys_json(client):
    response = client.post('/echo', data='{"key": "value1", "key": "value2"}')
    assert response.status_code == 400

def test_echo_route_unquoted_keys_json(client):
    response = client.post('/echo', data='{key: "value"}')
    assert response.status_code == 400

def test_echo_route_single_quotes_json(client):
    response = client.post('/echo', data="{'key': 'value'}")
    assert response.status_code == 400

def test_echo_route_mixed_quotes_json(client):
    response = client.post('/echo', data='{"key": \'value\'}')
    assert response.status_code == 400

def test_echo_route_escaped_chars_json(client):
    response = client.post('/echo', data='{"key": "value\\nwith\\nescapes"}')
    assert response.status_code == 200
    assert response.get_json() == {"key": "value\nwith\nescapes"}

def test_echo_route_unicode_escape_json(client):
    response = client.post('/echo', data='{"key": "\\u0041"}')
    assert response.status_code == 200
    assert response.get_json() == {"key": "A"}

def test_echo_route_large_number_json(client):
    response = client.post('/echo', data='{"big": 12345678901234567890}')
    assert response.status_code == 200
    assert response.get_json() == {"big": 12345678901234567890}

def test_echo_route_scientific_notation_json(client):
    response = client.post('/echo', data='{"sci": 1.23e-4}')
    assert response.status_code == 200
    assert response.get_json() == {"sci": 0.000123}

def test_echo_route_infinity_json(client):
    response = client.post('/echo', data='{"inf": Infinity}')
    assert response.status_code == 400

def test_echo_route_nan_json(client):
    response = client.post('/echo', data='{"nan": NaN}')
    assert response.status_code == 400

def test_echo_route_null_value_json(client):
    response = client.post('/echo', data='{"null": null}')
    assert response.status_code == 200
    assert response.get_json() == {"null": None}

def test_echo_route_multiple_nulls_json(client):
    response = client.post('/echo', data='{"a": null, "b": null, "c": null}')
    assert response.status_code == 200
    assert response.get_json() == {"a": None, "b": None, "c": None}

def test_echo_route_true_false_json(client):
    response = client.post('/echo', data='{"bool1": true, "bool2": false}')
    assert response.status_code == 200
    assert response.get_json() == {"bool1": True, "bool2": False}

def test_echo_route_empty_array_json(client):
    response = client.post('/echo', data='{"arr": []}')
    assert response.status_code == 200
    assert response.get_json() == {"arr": []}

def test_echo_route_array_with_null_json(client):
    response = client.post('/echo', data='{"arr": [null, 1, "text"]}')
    assert response.status_code == 200
    assert response.get_json() == {"arr": [None, 1, "text"]}

def test_echo_route_array_with_objects_json(client):
    response = client.post('/echo', data='{"arr": [{"a": 1}, {"b": 2}]}')
    assert response.status_code == 200
    assert response.get_json() == {"arr": [{"a": 1}, {"b": 2}]}

def test_echo_route_array_with_arrays_json(client):
    response = client.post('/echo', data='{"arr": [[1, 2], [3, 4]]}')
    assert response.status_code == 200
    assert response.get_json() == {"arr": [[1, 2], [3, 4]]}

def test_echo_route_object_in_array_in_object_json(client):
    response = client.post('/echo', data='{"outer": {"inner": [{"key": "value"}]}}')
    assert response.status_code == 200
    assert response.get_json() == {"outer": {"inner": [{"key": "value"}]}}

def test_app_run_with_port_env(client):
    import os
    os.environ['PORT'] = '8080'
    from src.flask import app as test_app
    assert test_app.run.__defaults__[1] == 8080

def test_app_run_default_port(client):
    import os
    if 'PORT' in os.environ:
        del os.environ['PORT']
    from src.flask import app as test_app
    assert test_app.run.__defaults__[1] == 5000

def test_app_run_host(client):
    from src.flask import app as test_app
    assert test_app.run.__defaults__[0] == '0.0.0.0'

def test_app_instance(client):
    from src.flask import app as test_app
    assert isinstance(test_app, Flask)
    assert test_app.name == 'src.flask'

def test_app_routes(client):
    from src.flask import app as test_app
    assert len(test_app.url_map._rules) == 3
    assert any(rule.rule == '/' for rule in test_app.url_map._rules)
    assert any(rule.rule == '/echo' for rule in test_app.url_map._rules)
    assert any(rule.rule == '/health' for rule in test_app.url_map._rules)

def test_app_echo_methods(client):
    from src.flask import app as test_app
    echo_rule = next(rule for rule in test_app.url_map._rules if rule.rule == '/echo')
    assert 'POST' in echo_rule.methods

def test_app_health_methods(client):
    from src.flask import app as test_app
    health_rule = next(rule for rule in test_app.url_map._rules if rule.rule == '/health')
    assert 'GET' in health_rule.methods

def test_app_index_methods(client):
    from src.flask import app as test_app
    index_rule = next(rule for rule in test_app.url_map._rules if rule.rule == '/')
    assert 'GET' in index_rule.methods

def test_app_echo_endpoint_name(client):
    from src.flask import app as test_app
    echo_rule = next(rule for rule in test_app.url_map._rules if rule.rule == '/echo')
    assert echo_rule.endpoint == 'echo'

def test_app_health_endpoint_name(client):
    from src.flask import app as test_app
    health_rule = next(rule for rule in test_app.url_map._rules if rule.rule == '/health')
    assert health_rule.endpoint == 'health'

def test_app_index_endpoint_name(client):
    from src.flask import app as test_app
    index_rule = next(rule for rule in test_app.url_map._rules if rule.rule == '/')
    assert index_rule.endpoint == 'index'

def test_app_echo_view_func(client):
    from src.flask import app as test_app
    echo_view = test_app.view_functions['echo']
    assert echo_view.__name__ == 'echo'

def test_app_health_view_func(client):
    from src.flask import app as test_app
    health_view = test_app.view_functions['health']
    assert health_view.__name__ == 'health'

def test_app_index_view_func(client):
    from src.flask import app as test_app
    index_view = test_app.view_functions['index']
    assert index_view.__name__ == 'index'

def test_app_echo_docstring(client):
    from src.flask import app as test_app
    echo_view = test_app.view_functions['echo']
    assert 'Endpoint that echoes back the JSON payload' in echo_view.__doc__

def test_app_health_docstring(client):
    from src.flask import app as test_app
    health_view = test_app.view_functions['health']
    assert 'Health check endpoint' in health_view.__doc__

def test_app_index_docstring(client):
    from src.flask import app as test_app
    index_view = test_app.view_functions['index']
    assert 'Root endpoint' in index_view.__doc__
