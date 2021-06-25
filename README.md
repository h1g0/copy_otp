# copy_otp

A simple Python script that generates Time-based One-time Password and copy it to clipboard.

## Usage

1. Run
   ```sh
   pip install pyotp
   pip install keyring
   ```
   to get the libraries required.
2. Get your private key. (Please google how to get your private key!)
3. Run
   ```sh
   python main.py
   ```
   in a shell (or execute `copy_otp.bat` if you are using Windows).
4. The first time you run the script, you will be asked to enter the secret key. Then input the key you got in step 2.
5. Time-based One-time Password will be copied to the clipboard.
