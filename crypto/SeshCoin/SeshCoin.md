# SeshCoin
## Category: Crypto
## Score: 300
## Author: CuPcakeN1njA

We need you to break into Kevins SeshCoin wallet and rinse their account.
Please move all the coins away from his account.

We have managed to acquire source code of the daemon in it's development, can you find the vulnerabilities and complete your mission.

`nc target port`

file: local.py

# Hints

1. Is random as random as random says it is

# Solution
Upon reviewing the generate.py and local.py the competitor will find the password to get through the first stage of this challenge. They will also find that the key pair that is generated when the daemon first runs is created using a seed. However since this seed is the time stamp and since we know that it is created when the daemon first runs we can begin to create a list of time stamps that the seed used to generate the private key will be in. Now we can run an offline brute force of the private key by changing the seed until we create a key pair that contains the public key the user can get from the daemon.

A POC can be seen in `admin/solve.py`.
