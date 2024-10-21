from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os

nonce = os.urandom(7)
FLAG = os.getenv("FLAG") # NCtfU{....}

print("I made an easy online encryption and decryption tool, \
but I haven't implement the decryption function yet.")


while True:
    cmd = input("""
What do you want to encrypt? (number)
1) my onw text
2) see an example
3) exit
""")
    if cmd == '1':
        key = input("Please input your key in hex: ")
        text = input("Please input your text in hex: ")
        if len(key) > 32:
            print('Wrong key length.')
            continue
        try:
            key = key.zfill(8)
            key = bytes.fromhex(key)
            text = bytes.fromhex(text)
        except:
            print("You're key and/or text are/is weird!!")
            continue

        enc = DES.new(key, DES.MODE_CTR, nonce=nonce).encrypt(text)
        print(f"Here you go: {enc.hex()}")

    elif cmd == '2':
        key = input("Please input your key in hex: ")
        if len(key) > 32:
            print('Wrong key length.')
            continue
        try:
            key = key.zfill(8)
            key = bytes.fromhex(key)
        except:
            print("You're key is weird")
            continue

        enc = DES.new(key, DES.MODE_CTR, nonce=nonce).encrypt( pad(FLAG.encode(),8) )
        print(f"Here you go: {enc.hex()}")
    
    elif cmd == '3':
        break

    else:
        print("please input 1 or 2 or 3")
    

print('bye~~')