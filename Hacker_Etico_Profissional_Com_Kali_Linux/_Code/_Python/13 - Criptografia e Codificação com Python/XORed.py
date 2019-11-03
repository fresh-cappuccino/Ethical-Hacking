import sys
import string

f = open("ciphers.txt", "r")

MSGS = f.readlines()

def strxor(a, b):
	if len(a) > len(b):
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in
		zip(a[:len(b)], b)])
	else:
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def encrypt(key, msg):
	c = strxor(key, msg)
	return c

for msg in MSGS:
	for value in string.ascii_letters:
		for value2 in string.ascii_letters:
			for value3 in string.ascii_letters:
				key = value+value2+value3
				answer = encrypt(msg, key)
				print answer[3:]
