# R U Alive

## Solution
In this challenge you are given a pcap with a large number of icmp requests to different places.

You have to notice that some of them go to places such as google.com and microsoft.com whilst others go to an ip address. You have to first filter the requests to that specific IP address.

Then you extract all the TTL valuse which are actually ascii character codes. Once they are extracted for example with tshark you can then convert them to ascii and you will get the flag.


