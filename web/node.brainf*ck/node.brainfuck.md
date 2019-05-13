# Node.brainfuck triliogy
## Solution

The first challenge is to learn how to use the appliucation.

Requesting it normally in a web browser gives you an error.

The trick is to connect via netcat and send a http request which is encoded in brainfuck.

This will return the first flag as a http response.

# Node.brainfuck 2
## Solution
Now you can talk to the backennd you can request robots.txt. This gives you a clue that ypou are using the wrong method to request the page.
If you request the index page with the PUT method you will recieve the flag.

# Node.brainfuck 3
## Solution
After gettinbg the 2nd flag you will get a hint that the devloper uses nano. If you use nano and get the message that was displayed in the page this leaves an arthifact behibd. It is a swap file. Therefore to solve the final section you just have to request .index.php.swp.

This will give you the final flag.
