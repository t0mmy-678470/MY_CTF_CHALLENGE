from pwn import *
from Crypto.Util.Padding import pad

guess_list = '!@#$%^&*()1234567890-_=+qwertyuiop[]{}asdfghjkl;\'zxcvbnm,./<>QWERTYUIOPASDFGHJKLZXCVBNM'

def to_blocks(response: bytes):
    blocks = []
    for i in range(0,len(response),16):
        blocks.append(response[i:i+16])
    return blocks

con = process(['python3', 'chall.py'])
known = b''
printable_index = 0
guess = guess_list[0].encode()
while len(known)<15:
    payload = pad(guess+known, 16) + b'a'*( len(known)+2 )
    con.recvuntil(b'hex: ')
    con.sendline(payload.hex().encode())
    output = con.recvline()
    output = bytes.fromhex(output.decode())
    if len(output) != 48:
        print(f'output length error: {len(output)}')
        print(f'payload = {payload}')
        break

    # 判斷有沒有出錯
    if b'Traceback' in output:
        print(output)
        con.interactive()
        
    output = to_blocks(output)
    # print(output[0], output[-1])
    if output[0] == output[-1]: # guess is right
        known = guess + known
        print(known)
        printable_index = 0
        guess = guess = guess_list[0].encode()
    elif guess == guess_list[-1].encode():
        print('error')
        break
    else:
        printable_index += 1
        guess = guess_list[printable_index].encode()

con.close()