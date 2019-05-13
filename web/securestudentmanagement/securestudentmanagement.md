# Secure Student Managment

## Solution

The hint tells the user that there password may be the username in reverse.

Upon looking at the source of the page they will see that there is a user with the username 40000000.

Therefore the username password combination is:
40000000:00000004

Upon logging in the user has multiple options.
If they go to the Upload a register they will recieve a 404 page. However stripping the file so they only go to the directory /bg/ they will see that directory listing is enabled.

Here they can navigate to /bg/upload.

Now it is a case of enumerating through each PDF file in the directory and searching for LTDH19.

When the find this they will get the flag as they will know which file the flag is in. 
