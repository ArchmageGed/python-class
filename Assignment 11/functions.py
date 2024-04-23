import library as l

def register_user(name, lastname, iban, balance):
    l.users.append({"name": name, "lastName": lastname, "iban": iban, "balance": balance})

def topup_balance(iban, balance):
    for user in l.users:
        if user.get("iban") == iban:
            user["balance"] += balance

def proccess_transaction(sender, receiver, amount):
    sender_user = find_user_with_iban(sender)
    receiver_user = find_user_with_iban(receiver)
    if sender_user and receiver_user:
        if sender_user.get("balance") >= amount:
            print("Proccessing transaction ...")
            sender_user['balance'] -= amount
            receiver_user['balance'] += amount
            l.transactions.append({"sender_iban": sender, "reciver_iban": receiver, "amount": amount})
    else:
        print("Does not exist")

def find_user_with_iban(iban):
    for user in l.users:
        if user.get("iban") == iban:
            return user
    return None

def print_transaction_logs():
    for transaction in l.transactions:
        sender_user = find_user_with_iban(transaction.get("sender_iban"))
        reciver_user = find_user_with_iban(transaction.get("reciver_iban"))
        print(sender_user.get("name"), " - >", reciver_user.get("name"), transaction.get("amount"))

def print_users():
    for user in l.users:
        print(user.get("name"), user.get("lastName"), user.get("iban"), user.get("balance"))