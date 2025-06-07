#Crypto-Pi main script
import time
import sys

#List of top-10 Cryptocurrenicies in the Crypto Market
def list_cryptocurrencies():
    
    cryptocurrencies = [
    {"symbol": "BTC", "name": "Bitcoin"},
    {"symbol": "ETH", "name": "Ethereum"},
    {"symbol": "BNB", "name": "Binance Coin"},
    {"symbol": "SOL", "name": "Solana"},
    {"symbol": "XRP", "name": "XRP (Ripple)"},
    {"symbol": "ADA", "name": "Cardano"},
    {"symbol": "DOGE", "name": "Dogecoin"},
    {"symbol": "AVAX", "name": "Avalanche"},
    {"symbol": "DOT", "name": "Polkadot"},
    {"symbol": "MATIC", "name": "Polygon"}
]
    for coin in cryptocurrencies:
        print(f"{coin['symbol']}:{coin['name']}")
        
def loading_animation():
    for i in range(3):
        sys.stdout.write("\rloading" + "." * (i + 1))
        sys.stdout.flush()
        time.sleep(0.5)
    print("\rloading...")

def check_status(currency):
    # Placeholder for check_status function
    pass

def send_email(email):
    # Placeholder for send_email function
    pass

def send_sms(phn_number):
    # Placeholder for send_sms function
    pass

print("""
  _______  _______           _______ _________ _______    _______ _________
 (  ____ \\(  ____ )|\\     /|(  ____ )\\__   __/(  ___  )  (  ____ )\\__   __/
 | (    \\/| (    )|( \\   / )| (    )|   ) (   | (   ) |  | (    )|   ) (   
 | |      | (____)| \\ (_) / | (____)|   | |   | |   | |  | (____)|   | |   
 | |      |     __)  \\   /  |  _____)   | |   | |   | |  |  _____)   | |   
 | |      | (\\ (      ) (   | (         | |   | |   | |  | (         | |   
 | (____/\\| ) \\ \\__   | |   | )         | |   | (___) |  | )      ___) (___
 (_______/|/   \\__/   \\_/   |/          )_(   (_______)  |/       \\_______/
""")


loading_animation()

print("Here's a list of top cryptocurrencies:")

list_cryptocurrencies()  
time.sleep(2)  

while True:
    currency = input("Enter the Crypto Currency Status you would like to notify yourself e.g BTC,ETH:")
    type_curr = currency

    if type_curr == "BTC":
        print("You selected Bitcoin.")
        break
    elif type_curr == "ETH":
        print("You selected Ethereum.")
        break
    elif type_curr == "BNB":
        print("You selected Binance Coin.")
        break
    elif type_curr == "SOL":
        print("You selected Solana.")
        break
    elif type_curr == "XRP":
        print("You selected XRP (Ripple).")
        break
    elif type_curr == "ADA":
        print("You selected Cardano.")
        break
    elif type_curr == "DOGE":
        print("You selected Dogecoin.")
        break
    elif type_curr == "AVAX":
        print("You selected Avalanche.")
        break
    elif type_curr == "DOT":
        print("You selected Polkadot.")
        break
    elif type_curr == "MATIC":
        print("You selected Polygon.")
        break
    else:
        print("Invalid cryptocurrency symbol.")
        print("Please try again.")
        time.sleep(2)
        print("Here's a list of top cryptocurrencies:")
        list_cryptocurrencies()
        time.sleep(2)

check_status(type_curr)

while True:
    email = input("Enter your email address:")
    if '@' in email and '.' in email:
        break
    else:
        print("Invalid email address. Please try again.")

while True:
    try:
        phn_number = int(input("Enter your phone number with COUNTRY CODE!:"))
        break
    except ValueError:
        print("Invalid phone number. Please enter a valid number.")

send_email(email)
send_sms(phn_number)

loading_animation()

print("You shall be notified via email and SMS when the price of the selected cryptocurrency reaches your desired price till then trade wisely.")
print("--------------------------------")
print("Thank you for using Crypto-Pi. Have a great day!")
print("To run the program again, type 'python main.py in your terminal'")

print("Made by:@vaishcodescape follow me on github https://github.com/vaishcodescape")
print("--------------------------------")