# Image Manipulation 2

__Challenge Author: @CuPcakeN1njA__

## Solution
Similar to image manipluation 1 this challenge involves modifying and manipulating the pixels in an image.

In order to solve this one the user must research the barcoce type.

You can find information here: https://en.wikipedia.org/wiki/PDF417

Essentailly the important section which is the data is the middle section.

Once they have this information they take only the data therefore the signatures stay the same and reverse the data.
The algorithm to do this is fairly simple however they must rewrite all the data reversed with the same signatures and padding.

If they do this correctly they will be able to scan the barcode and get the flag.

I have attached my solution.
