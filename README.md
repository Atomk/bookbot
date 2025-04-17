# bookbot

A CLI program that can perform some basic text analysis.

This is the first project of the [Boot.dev](https://www.boot.dev) curriculum.

It follows the course guidelines until commit `2891082`, the following commits are my own additions and corrections.

Developed with VS Code, and WSL to perform all Git commands.

## How to run
- `cd bookbot`
- `python3 main.py <text_file_path>`
    - Path has to be absolute, or relative to `main.py`
    - Should work with any plain-text file (e.g. `.txt`)

## Sample output
Output for Frankenstein, obtained from the [Gutenberg](https://www.gutenberg.org/cache/epub/41445/pg41445.txt) project's website.
```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Word Frequency --------
the: 4192
and: 2832
i: 2655
of: 2627
to: 2038
my: 1660
a: 1357
in: 1120
...11665 more
------ Character Frequency ------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
...60 more
============= END ===============
```