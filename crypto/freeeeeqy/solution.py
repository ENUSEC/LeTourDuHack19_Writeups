f = open("cipher.txt", "r")
t = f.read()
f.close()

chars = "abcdefghijklmnopqrstuvwxyz"
flag = ""

for i in range(len(chars)):
	flag += chr(t.count(chars[i]))

print(flag)
