import pyotp
import keyring
from pyzbar.pyzbar import decode
from PIL import Image
import pyperclip
import re
import os

SERVICE_ID = 'COPY_OTP'


def get_totp(secret: str) -> str:
    totp = pyotp.TOTP(secret)
    result = totp.now()
    return result


def get_skey() -> str:
    return keyring.get_password(SERVICE_ID, "totp")


def set_skey(key: str):
    keyring.set_password(SERVICE_ID, "totp", key)


def input_skey(repeat_until_valid: bool = True) -> str:
    result = ''
    while not result:
        result = input("Please input the secret for TOTP: ").strip()
        if(check_is_base32(result)):
            return result
        else:
            print('Invalid secret! Input again: ')
            if(repeat_until_valid):
                result = ''
            else:
                return result


def parse_otpauth_uri(uri: str) -> dict:
    # otpauth uri:
    # ```
    # otpauth://totp/[issuer]:[accountname]?secret=[secret]&issuer=[issuer]&algorithm=SHA1&digits=6&period=30
    # ```
    # cf. https://github.com/google/google-authenticator/wiki/Key-Uri-Format
    result = {
        'valid': False,
        'secret': '',
    }
    if 'otpauth://totp/' in uri:
        result['valid'] = True
        result['secret'] = re.search(r'secret=([A-Z2-7=]+)', uri).groups()[0]
        if(not result['secret']):
            result['valid'] = False
    else:
        result['valid'] = False
    return result


def read_qr_image(file_path: str) -> str:
    if(os.path.exists(file_path)):
        d = decode(Image.open(file_path))
        return d[0].data.decode("utf-8")
    else:
        return ''


def check_is_base32(key: str) -> bool:
    return True if re.fullmatch(r'[A-Z2-7=]+', key) else False


if __name__ == '__main__':
    qr_image = 'qr.png'
    skey: str = get_skey()
    if(not skey):
        #skey = input_skey()
        uri_str = read_qr_image(qr_image)
        if(uri_str):
            uri = parse_otpauth_uri(uri_str)
            if(uri['valid']):
                skey = uri['secret']
                os.remove(qr_image)
            else:
                print('Invalid QR code!')
                skey = input_skey()
        else:
            print('QR code not found.')
            skey = input_skey()

        set_skey(skey)

    result = get_totp(skey)
    pyperclip.copy(result)
    print(f'OTP {result} copied!')
