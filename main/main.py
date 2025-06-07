#Crypto-Pi main script
import time
import sys
import colorama
from colorama import init, Fore, Back, Style

# Initialize colorama
init()

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
    print(f"\n{Fore.CYAN}Available Cryptocurrencies:{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'=' * 40}{Style.RESET_ALL}")
    for coin in cryptocurrencies:
        print(f"{Fore.GREEN}• {coin['symbol']}{Style.RESET_ALL}: {Fore.WHITE}{coin['name']}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'=' * 40}{Style.RESET_ALL}\n")

def check_status(currency):
    # Placeholder for check_status function
    pass

def send_email(email):
    # Placeholder for send_email function
    pass

def send_sms(phn_number):
    # Placeholder for send_sms function
    pass

def print_banner():
    # Each line should be 70 characters wide (including borders)
    banner_lines = [
        f"{Fore.CYAN}╔{'═'*68}╗{Style.RESET_ALL}",
        f"{Fore.CYAN}║{' '*68}║{Style.RESET_ALL}",
        f"{Fore.CYAN}║{Fore.YELLOW}   ******                            **                  *******  ** {Fore.CYAN}║{Style.RESET_ALL}",
        f"{Fore.CYAN}║{Fore.YELLOW}  **////**         **   ** ******   /**                 /**////**/** {Fore.CYAN}║{Style.RESET_ALL}",
        f"{Fore.CYAN}║{Fore.YELLOW} **    //  ****** //** ** /**///** ******  ******       /**   /**/** {Fore.CYAN}║{Style.RESET_ALL}",
        f"{Fore.CYAN}║{Fore.YELLOW}/**       //**//*  //***  /**  /**///**/  **////** *****/******* /** {Fore.CYAN}║{Style.RESET_ALL}",
        f"{Fore.CYAN}║{Fore.YELLOW}/**        /** /    /**   /******   /**  /**   /**///// /**////  /** {Fore.CYAN}║{Style.RESET_ALL}",
        f"{Fore.CYAN}║{Fore.YELLOW}//**    ** /**      **    /**///    /**  /**   /**      /**      /** {Fore.CYAN}║{Style.RESET_ALL}",
        f"{Fore.CYAN}║{Fore.YELLOW} //****** /***     **     /**       //** //******       /**      /** {Fore.CYAN}║{Style.RESET_ALL}",
        f"{Fore.CYAN}║{Fore.YELLOW}  //////  ///     //      //         //   //////        //       //  {Fore.CYAN}║{Style.RESET_ALL}",
        f"{Fore.CYAN}║{' '*68}║{Style.RESET_ALL}",
        f"{Fore.CYAN}╚{'═'*68}╝{Style.RESET_ALL}"
    ]
    print("\n".join(banner_lines))

def loading_animation():
    print(f"\n{Fore.YELLOW}Initializing Crypto-Pi...{Style.RESET_ALL}")
    for i in range(3):
        sys.stdout.write(f"\r{Fore.GREEN}Loading{Style.RESET_ALL}" + "." * (i + 1))
        sys.stdout.flush()
        time.sleep(0.5)
    print(f"\r{Fore.GREEN}Loading complete!{Style.RESET_ALL}\n")

def print_section(title):
    print(f"\n{Fore.CYAN}{'=' * 60}")
    print(f"{title.center(60)}")
    print(f"{'=' * 60}{Style.RESET_ALL}\n")

# Main program flow
print_banner()
loading_animation()

print_section("CRYPTOCURRENCY SELECTION")
print("Here's a list of top cryptocurrencies:")
list_cryptocurrencies()

while True:
    currency = input(f"{Fore.YELLOW}Enter the Crypto Currency Status you would like to notify yourself (e.g., BTC, ETH): {Style.RESET_ALL}")
    type_curr = currency.upper()

    if type_curr == "BTC":
        print(f"{Fore.GREEN}You selected Bitcoin.{Style.RESET_ALL}")
        break
    elif type_curr == "ETH":
        print(f"{Fore.GREEN}You selected Ethereum.{Style.RESET_ALL}")
        break
    elif type_curr == "BNB":
        print(f"{Fore.GREEN}You selected Binance Coin.{Style.RESET_ALL}")
        break
    elif type_curr == "SOL":
        print(f"{Fore.GREEN}You selected Solana.{Style.RESET_ALL}")
        break
    elif type_curr == "XRP":
        print(f"{Fore.GREEN}You selected XRP (Ripple).{Style.RESET_ALL}")
        break
    elif type_curr == "ADA":
        print(f"{Fore.GREEN}You selected Cardano.{Style.RESET_ALL}")
        break
    elif type_curr == "DOGE":
        print(f"{Fore.GREEN}You selected Dogecoin.{Style.RESET_ALL}")
        break
    elif type_curr == "AVAX":
        print(f"{Fore.GREEN}You selected Avalanche.{Style.RESET_ALL}")
        break
    elif type_curr == "DOT":
        print(f"{Fore.GREEN}You selected Polkadot.{Style.RESET_ALL}")
        break
    elif type_curr == "MATIC":
        print(f"{Fore.GREEN}You selected Polygon.{Style.RESET_ALL}")
        break
    else:
        print(f"{Fore.RED}Invalid cryptocurrency symbol.{Style.RESET_ALL}")
        print("Please try again.")
        time.sleep(2)
        print("Here's a list of top cryptocurrencies:")
        list_cryptocurrencies()
        time.sleep(2)

check_status(type_curr)

print_section("CONTACT INFORMATION")
while True:
    email = input(f"{Fore.YELLOW}Enter your email address: {Style.RESET_ALL}")
    if '@' in email and '.' in email:
        print(f"{Fore.GREEN}Email address accepted!{Style.RESET_ALL}")
        break
    else:
        print(f"{Fore.RED}Invalid email address. Please try again.{Style.RESET_ALL}")

while True:
    try:
        phn_number = int(input(f"{Fore.YELLOW}Enter your phone number with COUNTRY CODE: {Style.RESET_ALL}"))
        print(f"{Fore.GREEN}Phone number accepted!{Style.RESET_ALL}")
        break
    except ValueError:
        print(f"{Fore.RED}Invalid phone number. Please enter a valid number.{Style.RESET_ALL}")

send_email(email)
send_sms(phn_number)

loading_animation()

print_section("SETUP COMPLETE")
print(f"{Fore.GREEN}You shall be notified via email and SMS when the price of {type_curr} reaches your desired price.{Style.RESET_ALL}")
print(f"{Fore.YELLOW}Until then, trade wisely!{Style.RESET_ALL}")

print_section("THANK YOU")
print(f"{Fore.CYAN}Thank you for using Crypto-Pi. Have a great day!{Style.RESET_ALL}")
print(f"{Fore.YELLOW}To run the program again, type 'python main.py' in your terminal{Style.RESET_ALL}")

print_section("CREDITS")
print(f"{Fore.GREEN}Made by: @vaishcodescape{Style.RESET_ALL}")
print(f"{Fore.BLUE}Follow me on GitHub: https://github.com/vaishcodescape{Style.RESET_ALL}")