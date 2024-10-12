from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

key = os.urandom(16)
iv  = os.urandom(16)
FLAG = os.getenv("FLAG").encode()
# FLAG = '0123456789abcdefFLAG{0123456789}'.encode()
assert(len(FLAG) == 32)

enc_flag = AES.new(key, AES.MODE_CBC, iv).encrypt(FLAG)
# print("""I encrypted your input with FLAG, so you would never get the FLAG, right?""")
print(f'encrypted FLAG: \n{enc_flag.hex()}')
while True:
    ciphertext = input("I can verify your ciphertext in hex: ")

    # 確認是輸入16進制的值
    try:
        ciphertext = bytes.fromhex(ciphertext)
    except:
        print("Please input hex")
        continue

    # 確認密文的長度正確
    try:
        plaintext = AES.new(key, AES.MODE_CBC, iv).decrypt(ciphertext)
    except:
        # print(error)
        print("Your ciphertext's length is incorrect.")
        continue
    
    # 確認明文的padding正確
    try:
        # print(plaintext)
        unpad(plaintext,16)
        print("It's valid ciphertext.")
    except:
        print('Wrong padding.')