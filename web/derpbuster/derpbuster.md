# Derp Buster

__Challenge Author: @CuPcakeN1njA__

## Solution:
Run OWASP Dirbuster with the wordlist as common.txt.
This wordlist is commonly used when dirb scanning.

Now you will be prompted for a regex string to match a 404 page.

The secret to this challenge was to use the tool `owasp dirbuster` which allows you to use a regex query to match a 404 page if it cannot detect it automatically.

An example of a working regex match is: .{25} which if you put into Owasp Dirbuster it will have given you the file with the flag in.
