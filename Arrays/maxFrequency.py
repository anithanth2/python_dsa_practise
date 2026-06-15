'''
Longest Repeating Character Replacement
Statement: You're given a string s consisting of uppercase letters, and an integer k.
 You can choose at most k characters in the string and change them to any other uppercase letter.
 Return the length of the longest substring containing the same letter after performing this operation.
pythonExample 1:
Input: s = "ABAB", k = 2
Output: 4
'''


def longestRepeatingChar(s, k):
    frequency = {}
    maxfreq = 0
    res = 0
    left = 0

    for right in range(len(s)):
        char = s[right]
        frequency[char] = frequency.get(char, 0) + 1

        maxfreq = max(maxfreq, frequency[char])

        if right - left + 1 - maxfreq > k:
            frequency[s[left]] -= 1
            left += 1

        res = max(res, right - left + 1)
    return res


print(longestRepeatingChar("AABABBA", 2))



