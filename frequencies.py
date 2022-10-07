"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for letter in items:
        if frequencies.get(letter):
            newFrequency = frequencies.get(letter) + 1
            frequencies.update({f'{letter}':newFrequency})
        else:
            frequencies.update({f'{letter}':1})
    return frequencies
