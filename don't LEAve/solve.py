from pwn import *
import os
import subprocess

def turn_payload_bytes(payload: str) -> bytes:
    output = b''
    skip = 0
    for i in range(len(payload)):
        if skip:
            skip -= 1
        elif payload[i] == '\\' and payload[i+1] == 'x':
            output += bytes.fromhex(payload[i+2:i+4])
            skip = 3
        else:
            output += payload[i].encode()

    return output


normal_token = 'test'
append_token = 'admin=1'

c = process(['python3', 'chall.py'])
c.recvuntil(b'exit\n')
c.sendline(b'1')

c.recvuntil(b'hex: ')
c.sendline(normal_token.encode().hex().encode())

mac = c.recvline().decode()[:-1]
# print(mac)
# print(f'hashpump -s "{mac}" --data "admin=0;{normal_token}" -a "{append_token}" -k 8')
new_mac = subprocess.check_output(['hashpump', '-s', f'{mac}', '--data', f'admin=0;{normal_token}',
                                    '-a', f'{append_token}', '-k', '8'])
new_mac, appended_token = new_mac.decode().replace('\\\\','\\').split('\n')[:2]
# print(new_mac)
# print(appended_token)
appended_token = turn_payload_bytes(appended_token).hex()
# print(appended_token)

c.recvuntil(b'exit\n')
c.sendline(b'2')

c.recvuntil(b'hex: ')
c.sendline(appended_token.encode())

c.recvuntil(b'verify: ')
c.sendline(new_mac.encode())

print(c.recvline())
c.close()