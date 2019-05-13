# No <3 4 PHP
## Author @CuPcakeN1njA
## Score: 500
## Category: Web

This challenge is a PHP exploitation challenge. Multiple exploits are nested to create a hard web challenge

## Description
PHP at its finest, find the weaknesses and get the flag!!!

## Hints
1.) Understand each Function
2.) When two things collide bad things happen
3.) This is Punny

## Solution
This challenge consists of 4 checks. Each check must be bypassed.
The first check:
```if(strpos(str_replace(array('e','n', 't', 'e', 'r'), '',$_), "enter") !== false){```
Is bypassed by setting the get parameter `_` to an array. This can be done like `_[]=`.

Now moving onto the second check. This check is
```if (!preg_match('/[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890\'\/~`\!@#\$%\^&\*\(\)_\-\+=\{\}\[\]\|;:"\<\>,\.\?\\\]/', $hash1)){```
To bypass this simply set the paramter `hash1` to a character that is not in the regex query. An example could be `hash1=%09`.

The third check is bypassed by simply setting the parameters `hash2` and `hash`.

The total get parameters looks like.
```?_[]&hash1=%09&hash2=5&hash=```
