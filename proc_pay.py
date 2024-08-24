from platform import processor
from index import credit_card, crypto, paypal_process, paypal_validate, process_crypto


def process_payment(payment_type, info, amount):
    if payment_type == "credit_card":
        if credit_card(info):
            processor(amount)
        else:
            print("Invalid credit card details")
    
    elif payment_type == "paypal":
        if paypal_validate(info):
            paypal_process(amount)
        else:
            print("Invalid PayPal details")
    
    elif payment_type == "crypto":
        if crypto(info):
            process_crypto(amount)
        else:
            print("Invalid cryptocurrency details")