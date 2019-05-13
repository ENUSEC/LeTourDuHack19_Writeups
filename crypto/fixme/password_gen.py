import base64, sys, md5, os
from Crypto.Cipher import AES
from Crypto import Random
alph = "abcdefghjiklmnoqprstuvwxyz"
if(len(sys.argv) != 2):
	print("Usage: python %s" % os.path.basename(__file__) + " (8 character long key)")
else:
	if(len(sys.argv[0]) != 0):
		key = "SUPERKEY"
	else:
		key = sys.argv[1]
	print(md5.new(''.join([base64.b64encode(AES.new(i*16, AES.MODE_CBC, key*2).encrypt(key*2)) for i in alph])).hexdigest())
