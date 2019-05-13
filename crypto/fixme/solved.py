import base64, sys, md5, os
from Crypto.Cipher import AES
from Crypto import Random
alph = "abcdefghijklmnopqrstuvwxyz"
if(len(sys.argv) != 2):
	print("Usage: python %s" % os.path.basename(__file__) + " (8 character long key)")
else:
	if(len(sys.argv[1]) != 8):
		key = "SUPERKEY"
	else:
		key = sys.argv[1]
	print(md5.new(''.join([base64.b64encode(AES.new(key*2, AES.MODE_CBC, i*16).encrypt(i*16)) for i in alph])).hexdigest())
