# Given an array of integers nums and an integer target,
# return the indices of two numbers whose sum is equal to target.
# nums = [2, 7, 11, 15]
# target = 9
#
# # Output:
# [0, 1]

#TimeComplexity: O(n²), Space Complexity: O(1)
from typing import List
def two_sum(nums: List[int], target):
    result = []
    for i in range (len(nums) - 1):
        for j in range (i+1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
    return result

# TimeComplexity: O(n)

from typing import List
def tw_sum(nums: List[int], target):
    dic = {}
    for i in range(len(nums)):
        number_need = target - nums[i]
        if number_need in dic:
            return [dic[number_need], i]

        dic[nums[i]] = i


nums = [2, 7, 11, 15]

print(tw_sum(nums,9))




















def two_s(nums: List[int], target):
    seen = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in seen:
            [seen[needed],i]
            print(needed)
        else:
            seen[num] = i
    print(seen)


nums = [2, 7, 11, 15]

print(two_s(nums,9))


