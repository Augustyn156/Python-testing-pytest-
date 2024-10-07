#write a function that returns number of vowels from a string
import pytest
def num_vowels(string):
    vowels=['a','e','i','o','u','ą','ę','ó']
    count=0
    for letter in string.lower():
        if letter in vowels:
            count+=1
    return count

def test_upper():
    assert num_vowels('GOOGOO GAGA')==6

def test_polish_vowels():
    assert num_vowels('ąęó')==3

def test_empty():
    assert num_vowels("")==0

def test_no_vowels():
    assert num_vowels('swfrth')==0