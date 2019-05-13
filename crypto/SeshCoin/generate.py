from Crypto.PublicKey import RSA
import random, string, md5, base64, time

def randomString(stringLength):
	letters = string.ascii_letters
	return ''.join(random.choice(letters) for i in range(stringLength))

def generateKeys(start=(int(time.time()) + random.randint(1,100))):
	#print(start)
	random.seed(start)
	rnd = randomString
	key = RSA.generate(2048, rnd)
	private_key = key.exportKey()
	public_key = key.publickey().exportKey()
	return [base64.b64encode(md5.new(public_key).digest()),
		base64.b64encode(md5.new(private_key).digest())]



#print("SeshCoin Address: " + getAddress())
