# Can't Read This

__Challenge Creator: @Pigoboom1__

## Solution
Get the flag by copying the header from the none encrypted image and then using it to replace the header of the encrypted image. 

As AES mode ECB has been used for the encryption of the image, patterns will show up when it is opened in a typical image viewer and so they should be able to make out that the flag is

ltdh19{ecb_is_not_very_good}
