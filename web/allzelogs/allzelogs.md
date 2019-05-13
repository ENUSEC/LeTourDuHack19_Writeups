# All ze Logs

__Challenge Author: @CuPcakeN1njA__

## Solution

This challenge first requires you to view the page source. Right click -> View Source.

Which revels you use the get parameter "?write" in its comments.

By using this parameter you write to a file however the user input is sanitized.

Therefore if you visited `http://challenge.com/?write=helloworld` helloworld will have been written to the file.

When you write data it will give you the location where you can view the file. For example 
```
active.php?log=/tmp/log44235.txt
```
This is vulnerable to local file inclusion however it is using a white list therefore only certain files can be included. This can be tested by visitng `active.php?log=/etc/passwd` Which will give you /etc/passwd however `../../../../etc/passwd` will give you an error.This comes in handy later on.

If you look at the cookies you have you will see a session id and fallback cookie. This fallback cookie contains a base64 encoded serialised object.

The description says that a fallback mechnism is in place. Meaning if you can stop the application functioning you fallback to the fallback cookie and the serialised object is  deserialised. In this case that means writing data to a different log file.

To break the application make a request: ?write[]= turning the write variable into and array and exploiting a type confusion vulnerabiltity. This then triggers the fallback and we have a deserialisation vulnerabilty. This is abused to write to the log file given and the contents can be modified.

Within the serialized object there was multiple different sections. The filepath which when changing did nothing and the contents which when changing changed what was wrote to tthe filepath specified in the serialised object.

Now we can use the LFI to include the log file we just wrote unsanitized data too.

Now we have a problem because the deserialisation breaks when certain characters are given to it. Therefore in order to bypass this we can use url encoding as there is a hidden urldecode operation performed on the string before it is written to a file. (url encoding is a common bypass for data sanitation).

Now urlencode a php webshell or reverseshell and pass it into your serialised object. Now trigger the fallback mechanism by using type confusion. Now use the lfi vulnerabilty to include the log file and execute your payload.
