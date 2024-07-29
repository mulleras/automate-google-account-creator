# automate-google-account-creator
Python script for automated Google account creation using Selenium WebDriver. Customize account details in config.json. Requires Python 3.7+, Selenium, and a browser driver like ChromeDriver. For educational use only; use responsibly and comply with Google’s terms of service.
Google Account Creator

This repository contains a Python script that automates the creation of Google accounts. The script uses Selenium WebDriver to interact with the Google account creation page and input the necessary details. This tool is intended for educational purposes only.
Features

    Automated Google account creation.
    Customizable input details such as username, password, and recovery options.
    Uses Selenium WebDriver for browser automation.
    Configurable to use different web browsers (Chrome, Firefox, etc.).

Prerequisites

    Python 3.7+
    Selenium WebDriver
    ChromeDriver (or other browser driver)

Installation

    Clone this repository:

    sh

git clone https://github.com/mulleras/automate-google-account-creator.git
cd google-account-creator

Install the required Python packages:

sh

    pip install -r requirements.txt

    Download the appropriate WebDriver for your browser and ensure it is in your system's PATH. For example, for Chrome:
        Download ChromeDriver.
        Extract the downloaded file and move it to a directory included in your system's PATH.

Usage

    Open the config.json file and update it with the desired account details (e.g., username, password, recovery email, etc.).

    Run the script:

    sh

    python create_google_account.py

Configuration

The config.json file allows you to customize the following details:

    first_name: First name of the account owner.
    last_name: Last name of the account owner.
    username: Desired Google account username.
    password: Account password.
    recovery_email: Recovery email address.
    phone_number: Phone number for account verification.

Example config.json:

json

{
  "first_name": "John",
  "last_name": "Doe",
  "username": "john.doe123",
  "password": "SecurePassword123!",
  "recovery_email": "recovery@example.com",
  "phone_number": "+1234567890"
}

Disclaimer

This script is intended for educational purposes only. Automating account creation may violate Google's terms of service. Use this tool responsibly and at your own risk. The authors are not responsible for any misuse of this tool.
Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or new features to suggest.
