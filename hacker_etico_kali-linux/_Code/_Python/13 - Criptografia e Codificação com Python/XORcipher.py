from os import urandom

def u_ord(c):
    """Adapt `ord(c)` for Python 2 or 3"""
    return ord(str(c)[0:1])


def genkey(length):
    """Generate key"""
    return urandom(length)


def xor_strings(s, t):
    """xor two strings together"""
    return "".join(chr(u_ord(a) ^ u_ord(b)) for a, b in zip(s, t))

message = 'ola a todos'
print ('mensagem:', message)

key = genkey(len(message))
print ('key:', key)

cipherText = xor_strings(message, key)
print ('cipherText:', cipherText)
print ('decrypted:', xor_strings(cipherText, key))

# verify
if xor_strings(cipherText, key) == message:
    print ('Unit test passed')
else:
    print ('Unit test failed')

