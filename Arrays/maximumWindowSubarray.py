'''
Given two strings s and t, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If no such window exists, return "".
pythonExample 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
'''


def maximumWindow(s, t):
    if t == "": return ""

    charT, window = {}, {}
    have, need = 0, len(charT)
    left = 0
    res, reslen = [-1, -1], float('inf')

    for c in t:
        charT[c] = 1 + charT.get(c, 0)

    for right in range(len(s)):
        window[s[right]] = 1 + window.get(s[right], 0)

        if s[right] in charT and window[s[right]] == charT[s[right]]:
            have += 1

        while have == need:

            if (right - left + 1) < reslen:
                res = [left, right]
                reslen = right - left + 1

            window[s[left]] -= 1
            if s[left] in charT and window[s[left]] < charT[s[left]]:
                have -= 1
            left += 1

        l, r = res
    return s[l:r+1] if reslen != float('inf') else ""


print(maximumWindow("ADOBECODEBANC", "ABC"))


