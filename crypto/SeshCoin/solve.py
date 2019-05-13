from Crypto.PublicKey import RSA
import random, string, md5, base64, time
import sys

target ="GO6jFhMfB4j5y8cVfLl2BA=="

def app(add):
	if(len(add) == 1):
		add = "0" + add
	return add

def randomString(stringLength):
	letters = string.ascii_letters
	return ''.join(random.choice(letters) for i in range(stringLength))

def generateKeys(myseed):
	random.seed(myseed)
	rnd = randomString
	key = RSA.generate(2048, rnd)
	private_key = key.exportKey()
	public_key = key.publickey().exportKey()
	return [base64.b64encode(md5.new(public_key).digest()),
		base64.b64encode(md5.new(private_key).digest())]

start = 1549988187
end = start + 100

for i in range(start,end):
	b = generateKeys(i)
	print("seed = " + str(i))
	print(str(b))
	if(str(b[0]) == target):
		print("Successfully cracked")
		print("Private Key: " + b[1])
		sys.exit(0)
