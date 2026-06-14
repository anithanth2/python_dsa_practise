'''
Given an integer array nums, find the contiguous subarray which has the largest sum and return its sum.
'''

def maxSubArray(nums):
    res = nums[0]

    maxSubresult = nums[0]

    for i in range(1, len(nums)):
        maxSubresult = max(maxSubresult + nums[i], nums[i])
        res = max (res, maxSubresult)

    return res


print(maxSubArray([2, 3, -8, 7, -1, 2, 3]))