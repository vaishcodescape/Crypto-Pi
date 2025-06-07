# Crypto-Pi

Crypto-Pi is a Python automation script that monitors the crypto market and sends notifications when cryptocurrency prices reach specified thresholds.

## Features

- Monitor multiple cryptocurrencies (BTC, ETH, BNB, SOL, XRP, ADA, DOGE, AVAX, DOT, MATIC)
- Set custom price change thresholds
- Receive email notifications
- Receive SMS notifications
- Real-time price monitoring
- Colorful terminal interface

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Crypto-Pi.git
cd Crypto-Pi
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up email notifications:
   - Go to your Google Account settings
   - Enable 2-Step Verification
   - Generate an App Password for "Mail"
   - Copy `config_secrets.py.template` to `config_secrets.py`
   - Fill in your email and App Password in `config_secrets.py`

4. Run the script:
```bash
python main/main.py
```

## Configuration

- Edit `config_secrets.py` to set up your email credentials
- The script will prompt you to:
  - Select a cryptocurrency to monitor
  - Set a price change threshold
  - Enter your email address
  - Enter your phone number

## Usage

1. Run the script
2. Select a cryptocurrency to monitor
3. Set your desired price change threshold
4. Enter your contact information
5. The script will monitor prices and send notifications when the threshold is reached

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Made by @vaishcodescape
Follow me on GitHub: https://github.com/vaishcodescape