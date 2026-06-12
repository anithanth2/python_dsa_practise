'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise. An anagram is a word formed by rearranging the letters of another, using all the original letters exactly once.
pythonExample 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

from collections import Counter


def validAnagram(string, other):
    return Counter(string) == Counter(other)


print(validAnagram("anagram", "nagaram"))
print(validAnagram("rat", "car"))


