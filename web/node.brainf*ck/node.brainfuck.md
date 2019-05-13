# Node.brainfuck triliogy

__Challenge Author: @CuPcakeN1njA__

## Solution

The first challenge is to learn how to use the application.

Requesting it normally in a web browser gives you an error.

The trick is to connect via netcat and send a http request which is encoded in brainfuck.

You can test that the server is accepting brainfuck by passing any valid brainfuck. For example if you connect and give it `.` you will get a 400 code http response. This indicates that the server recieved and invalid http request. Pointing you towards the brainfuck was decoded and sent as a http request. By encoding a http request with brainfuck you would be able to get a 200 response. 

This will return the first flag as a http response.

# Node.brainfuck 2
## Solution
Now you can talk to the backennd you can request robots.txt. This gives you a clue that ypou are using the wrong method to request the page.
If you request the index page with the POST method you will recieve the second flag.

# Node.brainfuck 3
## Solution
After getting the 2nd flag you will get a hint that the devloper uses nano. If you use nano and get the message that was displayed in the hint it indicates that a swap file has been left behind. Therefore to solve the final section you just have to request .index.php.swp.

This will give you the final flag.
