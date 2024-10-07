import hashlib
import os
hex1 = input('first token: ')
hex2 = input('second token: ')
try:
    b1 = bytes.fromhex(hex1)
    b2 = bytes.fromhex(hex2)
except:
    print('Please input hex')
    exit()
hash1 = hashlib.md5(b1).hexdigest()
hash2 = hashlib.md5(b2).hexdigest()
if hex1 != hex2 and hash1 == hash2:
    print("How did you do that?")
    print(os.getenv('FLAG'))
else:
    print(f'{hash1} != {hash2}')
    print("keep trying")
    print(os.getenv('FLAG'))