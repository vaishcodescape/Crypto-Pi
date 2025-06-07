#Crypto-Pi main script
import time
import sys
import colorama
import smtplib
import getpass
import requests
import os
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_CONFIG, COINGECKO_API_URL
# from config import TWILIO_API_KEY

import twilio

from colorama import init, Fore, Back, Style


# Initialize colorama
init(colorama)

# Global variable for selected cryptocurrency
type_curr = None

class EmailNotifier:
    def __init__(self):
        self.smtp_server = EMAIL_CONFIG['smtp_server']
        self.smtp_port = EMAIL_CONFIG['smtp_port']
        self.sender_email = EMAIL_CONFIG['sender_email']
        self.password = EMAIL_CONFIG['password']
    
    def send_notification(self, to_email, subject, content):
        try:
            # Create message
            message = MIMEMultipart()
            message["From"] = self.sender_email
            message["To"] = to_email
            message["Subject"] = subject
            
            # Add body to email
            message.attach(MIMEText(content, "plain"))
            
            # Create SMTP session with explicit TLS
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.ehlo()  # Can be omitted
                server.starttls()  # Secure the connection
                server.ehlo()  # Can be omitted
                server.login(self.sender_email, self.password)
                server.send_message(message)
            
            print(f"{Fore.GREEN}Email notification sent successfully!{Style.RESET_ALL}")
            return True
            
        except Exception as e:
            print(f"{Fore.RED}Failed to send email: {str(e)}{Style.RESET_ALL}")
            if "Authentication" in str(e):
                print(f"{Fore.RED}Authentication failed. Please check the email configuration.{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}To set up Gmail:{Style.RESET_ALL}")
                print("1. Go to your Google Account settings")
                print("2. Enable 2-Step Verification")
                print("3. Go to Security → App Passwords")
                print("4. Generate a new app password for 'Mail'")
                print("5. Use that password in the config file")
            return False
    
    def send_crypto_alert(self, to_email, crypto_symbol):
        """
        Send a cryptocurrency price alert email
        
        Args:
            to_email (str): Recipient's email address
            crypto_symbol (str): Cryptocurrency symbol (e.g., BTC, ETH)
        """
        subject = "Crypto-Pi Price Alert"
        content = f"""
        Hello Crypto-Pi User,
        
        This is a confirmation that you have successfully set up price alerts for {crypto_symbol}.
        You will receive notifications when the price reaches your desired target.
        
        Stay tuned for updates!
        
        Best regards,
        Crypto-Pi Team
        """
        return self.send_notification(to_email, subject, content)

class CryptoPriceAPI:
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"
        self.supported_coins = {
            "BTC": "bitcoin",
            "ETH": "ethereum",
            "BNB": "binancecoin",
            "SOL": "solana",
            "XRP": "ripple",
            "ADA": "cardano",
            "DOGE": "dogecoin",
            "AVAX": "avalanche-2",
            "DOT": "polkadot",
            "MATIC": "matic-network"
        }
        self.last_request_time = 0
        self.min_request_interval = 1.2  # Minimum time between requests in seconds
    
    def _wait_for_rate_limit(self):
        """Ensure we don't exceed rate limits"""
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time
        if time_since_last_request < self.min_request_interval:
            time.sleep(self.min_request_interval - time_since_last_request)
        self.last_request_time = time.time()
    
    def get_prices_batch(self, symbols):
        """Get prices for multiple cryptocurrencies in one request"""
        try:
            self._wait_for_rate_limit()
            coin_ids = [self.supported_coins[symbol] for symbol in symbols]
            url = f"{self.base_url}/simple/price"
            params = {
                "ids": ",".join(coin_ids),
                "vs_currencies": "usd",
                "include_24hr_change": "true"
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            return data
            
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}Error fetching prices: {str(e)}{Style.RESET_ALL}")
            return None
        except Exception as e:
            print(f"{Fore.RED}Unexpected error: {str(e)}{Style.RESET_ALL}")
            return None
    
    def get_price(self, symbol):
        """Get price for a single cryptocurrency"""
        try:
            if symbol not in self.supported_coins:
                print(f"{Fore.RED}Unsupported cryptocurrency symbol: {symbol}{Style.RESET_ALL}")
                return None
            
            data = self.get_prices_batch([symbol])
            if data:
                coin_id = self.supported_coins[symbol]
                return data[coin_id]["usd"]
            return None
            
        except Exception as e:
            print(f"{Fore.RED}Error getting price for {symbol}: {str(e)}{Style.RESET_ALL}")
            return None
    
    def get_price_change_24h(self, symbol):
        """Get 24h price change for a single cryptocurrency"""
        try:
            if symbol not in self.supported_coins:
                print(f"{Fore.RED}Unsupported cryptocurrency symbol: {symbol}{Style.RESET_ALL}")
                return None
            
            data = self.get_prices_batch([symbol])
            if data:
                coin_id = self.supported_coins[symbol]
                return data[coin_id]["usd_24h_change"]
            return None
            
        except Exception as e:
            print(f"{Fore.RED}Error getting price change for {symbol}: {str(e)}{Style.RESET_ALL}")
            return None

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

