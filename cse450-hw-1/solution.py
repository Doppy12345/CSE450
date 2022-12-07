import re

def question01(line):
    # Write a python program that takes a line of text and outputs it prefixed by the number of characters in that line.
    # See test case for output format.
    charCount = len(line.strip())
    return f"{charCount}: {line}"

def question02(sentence):
    # For a sentence, return a set of words (whitespace delimited strings).
    # If a digit (0-9) occurs in the sentence raise an exception.
    digit_re = r'[0-9]'
    word_re = r'\w+,*'
    if(re.search(digit_re, sentence) != None):
        raise Exception
      
    return set(re.findall(word_re, sentence))

