'''
Given a string s, find the length of the longest substring without repeating characters.
pythonExample 1:
Input: s = "abcabcbb"
Output: 3
# "abc" has length 3
'''


def longestSubstring(s):
    charset = set()
    left, minlen = 0, 0

    for right, char in enumerate(s):
        while char in charset:
            charset.remove(s[left])
            left = left + 1
        charset.add(char)
        minlen = max(minlen, right - left + 1)

    return minlen


print(longestSubstring("abcabcbb"))
print(longestSubstring("bbbbb"))
print(longestSubstring("pwwkew"))
