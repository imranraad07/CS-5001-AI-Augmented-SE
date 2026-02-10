import pytest
from datetime import datetime
from unittest.mock import patch
from src.app import validate_card_number, validate_expiry_date, validate_cvv

@pytest.mark.parametrize("card_number, expected", [
    ("4111 1111 1111 1111", True),  # Valid Visa
    ("5500 0000 0000 0004", True),  # Valid Mastercard
    ("3782 8224 6310 005", True),   # Valid Amex
    ("6011 1111 1111 1117", True),  # Valid Discover
    ("1234 5678 9012 3456", False), # Invalid
    ("123", False),                  # Too short
    ("1234567890123456789012345678901", False), # Too long
    ("abc123", False),               # Non-digit
    ("4111 1111 1111 1112", False),  # Invalid Luhn
])
def test_validate_card_number(card_number, expected):
    assert validate_card_number(card_number) == expected

@pytest.mark.parametrize("expiry_date, expected", [
    ("12/25", True),    # Valid future date
    ("01/23", True),    # Valid current year
    ("12/22", False),   # Expired
    ("00/23", False),   # Invalid month
    ("13/23", False),   # Invalid month
    ("12/00", False),   # Invalid year
    ("12/100", False),  # Invalid year
    ("1223", False),    # Wrong format
    ("12-23", False),   # Wrong separator
    ("", False),        # Empty
])
def test_validate_expiry_date(expiry_date, expected):
    with patch('src.app.datetime') as mock_datetime:
        mock_datetime.now.return_value.year = 2023
        mock_datetime.now.return_value.month = 6
        assert validate_expiry_date(expiry_date) == expected

@pytest.mark.parametrize("cvv, expected", [
    ("123", True),      # Valid 3-digit
    ("1234", True),     # Valid 4-digit
    ("12", False),      # Too short
    ("12345", False),   # Too long
    ("abc", False),     # Non-digit
    ("", False),        # Empty
])
def test_validate_cvv(cvv, expected):
    assert validate_cvv(cvv) == expected

def test_main_form_submission():
    with patch('streamlit.text_input') as mock_text_input, \
         patch('streamlit.form_submit_button') as mock_submit, \
         patch('streamlit.error') as mock_error, \
         patch('streamlit.success') as mock_success, \
         patch('streamlit.write') as mock_write:

        # Setup mock inputs
        mock_text_input.side_effect = ["4111 1111 1111 1111", "12/25", "123", "John Doe", True]

        # Call main
        from src.app import main
        main()

        # Verify success case
        assert mock_success.called
        assert mock_error.call_count == 0

def test_main_form_validation_errors():
    with patch('streamlit.text_input') as mock_text_input, \
         patch('streamlit.form_submit_button') as mock_submit, \
         patch('streamlit.error') as mock_error, \
         patch('streamlit.success') as mock_success, \
         patch('streamlit.write') as mock_write:

        # Test empty fields
        mock_text_input.side_effect = ["", "", "", "", True]
        from src.app import main
        main()
        assert mock_error.call_count == 1
        assert "All fields are required!" in str(mock_error.call_args)

        # Test invalid card number
        mock_text_input.side_effect = ["1234 5678 9012 3456", "12/25", "123", "John Doe", True]
        main()
        assert mock_error.call_count == 2
        assert "Invalid card number!" in str(mock_error.call_args)

        # Test invalid expiry date
        mock_text_input.side_effect = ["4111 1111 1111 1111", "12/22", "123", "John Doe", True]
        main()
        assert mock_error.call_count == 3
        assert "Invalid expiry date!" in str(mock_error.call_args)

        # Test invalid CVV
        mock_text_input.side_effect = ["4111 1111 1111 1111", "12/25", "12", "John Doe", True]
        main()
        assert mock_error.call_count == 4
        assert "Invalid CVV!" in str(mock_error.call_args)
