# Variants
grep, egrep (Extended GREP), fgrep (Fixed GREP), pgrep (Process GREP), rgrep (Recursive GREP), etc

* egrep | grep -e\
In case of egrep, even if you do not escape the meta-characters, it would treat them as special characters and substitute them for their special meaning instead of treating them as part of string.

* fgrep | grep -f \
Fgrep searches for complete string and doesn’t even recognize special characters as part of regular expression even if escaped or not escaped.


# Some Special Meta-Characters of grep
> \+ – Equivalent to one or more occurrences of previous character.\
? – This denotes almost 1 repetition of previous character. Like: a? Would match ‘a’ or ‘aa’\
( – Start of alternation expression.\
) – End of alternation expression.\
| – Matching either of the expression separated by '|'. Like: “(a|b)cde” would match either ‘abcde’ or ‘bbcde’.\
{ – This meta-character indicates start of range specifier. Like: “a{2}” matches “aa” in file i.e. a 2 times.\
} – This meta-character indicates end of range specifier.
