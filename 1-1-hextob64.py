def hextobin(hex):
	b2 = ''
	for i in hex:
		if '0' <= i and i <= '9':
			b2 += bin(ord(i) - ord('0'))[2:].zfill(4)
		elif 'A' <= i and i <= 'Z':
			b2 += bin(ord(i) - ord('A') + 10)[2:].zfill(4)
		elif 'a' <= i and i <= 'z':
			b2 += bin(ord(i) - ord('a') + 10)[2:].zfill(4)
	return b2

def bintob64(b2):
	b64 = ''
	for i in xrange(0, len(b2), 6):
		n = int(b2[i:i+6], 2)
		if n < 26:
			b64 += chr(n + ord('A'))
		elif n < 52:
			b64 += chr(n - 26 + ord('a'))
		elif n < 62:
			b64 += chr(n - 52 + ord('0'))
	return b64

def hextob64(hex):
	return bintob64(hextobin(hex))

if __name__=='__main__':
	hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
	b64 = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
	print hextob64(hex) == b64