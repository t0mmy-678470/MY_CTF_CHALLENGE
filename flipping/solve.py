from pwn import *
from Crypto.Util.Padding import pad


def to_blocks(response: bytes):
    blocks = []
    for i in range(0,len(response),16):
        blocks.append(response[i:i+16])
    return blocks

def get_guess(i2,known_len):
    guess = ''
    for i in range(0,len(i2),2):
        guess += hex(int(i2[i:i+2],16) ^ (known_len+1))[2:].zfill(2)
    guess = '0'*(32-len(guess)) + guess
    return guess
    

# con = process(['python3', 'chall.py'])
con = remote('140.115.152.10', 10001)

ciphertext = con.recvlines(2)[1].decode()
c1 = ciphertext[:32]
c2 = ciphertext[32:]
i2 = ''
unknown_len = 16
guess = get_guess(i2, 16-unknown_len)

while unknown_len > 0:
    con.recvuntil(b'hex: ')
    con.sendline(guess.encode()+c2.encode())

    # plain = con.recvline()
    # print(plain.decode()[:-1])
    result = con.recvline()
    if result == b'It\'s valid ciphertext.\n':
        i2 = hex((17-unknown_len) ^ int(guess[unknown_len*2-2:unknown_len*2],16))[2:].zfill(2) + i2
        unknown_len -= 1
        # print(f"corrected guess = {guess}")
        guess = get_guess(i2, 16-unknown_len)
        # print(f'new guess = {guess}')
    elif result == b'Wrong padding.\n':
        if int(guess[unknown_len*2-2:unknown_len*2], 16) == 0xff:
            print('[error] out of range')
            print(guess)
        next = hex(int(guess[unknown_len*2-2:unknown_len*2], 16) + 1)[2:].zfill(2)
        guess = guess[:unknown_len*2-2] + next + guess[unknown_len*2:]
        # print(guess)
    else:
        print("[error] unexpected result")
        print(result)
        con.interactive()
        break

# print(f'i2 = {i2}')
# i2 ^ c1
for i in range(0,len(i2),2):
    print(chr(int(i2[i:i+2],16) ^ int(c1[i:i+2],16)), end="")
print()

con.close()