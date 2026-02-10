import streamlit as st
from datetime import datetime

def validate_card_number(card_number):
    """Validate credit card number using Luhn algorithm."""
    card_number = card_number.replace(" ", "")
    if not card_number.isdigit() or len(card_number) < 13 or len(card_number) > 19:
        return False
    digits = [int(d) for d in card_number]
    for i in range(len(digits)-2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    return sum(digits) % 10 == 0

def validate_expiry_date(expiry_date):
    """Validate credit card expiry date in MM/YY format."""
    try:
        month, year = map(int, expiry_date.split('/'))
        if month < 1 or month > 12 or year < 0 or year > 99:
            return False
        current_year = datetime.now().year % 100
        current_month = datetime.now().month
        if year < current_year or (year == current_year and month < current_month):
            return False
        return True
    except:
        return False

def validate_cvv(cvv):
    """Validate CVV code."""
    return cvv.isdigit() and len(cvv) in (3, 4)

def main():
    """Main function to render Streamlit app for credit card information."""
    st.title("Credit Card Information")
    st.write("Please enter your credit card details below:")

    with st.form("credit_card_form"):
        card_number = st.text_input("Card Number", placeholder="1234 5678 9012 3456")
        expiry_date = st.text_input("Expiry Date (MM/YY)", placeholder="12/25")
        cvv = st.text_input("CVV", placeholder="123", type="password")
        name = st.text_input("Cardholder Name", placeholder="John Doe")

        submitted = st.form_submit_button("Submit")

        if submitted:
            if not card_number or not expiry_date or not cvv or not name:
                st.error("All fields are required!")
            elif not validate_card_number(card_number):
                st.error("Invalid card number!")
            elif not validate_expiry_date(expiry_date):
                st.error("Invalid expiry date!")
            elif not validate_cvv(cvv):
                st.error("Invalid CVV!")
            else:
                st.success("Credit card information submitted successfully!")
                st.write(f"Card Number: {card_number}")
                st.write(f"Expiry Date: {expiry_date}")
                st.write(f"CVV: {'*' * len(cvv)}")
                st.write(f"Cardholder Name: {name}")

if __name__ == "__main__":
    main()
