'''
Given an array height where height[i] represents the height of a vertical line at position i, find two lines that,
together with the x-axis, form a container that holds the maximum amount of water. Return that max area.
pythonExample:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
'''

def maxArea(height):
    left,right = 0, len(height) - 1
    maxArea = float('-inf')

    while left < right:
        maxArea = max((right - left) * min(height[left], height[right]), maxArea)
        if height[left] <= height[right]:
            left = left + 1
        else:
            right = right - 1

    return maxArea


print(maxArea([1,8,6,2,5,4,8,3,7]))
