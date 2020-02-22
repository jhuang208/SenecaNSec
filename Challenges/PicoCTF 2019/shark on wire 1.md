# Solution

#Process
Searching for Pico/PicoCTF/CTF using Wireshark search functionality. Using Packet bytes, Strings and searching Pico we find the following. 

![wireshark1](https://user-images.githubusercontent.com/32277825/75100235-1a6e1280-5599-11ea-9c97-91f7ea678486.png)

The hint provided points you towards streams. ``What are streams?``

Searching around we find stream 6 and 7 both contain a flag under the format picoCTF{}.

![wireshark](https://user-images.githubusercontent.com/32277825/75100206-d0852c80-5598-11ea-8718-c8cd2ce6e3bb.png)


```picoCTF{StaT31355_636f6e6e}```
