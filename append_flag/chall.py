from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

key = os.urandom(16)
cipher = AES.new(key, AES.MODE_ECB)
FLAG = os.getenv("FLAG")
assert(len(FLAG) == 15)

print("""I encrypted you're input with flag, so you would never get the flag, right?""")
while True:
    payload = bytes.fromhex(input("Try input something in hex: "))
    payload += FLAG.encode()
    payload = pad(payload,16)
    enc = cipher.encrypt(payload)
    print(enc.hex())