import generate, time, random, sys
from time import sleep
# Beta version of deamon
# Run once to emulate the deamon
# Wallet will be set up when you run the deamon
# TODO
# 1. Finish writing initial login (default password will be seshcoin)
# 2. Write AUTHENTICATED modules
# 3. 

man = """
MANUAL


authenticate => Submit the base64 encoded hash of your Private key in order to
                authenticate to the system

showaddress => Show your current SeshCoin address

|--------------------------|

showbalance => Show balance that is currently in you're SeshCoin wallet

move (amount) => Move a given amount out from you're wallet and back to the
                 creator
"""
help = """
man => Manual
authenticate => Authenticate to the system
showaddress => Show SeshCoin address
help => ? DUH ?
suprise => Heres a suprise

|------------------|
Authenticated commands
showbalance => Show account balance
move (amount) => Move Coinage
"""
starttime = time.asctime()
# Begin Welocme message to be displayed when client logs in
welcome = "Welcome to the SeshCoin Deamon\nYour one stop shop for managing your favourite cryptocurrency\nDeamon Started at:" + starttime
# End welcome message
print("Generating your Address ... ")
address = generate.generateKeys()
#print("Debugging: " + str(address))
print("Address Generated Successfully\nWallet created")
print("Deamon ready to use")
print("\n\n" + welcome)
while True:
	command = raw_input("$> ")
	if(command == "help"):
		print(help)
	elif(command == "man"):
		print(man)
	elif(command == "showaddress"):
		print("You're SeshCoin Address is: " + address[0])
	elif(command == "exit"):
		sys.exit(0)
	elif(command == "authenticate"):
		key = raw_input("Please Enter Private Key: ")
		if(key == address[1]):
			print("Successfully authenticated")
			# HERE SET STATUS FLAG
		else:
			print("Authentication Unsuccessful")
