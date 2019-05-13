# AAAAAAAAAAAA
## Soltuion

The binary you are given contains the source code.

You can see this by loading the bianry in gdb
`$> gdb binary`
`$> list`
This will give you the source. From this you can see the first section is vulnerable to a buffer overflow. This then gives you another input. In this input all you have to do is put nothing and you are presented the flag.
