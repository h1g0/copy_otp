from tabnanny import check
import pyotp
import keyring
import pyperclip
import re

SERVICE_ID = 'COPY_OTP'

def get_totp(secret: str) -> str:
    totp = pyotp.TOTP(secret)
    result = totp.now()
    return result


def get_skey() -> str:
    return keyring.get_password(SERVICE_ID,"totp")

def set_skey(key: str):
    keyring.set_password(SERVICE_ID,"totp",key)

def check_is_base32(key:str):
    return True if re.fullmatch('[A-Z2-7=]+',key) else False

if __name__ == '__main__':
    skey: str = get_skey()
    #skey = ''
    while not skey:
        skey = input("Please input the secret for TOTP: ").strip()
        if(check_is_base32(skey)):
            set_skey(skey)
        else:
            print('Invalid secret! Input again: ')
            skey = ''    

    result = get_totp(skey)
    pyperclip.copy(result)
    print(f'OTP {result} copied!')
