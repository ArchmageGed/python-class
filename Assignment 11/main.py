#import functions as f
#from functions import *
from functions import register_user, topup_balance, proccess_transaction, print_transaction_logs, print_users

def runner():
    register_user("Elene", "Buskivadze", "TB028", 0)
    topup_balance("TB028", 100)
    proccess_transaction("TB028", "TB001", 50)
    
    print_transaction_logs() 
    print_users()

if __name__ == "__main__":
    runner()