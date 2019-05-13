# Forge Your Way

__Challenge Author: @CuPcakeN1njA__

## Solution

You can log in with any username password combination.

Now you were presented a file upload.

This has checks to stop bad files from being uploaded however it will upload the file into the upload directory and then delete it after 5 seconds. This means for 5 seconds the bad file is hosted on the webserver.

Unfortunately the user does not have permision to view the bad file however does have the location. (Due to a misconfiguration it was possible to access any php file uploaded for 5 seconds) therefore all you had to do was upload a php shell and navigate to the path it gave you. The file was available for 5 seconds after upload which allowed you to execute a reverseshell.

## Intended solution
Hidden in the log in mechanism there is a server side request forgery vulnerability.

When you log in you will examine that the page gets passed parameters. Username, Password, and Ping. This ping parameter can be modified and the web server will curl it. You can test this by ponting to your own webserver and examining the logs.

The solution to this challenge is to point this at a reverse shell you have uploaded and in the 5 second period where the file is on the web server exploit the server side request forgery so it will execute the reverse shell as the web server has permision to execute the uploaded file however you do not.

Once you have RCE you will be able to find and view the flag.
