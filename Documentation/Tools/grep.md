
# Flags
> -c - counts number of matches without printing\
-i - search case insensitive\
-n - print the number of lines before each match\
-v - prints the complement of the regular expression\
-l - print file names with lines that match the expression\
-r - recursively searches files

# Some Special Meta-Characters of grep
> \+ – Equivalent to one or more occurrences of previous character.\
? – This denotes almost 1 repetition of previous character. Like: a? Would match ‘a’ or ‘aa’\
( – Start of alternation expression.\
) – End of alternation expression.\
| – Matching either of the expression separated by '|'. Like: “(a|b)cde” would match either ‘abcde’ or ‘bbcde’.\
{ – This meta-character indicates start of range specifier. Like: “a{2}” matches “aa” in file i.e. a 2 times.\
} – This meta-character indicates end of range specifier.

# egrep | Extended GREP | grep -E
Treats the pattern as a regular expression, see above for meta characters.

In case of egrep, even if you do not escape the meta-characters, it would treat them as special characters and substitute them for their special meaning instead of treating them as part of string.

# fgrep | Fixed-string GREP | grep -F
Is fixed or fast grep and behaves as grep but does NOT recognize any regular expression meta-characters as being special. The search will complete faster because it only processes a simple string rather than a complex pattern.

# pgrep | Process-ID GREP
pgrep looks through the currently running processes and lists the process IDs which matches the selection criteria to stdout.
Returns process ID of a process from the name.
