# Q1 Write a function to return minimum/maximum in an array. 
# Your program should make the minimum number of comparisons. 
from re import L
from jovian.pythondsa import evaluate_test_case, evaluate_test_cases

def max_self(nums):
    if len(nums) == 0:
        return -1
    else:
        max = 0
        for num in nums:
            if num > max:
                max = num
        return max

def test_cases():
    tests = []
    tests.append(
        {"input": {"nums": [13, 11, 12, 7, 4, 3, 1, 0]}, "output": 13}
    )
    tests.append(
        {"input": {"nums": []}, "output": -1}
    )
    tests.append(
        {"input": {"nums": [0,1,5,6,7,8,10]}, "output": 10}
    )
    tests.append(
        {"input": {"nums": [0,1,5,16,7,18,10]}, "output": 18}
    )
    tests.append(
        {"input": {"nums": [0,0,1,5,5,2,4]}, "output": 5}
    )
    return tests

tests = test_cases()

evaluate_test_cases(max_self, tests)

# Q2 Reverse an array
def reverse_python(nums):
    if len(nums) == 0:
        return -1
    else:
        return nums[::-1]
    
def reverse(nums):
    if len(nums) == 0:
        return -1
    else:
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
    
nums = [i for i in range(1,100000001)]
nums_reverse = [100000000-i for i in range(100000000)]
nums == reverse_python(nums_reverse)


def test_cases_reverse(nums, nums_reverse):
    tests = []
    tests.append(
        {"input": {"nums": nums}, "output": nums_reverse}
    )
    return tests

tests = test_cases_reverse(nums, nums_reverse)

import timeit
start = timeit.timeit()
nums == reverse_python(nums_reverse)
end = timeit.timeit()
print(end - start)

start = timeit.timeit()
nums == reverse(nums_reverse)
end = timeit.timeit()
print(end - start)

# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

def maximum_subarray(nums):
    if len(nums) == 0:
        return -1 
    else:
        max = float('-Inf')
        max_end = float('-Inf')
        for num in nums:
            max_end +=num 
            if max_end > max:
                max = max_end
            if max_end < 0:
                max_end = 0
        return max
            
            
                
             
nums = [-2,1,-3,4,-1,2,1,-5,4]
maximum_subarray(nums)