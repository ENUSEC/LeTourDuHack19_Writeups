# PPower+ 2

__Challenge Author: @CuPcakeN1njA__

## solution
After clicking to get started the user is redirected to a portal which allows them to move an amount from their temperature allowance to the current temperature.

Before they do anything they will want to take note of the token cookie. 

Then they transfer the maximum amount they can which is 2000.

Now if they try and transfer anything else they will not have enough too.

Therefore if they replace the token cookie with the cookie they had before then they can transfer the same amount again.

Repeat this proccess until the current temperature is greater than the max and you are presented the flag.

In order to solve the challenge you just had to reuse the signed cookie with the maximum temperature. This is because the temperature and the session were stored in different cookies.
