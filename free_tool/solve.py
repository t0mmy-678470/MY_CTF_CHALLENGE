from pwn import *

# c = process(['python3', './chall.py'])
c = remote('140.115.152.10', 10004)

c.recvuntil(b"exit\n")
c.sendline(b'2') # cmd 2 (example)

c.recvuntil(b"hex: ")
c.interactive()
c.sendline(b"00"*8) # input key

c.recvuntil(b'go: ')
enc_flag_hex = c.recvline() # get result

c.recvuntil(b'exit\n')
c.sendline(b'1') # cmd 1 (my own text)

c.recvuntil(b"hex: ")
c.sendline(b"00"*8) # input key

c.recvuntil(b"hex: ")
c.sendline(enc_flag_hex) # input text

c.recvuntil(b'go: ')
flag_hex = c.recvline() # get result

c.recvuntil(b'exit\n')
c.sendline(b'3') # exit

print(bytes.fromhex(flag_hex.decode()))