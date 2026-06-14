'''
nums = [1,2,3,4]
Output: [24,12,8,6]
'''


def productOfArrayItself(nums):
    n = len(nums)
    result = [1] * len(nums)

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix = prefix * nums[i]

    suffix = 1
    for i in range(n-1, -1, -1):
        result[i] = result[i] * suffix
        suffix = suffix * nums[i]

    return result




print(productOfArrayItself([1,2,3,4]))
