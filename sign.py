def log_transaction(method, amount, status):
    with open('transactions.log', 'a') as log_file:
        log_file.write(f"Method: {method}, Amount: {amount}, Status: {'Success' if status else 'Failed'}\n")
