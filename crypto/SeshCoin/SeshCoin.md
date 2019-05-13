# SeshCoin

__Challenge Author: @CuPcakeN1njA__

## Solution
Upon reviewing the generate.py and local.py the competitor will find the password to get through the first stage of this challenge. 

They will also find that the key pair that is generated when the daemon first runs is created using a seed. However since this seed is the time stamp and since we know that it is created when the daemon first runs we can begin to create a list of time stamps that the seed used to generate the private key will be in. You can get the timestamp from the date given when you first connect to the server.

Now we can run an offline brute force of the private key by changing the seed until we create a key pair that contains the public key the user can get from the daemon.

A POC can be seen in `admin/solve.py`.

For an example I have pasted the bellow so that you can attempt the challenge. This emmulates the output you would have recieved if you were to log into the application and request to see your address. The information bellow is enough to solve the challenge. The correct private key for this particular instance is `6bl53tBi6VZUVFdnRpwYuQ==` if you are able to get this then you would have been able to get the flag.

```
Welcome to the SeshCoin Deamon
Your one stop shop for managing your favourite cryptocurrency
Deamon Started at:Mon May 13 16:46:49 2019


Password: seshcoin

$> help

man => Manual
authenticate => Authenticate to the system
showaddress => Show SeshCoin address
help => ? DUH ?
suprise => Heres a suprise

|------------------|
Authenticated commands
showbalance => Show account balance
move => Move SeshCoin



$> showaddress

You're SeshCoin Address is: FRxqe36WU0iLwMO72uG5Pg==
$> 

```

I have attached the server.py and the supporting files as well as a bruteforce script which will bruteforce the public key based from the timestamp you give it.
