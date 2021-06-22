# copy_otp

A simple Python script that generates Time-based One-time Password and copy it to clipboard.

## Usage

1. Run
   ```sh
   pip install pyotp
   ```
   to get the libraries required.
2. Get your private key. (Please google how to get your private key!)
3. Save it in the same directory as `main.py` with the name `secret.txt`.
4. Run
   ```sh
   python main.py
   ```
   in a shell (or execute `copy_otp.bat` if you are using Windows).
5. Time-based One-time Password will be copied to the clipboard.

## Attention

This script stores the private key in plain text, which may lead to reduced security.