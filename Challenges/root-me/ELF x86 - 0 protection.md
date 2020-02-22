# Solution

## Using Ghidra
Loading the binary into Ghidra allows you to review the program structure by opening the Function Graph (Windows -> Function Graph).

![Function Graph](https://user-images.githubusercontent.com/32277825/75081241-7e7ed100-54dc-11ea-8104-876b5bffb2ae.PNG)

We can see that the overall program is very simple, main function has a conditional and then exits.

So taking a look at what causes each condition to trigger, in this case there is a strcmp function for the string you enter compared against ``123456789``. That's the password sitting right there, we can validate by translating the messages.

![Code Overview](https://user-images.githubusercontent.com/32277825/75081448-3ad89700-54dd-11ea-91a3-b4223c644e69.PNG)

## If True
```
"Bien joue, vous pouvez valider l\'epreuve avec le pass : %s!\n"
"Well done, you can validate the test with the pass:% s! \ N"
```
## If False
```
"Dommage, essaye encore une fois."
"Too bad, try again."
```
