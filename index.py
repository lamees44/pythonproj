
def credit_card(info):
    return 'card_num' in info and 'exp_date' in info

def process_creditcard(amount):
    print(f"credit card: {amount}")

def paypal_validate(info):
    return 'email' in info

def paypal_process(amount):
    print(f" paypalprocess: {amount}")

def crypto(info):
    return 'wallet address' in info

def process_crypto(amount):
    print(f"Crypto: {amount}")
