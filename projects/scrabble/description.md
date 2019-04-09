# Scrabble helper

Create a web app with the following functionality:

1. Take 7 letters as input and generate all possible dictionary (american/british) words from those letters

    * Wildcard \* should be acceptable
    * **Nothing found** is a valid result

2. Words should be ordered by the total word value

    * Bonus **+10%** if you can make the table sortable by either column

3. If specified by the user, the generated words must contain the provided existing letter(s)

    * *Existing letter(s)* field should stay disabled until *Attach to existing* option is checked

4. Your application must not be slow

![Scrabble](scrabble.png)

## Dictionaries

* American English

```bash
/usr/share/dict/american-english
```

* British English

```bash
/usr/share/dict/british-english
```

## Grading

1. Proper form elements
2. Generate permutations of letters
3. *Not found* is handled correctly
4. Existing letters are used properly
5. Both dictionaries are used
6. Wildcards are processed
7. Word value is calculated properly (WC = 0)
8. Table is generated and sorted
9. Everything works
10. Efficiency

## References

* [Scrabble - Wikipedia](https://en.wikipedia.org/wiki/Scrabble)

* [Scrabble letter distributions - Wikipedia](https://en.wikipedia.org/wiki/Scrabble_letter_distributions)
