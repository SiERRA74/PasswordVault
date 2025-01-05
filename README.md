# Password Vault

Password Vault is a secure and user-friendly password manager built with Python and Tkinter. It hashes your account password using bcrypt and uses the unhashed password as a Vigenere cipher key for encrypting and decrypting other passwords associated with the account.

## Features:

Secure Login: Account passwords are hashed using bcrypt.
Vigenere Encryption: Encrypts and decrypts stored passwords with a user-provided master password.
Responsive GUI: Built with Tkinter for an interactive and intuitive user experience.
Password Management: Add, view, and delete passwords associated with unique aliases.
Theming Options: Easily toggle between light and dark modes (future feature).

## Installation :

Clone this repository:
git clone https://github.com/SiERRA74/PWM.git

cd password-vault

(Optional : Create a virtual environment and activate it)

python -m venv venv

source venv/bin/activate # On Windows: venv\Scripts\activate

Install the required dependencies:
pip install bcrypt

## Usage

Run the application:
python start.py

### File Structure

start.py: Main entry point for the application.
accounts_handling.py: Handles user authentication (sign-up and log-in).
pwd_management.py: Manages encrypted password storage and retrieval.
vault.py: GUI components for displaying and managing passwords.
vignere.py: Implements Vigenere encryption and decryption.
wallpaper.py: Handles GUI theming (dark/light mode (in progress)).

### Notes

Ensure your Python installation includes Tkinter.
For Windows users, Tkinter is typically bundled with the Python installer.
For Linux users, you may need to install Tkinter manually:
