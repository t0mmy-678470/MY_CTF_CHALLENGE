import hashlib
import os

FLAG = os.getenv("FLAG")
salt = os.urandom(8)

while True:
    cmd = input("""
Please input command (number) that you want to perform: 
1. Get auth
2. Get flag
3. exit
""")
    if cmd == '1':
        token = input("Please input token in hex: ")
        try:
            token = bytes.fromhex(token)
        except:
            print('Your token is not in hex.')
            continue

        if b'admin=1' in token:
            print("You're not admin!!")
            continue

        mac = hashlib.sha256(salt + b'admin=0;' + token).hexdigest()
        print(mac)
    elif cmd == '2':
        token = input("Please input token in hex: ")
        untrustful_mac = input("Please input your mac to verify: ")
        try:
            token = bytes.fromhex(token)
        except:
            print('Your token is not in hex.')
            continue
        real_mac = hashlib.sha256(salt + token).hexdigest()
        if real_mac == untrustful_mac:
            if b'admin=1' in token:
                print(f"Here's the flag: {FLAG}")
                break
            else:
                print("Only admin can get the flag")
        else:
            print("You're mac is unauthorized")
    elif cmd == '3':
        break
    else:
        print("Please input 1 or 2")
        
print('good bye')