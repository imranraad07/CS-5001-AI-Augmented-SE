import json
from a2a_demo import coder_result, planner_message

def test_message_is_structured():
    request = planner_message()
    payload = json.loads(request.to_json())
    assert payload["sender"] == "planner"
    assert payload["recipient"] == "coder"

def test_result_routes_to_reviewer():
    assert coder_result(planner_message()).recipient == "reviewer"
