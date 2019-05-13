# Fix Me

## Solution
In this challenge you notice that the python file md5 hashes the contents of some output from an AES encryption.
The AES encryption encrypts each letter of the aplhabet (16 times) against a flag of 8 characters (2 times). This happens for each character in the
alphabet and these are then base64 encoded joined together and md5sumed. This creates a single md5 hash.

The trick to solving this challenge is to notice that in the AES algorithm the IV and Key have been switched, therefore you must switch
these around.

You must also delete the part of the code that is checking the length of the first sys.argv parameter, as this should be checking the 
second index and be checking against 8, as that way of the key doesnt have legnth 8 it will become a default value.

finally the final trick is to notice in the alphabet there are a few characters switched postions. For example the i and j, and the p and q.
Once you have made these changes you will be able to get the flag.


LTDH19{N0t_aLL_thAt_tR1ckY}

