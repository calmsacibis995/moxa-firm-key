#!/usr/bin/env python3

#
# Originally written by stacksmashing (Thomas Roth)
#

# The obfuscated Moxa decryption key
passwd = [0x95, 0xb3, 0x15, 0x32, 0xe4, 0xe4, 0x43, 0x6b, 0x90, 0xbe, 0x1b, 0x31, 0xa7, 0x8b, 0x2d, 0x05]

i = 0

# Small XOR cipher implementation, derived from Ghidra de-compilation.
while(i < len(passwd)):
    passwd[i] ^= 0xa7
    passwd[i+1] ^= 0x8b
    passwd[i+2] ^= 0x2d
    passwd[i+3] ^= 5
    i += 4

# Print the password in plain text.
print("The password is: ")
for c in passwd:
    print(chr(c), end="")
print("")

# Print the AES-128 key.
print("The AES-128 key is: ")
for c in passwd:
    print(hex(c)[2:], end="")
print("")
