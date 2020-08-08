# Description
Find the least common 2-letter substring in the English language

# Motivation
To find the best key mapping in vim to escape insert mode, without having to reach for the `esc` key.\
Ideally, the substring would be entirely on the home row of a QWERTY keyboard and quick to type, consisting of a combination of letters that are rarely typed in the English language (to avoid accidentally exiting insert mode while typing text). Additionally, this combination shouldn't be destructive if accidentally pressed in normal mode. Common wisdom suggests that one good keymapping to `esc` might be `jk` but is this true?

# Requirements
* Python 3

# Assorted Findings
The least common 2-letter substrings present in the English language (i.e. they are found at least once in the English dictionary) are: 'qx', 'qg', 'mx', 'qf', 'qm', 'gq', 'kx', 'qy', 'kq', 'xz', 'vh', 'pz', 'jv', 'px', and 'vb'.\
The most common 2-letter substring present in the English language is: 'er'.\
Restricting to substrings that are found entirely on the home row of a QWERTY keyboard, the five least common substrings (among substrings that were found) were: 'jl', 'js', 'jk', 'jj' and 'fj'.\
After generating all 2-letter subtring permutations from characters from the home row (i.e. 'asdfjkl', ignoring the semicolon character), and comparing them with the substrings that were found, there was only one 2-letter substring that never appeared in the English dictionary: 'jf'.

# Conclusion
These results can be validated and expanded by searching through the dictionary, to check if the words that these substrings are found in, are also words that you would commonly type.\
For example, grepping through the dictionary, the substring 'jk' is found in four words: 'pirojki', 'rijksdaalder', 'rijksdaaler', 'satlijk'. It's also found in names like 'Rijksmuseum' or 'Rijkaard'.

Based on the [criteria mentioned](#Motivation), `jf` is possibly the best candidate because it is rarely typed (since it was not found in the English dictionary), is on the home row, and does not have any destructive effects in normal mode with the standard key bindings. Additionally, `jf` resets the index fingers to the "correct" position on the home row. 

The results confirm that `jk` is also a good key mapping, but it does appear to be used slightly more commonly than `jf`.

Conclusion: `jf` might be the best remapping for the `esc` key in vim. As a result, I have added the line `inoremap jf <Esc>` to my `.vimrc`.

# Caveat
The dictionary used for this analysis does not have any notion of frequency, so some substrings may be typed more often even though they appear in fewer words.

# Disclaimer
This project was done more so out of curiousity about the English language than anything else. Use this information at your own peril.
