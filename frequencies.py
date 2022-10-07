"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for letter in items:
        strLetter = f'{letter}'
        if frequencies.get(strLetter):
            print(letter)
            newFrequency = frequencies.get(strLetter) + 1
            frequencies.update({strLetter:newFrequency})
            print(frequencies)
        else:
            print(letter)
            frequencies.update({strLetter:1})
            print(frequencies)
    print(frequencies)
    return frequencies
