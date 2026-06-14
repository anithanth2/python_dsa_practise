'''
Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
such that i != j != k and nums[i] + nums[j] + nums[k] == 0. The solution set must not contain duplicate triplets.
pythonExample:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''


def calculate3Sum(nums):
    res = []
    nums.sort()

    for i in range(len(nums)):
        if i>0 and (nums[i] == nums[i-1]):
            continue
        j = i + 1
        k = len(nums) - 1

        while j < k:
            targetsum = nums[i] + nums[j] + nums[k]
            if targetsum < 0:
                j = j+1
            elif targetsum > 0:
                k = k-1
            else:
                res.append([nums[i],nums[j],nums[k]])
                j = j + 1
                while j < k and (nums[j] == nums[j-1]):
                    j = j + 1

    return res


print(calculate3Sum([-1,0,1,2,-1,-4]))