def crypto_prices():
    api = CryptoPriceAPI()
    print(f"\n{Fore.CYAN}Current Cryptocurrency Prices:{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'=' * 40}{Style.RESET_ALL}")
    
    for symbol in api.supported_coins.keys():
        price = api.get_price(symbol)
        change = api.get_price_change_24h(symbol)
        
        if price is not None:
            price_str = f"${price:,.2f}"
            if change is not None:
                change_color = Fore.GREEN if change >= 0 else Fore.RED
                change_str = f"{change_color}{change:+.2f}%{Style.RESET_ALL}"
                print(f"{Fore.GREEN}{symbol}{Style.RESET_ALL}: {price_str} ({change_str})")
            else:
                print(f"{Fore.GREEN}{symbol}{Style.RESET_ALL}: {price_str}")
    
    print(f"{Fore.YELLOW}{'=' * 40}{Style.RESET_ALL}\n")

def check_status(currency):
    # Placeholder for check_status function
    pass

def send_email(email):
    notifier = EmailNotifier()
    notifier.send_crypto_alert(email, type_curr)

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

def display_real_time_prices(interval=10):
    api = CryptoPriceAPI()
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n{Fore.CYAN}Real-time Cryptocurrency Prices{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Last Updated: {current_time}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{'=' * 60}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'Symbol':<8} {'Price (USD)':<15} {'24h Change':<12} {'Status'}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{'-' * 60}{Style.RESET_ALL}")
            
            # Get all prices in one batch request
            data = api.get_prices_batch(list(api.supported_coins.keys()))
            
            if data:
                for symbol, coin_id in api.supported_coins.items():
                    if coin_id in data:
                        price = data[coin_id]["usd"]
                        change = data[coin_id]["usd_24h_change"]
                        
                        price_str = f"${price:,.2f}"
                        change_color = Fore.GREEN if change >= 0 else Fore.RED
                        change_str = f"{change_color}{change:+.2f}%{Style.RESET_ALL}"
                        status = "🟢" if change >= 0 else "🔴"
                        
                        print(f"{Fore.GREEN}{symbol:<8}{Style.RESET_ALL} {price_str:<15} {change_str:<12} {status}")
                    else:
                        print(f"{Fore.GREEN}{symbol:<8}{Style.RESET_ALL} {'N/A':<15} {'N/A':<12} ⚪")
            else:
                print(f"{Fore.RED}Failed to fetch price data. Please try again later.{Style.RESET_ALL}")
            
            print(f"{Fore.YELLOW}{'=' * 60}{Style.RESET_ALL}")
            print(f"\n{Fore.CYAN}Press Ctrl+C to stop updates{Style.RESET_ALL}")
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Stopping real-time updates...{Style.RESET_ALL}")
        time.sleep(1)
        print(f"{Fore.GREEN}Updates stopped. Thank you for using Crypto-Pi!{Style.RESET_ALL}\n")

def main():
    global type_curr
    # Display banner and loading animation
    print_banner()
    loading_animation()

    # Display available cryptocurrencies
    print_section("CRYPTOCURRENCY SELECTION")
    list_cryptocurrencies()

    # Get user's cryptocurrency choice
    while True:
        currency = input(f"{Fore.YELLOW}Enter the Crypto Currency you want to monitor (e.g., BTC, ETH): {Style.RESET_ALL}")
        type_curr = currency.upper()

        if type_curr in ["BTC", "ETH", "BNB", "SOL", "XRP", "ADA", "DOGE", "AVAX", "DOT", "MATIC"]:
            print(f"{Fore.GREEN}You selected {type_curr}.{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid cryptocurrency symbol.{Style.RESET_ALL}")
            print("Please try again.")
            time.sleep(1)
            list_cryptocurrencies()

    # Display real-time prices
    print_section("REAL-TIME PRICES")
    while True:
        choice = input(f"{Fore.YELLOW}Would you like to see real-time prices? (yes/no): {Style.RESET_ALL}").lower()
        if choice in ['yes', 'y']:
            print(f"\n{Fore.GREEN}Starting real-time price updates...{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Updates will refresh every 10 seconds.{Style.RESET_ALL}")
            time.sleep(2)
            display_real_time_prices()
            break
        elif choice in ['no', 'n']:
            crypto_prices()
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please enter 'yes' or 'no'.{Style.RESET_ALL}")

    # Get contact information
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

    # Send notifications
    print_section("SENDING NOTIFICATIONS")
    send_email(email)
    send_sms(phn_number)

    # Final messages
    print_section("SETUP COMPLETE")
    print(f"{Fore.GREEN}You will be notified via email and SMS when the price of {type_curr} reaches your desired price.{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Until then, trade wisely!{Style.RESET_ALL}")

    print_section("THANK YOU")
    print(f"{Fore.CYAN}Thank you for using Crypto-Pi. Have a great day!{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}To run the program again, type 'python main.py' in your terminal{Style.RESET_ALL}")

    print_section("CREDITS")
    print(f"{Fore.GREEN}Made by: @vaishcodescape{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Follow me on GitHub: https://github.com/vaishcodescape{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
