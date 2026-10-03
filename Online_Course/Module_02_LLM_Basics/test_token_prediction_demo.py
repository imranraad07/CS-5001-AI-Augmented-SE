from token_prediction_demo import predict_next

def test_language_context_prefers_lamb():
    assert predict_next("Mary had a little")[0].token == "lamb"

def test_context_changes_code_prediction():
    assert predict_next("for i in range(")[0].token != predict_next("items = ['a', 'b', 'c']\nfor i in range(")[0].token
