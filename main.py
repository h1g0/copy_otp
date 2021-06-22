import pyotp
import pyperclip

def get_totp(secret: str) -> str:
    totp = pyotp.TOTP(secret)
    result = totp.now()
    return result

def get_skey_from_file(file_path: str)->str:
    with open(file_path) as f:
        result = f.readline().strip()
        return result

if __name__ == '__main__':
    result = get_totp(get_skey_from_file('secret.txt'))
    pyperclip.copy(result)
    print(f'OTP {result} copied!')
