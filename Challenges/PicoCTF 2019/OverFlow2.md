Solution:
   
   When we examine the source code, we see that this program is similar with the program in OverFlow1. The differences between them
   are we have to not only push the return address to vuln() function but also push two arguments at the bottom of the stack which
   are 0xDEADBEEF string and 0xC0DED00D as arg1 and arg2.
   
   To do this, we have to know where is the location of the return address to overwrite it.
   After examine the program, we know that when we write the return address up to 44 times, it will give us segmentation fault
   (To get the return address, we can use the same command from OverFlow1 which is "readelf -a vuln | grep flag")
   So, we will write the return address first, then the arguments, the command should look like this: 

    perl -e 'print "\xe6\x85\x04\x08"x52 . "\xEF\xBE\xAD\xDE" . "\x0D\xD0\xDE\xC0"' | ./vuln
   
   Because of little-endian, we have to write each byte backward and because of 2 arguments have 8 bytes in them, so we have to write 8 more bytes from the return address. But in fact, we just need to write more than 52 times, it still works but remember to choose a multiple of four number because they are chunks of 4 bytes.
   
   Notice: When we use "." to seperate what we print, remember to put space before and after the ".".
   
   ![image](https://user-images.githubusercontent.com/60718485/75126273-2801c600-5687-11ea-998b-d691fd13f5a8.png)
