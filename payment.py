from convert import currency_convert
from discount import percentage_discount
from proc_pay import process_payment
from sign import log_transaction


payment_method = "credit_card"
info = {'card_num': '1234', 'exp_date': '12/25'}

amount = 100

discounted_amount = percentage_discount(amount, 10)

process_payment(payment_method, info, discounted_amount)

log_transaction(payment_method, discounted_amount, True)

converted_amount = currency_convert(discounted_amount, 'USD', 'EUR')
print(f"Converted amount: {converted_amount} EUR")
