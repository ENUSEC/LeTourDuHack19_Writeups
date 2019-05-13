# R U Alive

## Solution
In this challenge you are given a pcap with a large number of icmp requests to different places.

You have to notice that some of them go to places such as google.com and microsoft.com whilst others go to the ip address 13.37.13.37. You have to first filter the requests to that specific IP address.

Now you can notice that for each ICMP request the TTL is a different number. These are unusual as the TTL would not normally fluxuate in the way it is here.

The TTL values actuall relate to an ascii character. To solve this challenge all you have to do is extract the TTL values and convert them to ascii. You can use tshark to do that.
```
tshark -r rualive.pcapng -T fields -e ip.ttl -Y "ip.dst==13.37.13.37"
```
Just iterate over the output of this command and convert each number on each seperate line into ascii. The following python script would do this if the above command output was saved to output.txt.
```
solution = ""
with open("output.txt") as f:
	for line in f.readlines():
		try:
			solution += chr(int(line.strip()))
		except:
			pass

print(t)
```

An alternative solution is to use wireshark as the time to live value is reflected as ASCII in the hex display. If you view the correct packets you will be able to see L followed by T in the next packet and so on untill you reach a closing } and that would give you the flag. This is a solution one of the teams used during Le Tour.
