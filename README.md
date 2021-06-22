# copy_otp

A simple Python script that generates Time-based One-time Password and copy it to clipboard.

## Usage

1. Get your private key. (Please google how to get your private key!)
2. Save it in the same directory as `main.py` with the name `secret.txt`.
3. Run
   ```sh
   python main.py
   ```
   in a shell (or execute `copy_otp.bat` if you are using Windows).
4. Time-based One-time Password will be copied to the clipboard.

## Attention

This script stores the private key in plain text, which may lead to reduced security.