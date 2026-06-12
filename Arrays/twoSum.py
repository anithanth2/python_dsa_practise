'''
Statement: Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target. Each input has exactly one solution, and you may not use the same element twice.
pythonExample:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]  # because nums[0] + nums[1] = 2 + 7 = 9
'''


def twoSum(nums, target):
    reference = dict()
    for i, num in enumerate(nums):
        diff = target - num
        if diff in reference:
            return [reference[diff], i]
        reference[num] = i


print(twoSum([2, 7, 11, 15], 9))
