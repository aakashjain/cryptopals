####################
# Hex to Base64

def hextobin(b16):
	if len(b16)%2:
		b16 = '0' + b16
	return bin(int(b16, 16))[2:].zfill(4*len(b16))

def bintob64(b2):
	chunks = len(b2)%24
	if chunks:
		pad = (24 - chunks)/8
		b2 += '0'*8*pad
	b64 = ''
	for i in xrange(0, len(b2), 6):
		n = int(b2[i:i+6], 2)
		if n < 26:
			b64 += chr(n + ord('A'))
		elif n < 52:
			b64 += chr(n - 26 + ord('a'))
		elif n < 62:
			b64 += chr(n - 52 + ord('0'))
	if chunks:
		b64 = b64[:-pad] + '='*pad
	return b64

def hextob64(b16):
	return bintob64(hextobin(b16))

####################
# Fixed XOR

def fixedxor(x, y):
	if len(x) != len(y):
		return False
	x, y = int(x, 16), int(y, 16)
	return hex(x ^ y)[2:].rstrip('L');

####################

if __name__=='__main__':
	print hextob64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d') == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
	print hextob64('41') == 'QQ=='
	print fixedxor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965') == '746865206b696420646f6e277420706c6179'
