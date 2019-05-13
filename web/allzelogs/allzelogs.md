# All ze Logs

## Solution

This challenge first requires you to view the page source. Which revels you use the get parameter "write".

By using this parameter you write to a file however the user input is sanitized.

When you write data it will give you the location where you can view the file.
active.php?log=filenamehere.

This is vulnerable to local file inclusion however it is using a white list therefore only certain files can be included.

This comes in handy later on.

If you look at the cookies you have you will see a session id and fallback cookie. This fallback cookie contains a base64 encoded serialised object.

The description says that a fallback mechnism is in place. Meaning if you can stop the application functioning you fallback to the fallback cookie and the serialised object is  deserialised. In this case that means writing data to a different log file.

To break the application make a request: ?write[]= turning the write variable into and array and exploiting a type confusion vulnerabiltity. This then triggers the fallback and we have a deserialisation vulnerabilty. This is abused to write to the log file given and the contents can be modified.

Now we can use the LFI to include the log file we just wrote unsanitized data too.

(remmeber your serialised object must contain the legnth of the string)

Now we have a problem because the deserialisation breaks when certain characters are given to it. Therefore in order to bypass this we can use url encoding as there is a hidden urldecode operation performed on the string before it is written to a file. (url encoding is a common bypass for data sanitation).

Now urlencode a php webshell or reverseshell and pass it into your serialised object. Now trigger the fallback mechanism by using type confusion. Now use the lfi vulnerabilty to include the log file and execute your payload.
