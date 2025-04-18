# Dorm Room Availability Notifier from MSE Application Portal

This Python script uses Selenium to monitor the MSE HDA portal and sends an email alert when a third payment option appears in the "Payment" section of the dashboard. The logic here is, whenever the third payment option is available under the "Payment" section of the Application Portal (Kopla), it would suggest that applications for the dorm rooms is open.

## Features
- Uses Selenium to control a Chrome browser
- Manually login once, then checks periodically
- Refreshes the page every 30 seconds (this is customizable)
- Sends email notification when the third payment row appears

## Prerequisites
- Python 3.7+
- Chrome browser installed
- ChromeDriver installed and added to PATH

## Installation

1. **Clone this repository**:
```bash
https://github.com/nachiketathakur/h_da-Dorm-Availability-Checker
cd mse-payment-checker
```

2. **Create a virtual environment (optional but recommended)**:
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install the required packages**:
```bash
pip install selenium yagmail
```

4. **Set up Gmail App Password**:
   - Enable 2-Step Verification on your Gmail account
   - Go to [App Passwords](https://myaccount.google.com/apppasswords)
   - Generate a 16-digit app password for "Mail"
   - Replace the placeholder in the script with your app password

## Usage

1. Run the script:
```bash
python Dorm-Available-Alert-Script.py
```

2. A Chrome window will open. Log in to your MSE dashboard manually.

3. Once logged in, press Enter in the terminal to start the periodic checker.

4. The page will refresh every 30 seconds. You will receive an email alert when the third payment option appears.

## Configuration
- Change the recipient email by editing the `EMAIL_TO_NOTIFY` value in the script.
- Adjust the checking interval using the `CHECK_INTERVAL` variable.

## Notes
- The script waits for manual login for security reasons.
- If you want to run this on a server without GUI, consider using headless mode for Chrome.

## License
MIT License

