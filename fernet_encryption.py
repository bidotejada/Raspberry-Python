from json import decoder
from cryptography.fernet import Fernet
# encryption
key=b'pdv4ABwAgu-dXsZf1kBfaKg28DUVllf50VrrMm38tiQ='
f=Fernet(key)

# encrypted message
fernet_token=f.encrypt("0000".encode("utf-8"))
print(fernet_token)
print(fernet_token.decode("utf-8"))

# decryption
# decrypted_message=f.decrypt(fernet_token)
# print(decrypted_message.decode("utf-8"))

def encrypt(decrypted_passcode):
    fernet_token = f.encrypt(decrypted_passcode.encode("utf-8"))
    return fernet_token


def decrypt(fernet_token):
    decrypted_passcode = f.decrypt(fernet_token).decode("utf-8")
    return decrypted_passcode