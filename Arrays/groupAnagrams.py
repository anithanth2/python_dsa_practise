'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
pythonExample:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

from collections import defaultdict


def groupAnagrams(strs):
    groupAnagramsDict = {}
    for s in strs:
        key = ''.join(sorted(s))
        try:
            groupAnagramsDict[key].append(s)
        except KeyError:
            groupAnagramsDict[key] = [s]

    return list(groupAnagramsDict.values())


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

