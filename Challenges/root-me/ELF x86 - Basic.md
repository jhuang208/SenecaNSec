# Solution

## Using Ghidra
Loading the binary into Ghidra allows you to review the program structure by opening the Function Graph (Windows -> Function Graph).

![Function Graph](https://user-images.githubusercontent.com/32277825/75082067-e84caa00-54df-11ea-93e4-52c03e90b113.PNG)

This time the program has more going on compared to the first binary, might be unclear from the picture but there is 3 conditionals going on so let's start with the dead end looking path.

![Bad Username](https://user-images.githubusercontent.com/32277825/75082331-0cf55180-54e1-11ea-910d-c0c51e5402f8.PNG)

Full string is ``Bad username``, so it looks for a username input, and likely a password. So review the main() function.

![Username](https://user-images.githubusercontent.com/32277825/75082477-c5bb9080-54e1-11ea-80e7-0275d6b14810.PNG)


![strcmp John](https://user-images.githubusercontent.com/32277825/75082598-614d0100-54e2-11ea-9f64-3e45c561b161.PNG)



