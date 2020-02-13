# Strings
A basic file analysis step typically involves looking for any readible strings that exist in the binary/executable. This can be done with strings in Unix or Sysinternals Strings on Windows.

Download Link: https://docs.microsoft.com/en-us/sysinternals/downloads/strings

# Syntax
```
strings [OPTIONS] FILENAME\
-n - Set custom character length (default 4)\
-t [o | x | d] - Print offset before printing string. **O**ctal | he**x**adecimal | **d**ecimal\
-a | --all - Scan the whole file; do not scan only the initialized and loaded sections of object files.\
-s - Change default delimiter from new line to specified string.
```

# Use case
```
strings FILENAME | grep STRING
```
