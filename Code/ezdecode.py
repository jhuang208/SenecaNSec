#!/usr/bin/python3
import sys
import base64
import time

try:
	string = sys.argv[1]
except IndexError:
	print("Please enter an argument to decode.")
	print("usage: python3 ezdecode.py VGhpbmtwYWRzIGFyZSBvdmVycHJpY2Vk")
	exit()

def Base64Decode(string):
	print("Base64:\n" + base64.b64decode(string).decode('ascii') + '\n')
	time.sleep(1)

def CaesarCipher(string):
	print("Caesar Cipher:")
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	string = string.lower()

	for key in range(len(alphabet)):
		translated = ''
		for symbol in string:
			if symbol in alphabet:
				num = alphabet.find(symbol)
				num = num - key
				if num < 0:
					num = num + len(alphabet)
				translated = translated + alphabet[num]
			else:
				translated = translated + symbol
		print(translated)
		time.sleep(0.2)
	print('\n')

Base64Decode(string)
CaesarCipher(string)
