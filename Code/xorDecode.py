#!/usr/bin/python3
#XOR each individual hex byte in the content using the key
import sys
from binascii import unhexlify, hexlify
from itertools import cycle
content = sys.argv[1]
key = sys.argv[2]
conteent = hexlify(bytes(char1 ^ char2 for char1, char2 in zip(unhexlify(content), cycle(unhexlify(key)))))
bytearray.fromhex(content.decode("utf-8")).decode()