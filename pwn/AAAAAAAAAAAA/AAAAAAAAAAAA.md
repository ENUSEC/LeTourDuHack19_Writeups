# AAAAAAAAAAAA

__Challenge Author: @CuPcakeN1njA__

## Soltuion

The binary you are given contains the source code.

You can see this by loading the bianry in gdb

`$> gdb binary`

`$> list`

This will give you the source. From this you can see the first section is vulnerable to a buffer overflow. So entering a large number of characters will overflow the buffer and allow you to progress to the next part.

This then gives you another input. In this input all you have to do is put nothing and you are presented the flag.

The flag locally is not the same as the flag which was on the remote server.
