# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = word.split(" ")
    word = "".join(word)
    anagram = anagram.split(" ")
    anagram = "".join(anagram)
    if(len(word) == len(anagram)):
        sorted_words = sorted(word)
        sorted_anagram = sorted(anagram)
        if(sorted_words == sorted_anagram):
            return True
        else:
            return False
    else:
        return False
