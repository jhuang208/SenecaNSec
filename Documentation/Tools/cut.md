# Cut

# Syntax
```
cut OPTION [FILE]\
-d, --delimiter=DELIM -  Sets a custom deliminter (Default TAB)
-f, --fields=LIST - Select only these fields determined by the delimiter
```

# Use case
## Getting the flag string hardcodded in a string. E.g. PicoCTF 2019 VaultDoor1
```
password.charAt(0)  == 'd' &&
password.charAt(29) == '7' &&
password.charAt(4)  == 'r' &&

cat temp | cut -d'(' -f2 | sort -n | cut -d"'" -f2 | tr -d "\n" ; echo
```
