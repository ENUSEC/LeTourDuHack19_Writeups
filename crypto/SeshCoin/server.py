import generate, time, random, sys, threading, socket
from time import sleep
# Beta version of deamon
# Run once to emulate the deamon
# Wallet will be set up when you run the deamon
# TODO
# 1. Finish writing initial login (default password will be seshcoin)
# 2. Write AUTHENTICATED modules
# 3. 

status = 0
auth = 0
balance = 200000
man = """
MANUAL


authenticate => Submit the base64 encoded hash of your Private key in order to
                authenticate to the system

showaddress => Show your current SeshCoin address

|--------------------------|

showbalance => Show balance that is currently in you're SeshCoin wallet

move => Move a given amount out from your wallet and back to the
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
move => Move SeshCoin
\n\n"""
starttime = time.asctime()
# Begin Welocme message to be displayed when client logs in
welcome = "Welcome to the SeshCoin Deamon\nYour one stop shop for managing your favourite cryptocurrency\nDeamon Started at:" + starttime + "\n\n"
# End welcome message
print("Generating your Address ... ")
address = generate.generateKeys()
print("Debugging: " + str(address))
print("Address Generated Successfully\nWallet created")
print("Deamon ready to use")

# Each session starts here
balance = 200000
me = ""
count = 0

def main(connection, client_address):
	#connection.sendall("")
	#connection.recv(25)
	auth = 0
	balance = 200000
	me = ""
	count = 1
	status = 0
	connection.sendall("\n\n" + welcome)
	while True:
		if(status == 1):
			if(balance <= 0):
				connection.sendall("\n!!!HOLY SESH!!! Your Balanced is !!!RINSED!!!\n")
				connection.sendall("LTDH19{YoU_Br0K3_Th3_K3y_G3n}\n")
			if(count >= 3):
				break
			connection.sendall("\n" + me + "$> ")
			command = connection.recv(25).strip()
			if(command == "help"):
				connection.sendall(help)
			elif(command == "man"):
				connection.sendall(man)
			elif(command == "\nshowaddress"):
				connection.sendall("\nYou're SeshCoin Address is: " + address[0])
			elif(command == "exit"):
				connection.sendall("\nExiting")
				break
			elif(command == "authenticate"):
				connection.sendall("\nPlease Enter Private Key: ")
				key = connection.recv(25).strip()
				if(key == address[1]):
					connection.sendall("\nSuccessfully authenticated")
					auth = 1
					me = "SESH~"
				else:
					connection.sendall("\nAuthentication Unsuccessful")
			elif(command == "showbalance"):
				if(auth == 0):
					connection.sendall("\nNot Authenticated")
				else:
					connection.sendall("\nCurrent Ballance: " + str(balance))
			elif(command == "move"):
				if(auth == 0):
					connection.sendall("\nNot Authenticated")
				else:
					connection.sendall("\nAmount: ")
					amount = int(connection.recv(25).strip())
					if(amount > balance):
						connection.sendall("\nYou do not have that much much in your balance")
					else:
						connection.sendall("\nMoving " + str(amount))
						balance = balance - amount
						connection.sendall("\nTransaction completed")
			else:
				connection.sendall("Command Not Found")
		else:
			connection.sendall("\nPassword: ")
			password = connection.recv(25).strip()
			if(count >= 3):
                                connection.sendall("\nYou have ran out of attempts")
				break
			if(password == "seshcoin"):
				status = 1
			else:
				count += 1
				connection.sendall("\nIncorrect Password")
	connection.sendall("\nProgram Exiting\n")
	connection.close()

if __name__ == "__main__":
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Place server address and port
        server_address = ('127.0.0.1', 7777)
        print >>sys.stderr, 'starting up on %s port %s' % server_address
	try:
        	sock.bind(server_address)
        	sock.listen(1)
        	while True:
        	        print >>sys.stderr, 'waiting for a connection'
        	        connection, client_address = sock.accept()
        	        threading.Thread(target=main, args=(connection,client_address,)).start()
	except Exception as e:
		print >>sys.stderr, 'Connection Closing: ', e
		sock.shutdown()
		sock.close()
