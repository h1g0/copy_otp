# copy_otp

A simple Python script that generates Time-based One-time Password and copy it to clipboard.

Reading the secret can be done both by reading the QR code or by entering a text string.

The secret will be stored in encryption.

## Usage

1. Run
   ```sh
   pip install pyotp
   pip install keyring
   pip install pyzbar
   ```
   to get the libraries required.
2. Get your QR code or secret for your 2FA. (Please google how to get your QR code or secret!)
3. If you got your QR code, save the QR code you got in the same directory with the name `qr.png`.
4. Run
   ```sh
   python main.py
   ```
   in a shell (or execute `copy_otp.bat` if you are using Windows).
5. The first time you run the script, if the image file of the QR code exists, the secret will be read from the QR code and the image file will be deleted. If not, you will be asked to enter the secret.
6. Time-based One-time Password will be copied to the clipboard.
