from jovian.pythondsa import evaluate_test_case, evaluate_test_cases
# 1. Given an integer array nums, return true if any value appears at 
# least twice in the array, and return false if every element is distinct.
def test_cases():
    tests = []
    tests.append(
        {"input": {"nums": [1,2,3,4,5,6,7,8,9]}, "output": False }
    )
    tests.append(
        {"input": {"nums": []}, "output": False}
    )
    tests.append(
        {"input": {"nums": [1,1,1]}, "output": True}
    )
    tests.append(
        {"input": {"nums": [1,3,4,4,2]}, "output": True}
    )
    return tests
tests = test_cases()
def duplicate_array(nums):
    nums_set= set()
    for num in nums:
        if num in nums_set:
            return True
        nums_set.add(num)
    return False  
evaluate_test_cases(duplicate_array, tests)

# 2. Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word 
# or phrase, typically using all the original letters exactly once.

def isanagram(s, t):
    pass

def test_cases():
    tests

