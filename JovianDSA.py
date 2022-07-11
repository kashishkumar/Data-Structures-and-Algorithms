from jovian.pythondsa import evaluate_test_case, evaluate_test_cases
import jovian

# Linear Search
def test_cases():
    tests = []
    tests.append(
        {"input": {"cards": [13, 11, 12, 7, 4, 3, 1, 0], "query": 7}, "output": [3]}
    )
    tests.append(
        {"input": {"cards": [13, 11, 12, 7, 4, 3, 1, 0], "query": 13}, "output": [0]}
    )
    tests.append(
        {"input": {"cards": [13, 11, 12, 7, 4, 3, 1, 0], "query": 0}, "output": [7]}
    )
    tests.append({"input": {"cards": [13], "query": 13}, "output": [0]})
    tests.append(
        {"input": {"cards": [13, 11, 12, 7, 4, 3, 1, 0], "query": 19}, "output": [-1]}
    )
    tests.append({"input": {"cards": [], "query": 7}, "output": [-1]})
    tests.append(
        {
            "input": {"cards": [13, 11, 12, 13, 4, 13, 1, 0], "query": 13},
            "output": [0, 3, 5],
        }
    )
    return tests


tests = test_cases()


def locate_cards(cards, query):
    indices = []
    if query in cards:
        for index, card in enumerate(cards):
            if query == card:
                indices.append(index)
    else:
        indices.append(-1)
    return indices


evaluate_test_cases(locate_cards, tests)
evaluate_test_case(locate_cards, tests[-1])

# Binary Search
def test_cases_b():
    tests = []
    tests.append(
        {"input": {"cards": [0, 1, 3, 4, 7, 11, 12, 13], "query": 7}, "output": 4}
    )
    tests.append(
        {"input": {"cards": [0, 1, 3, 4, 7, 11, 12, 13], "query": 13}, "output": 7}
    )
    tests.append(
        {"input": {"cards": [0, 1, 3, 4, 7, 11, 12, 13], "query": 0}, "output": 0}
    )
    tests.append({"input": {"cards": [13], "query": 13}, "output": 0})
    tests.append(
        {"input": {"cards": [0, 1, 3, 4, 7, 11, 12, 13], "query": 19}, "output": -1}
    )
    tests.append({"input": {"cards": [], "query": 7}, "output": -1})
    tests.append(
        {"input": {"cards": [0, 1, 4, 7, 7, 7, 9, 10], "query": 7}, "output": 3}
    )
    return tests


tests_b = test_cases_b()


def verify_middle(cards, query, middle):
    if cards[middle] == query:
        if cards[middle - 1] == query and middle - 1 >= 0:
            return "left"
        else:
            return "found"
    elif cards[middle] < query:
        return "left"
    elif cards[middle] > query:
        return "right"


def locate_cards_b(cards, query):
    if len(cards) == 0:
        return -1
    else:
        left, right = 0, len(cards) - 1
        while left <= right:
            middle = (left + right) // 2
            ismiddle = verify_middle(cards, query, middle)
            if ismiddle == "found":
                return middle
                break
            elif ismiddle == "left":
                left = middle + 1
            else:
                right = middle - 1
        return -1


evaluate_test_cases(locate_cards_b, tests_b)

# Rotate arrays


def count_rotations(nums):
    if len(nums) == 0:
        return -1
    else:
        return locate_cards_b(nums, min(nums))


def test_cases_rotate_array():
    tests = []
    tests.append({"input": {"nums": [5, 6, 9, 0, 2, 3, 4]}, "output": 3})
    tests.append({"input": {"nums": [7, 8, 1, 2, 3, 4, 5]}, "output": 2})
    tests.append({"input": {"nums": [5, 7, 8, 9, 1, 3, 4]}, "output": 4})
    tests.append({"input": {"nums": [0, 2, 3, 4]}, "output": 0})
    tests.append({"input": {"nums": []}, "output": -1})
    return tests


tests_rotate = test_cases_rotate_array()

evaluate_test_cases(count_rotations, tests_rotate)

# complexity is linear and so need to find a different solution
# Using binary search approach to find the rotation point
def count_rotations_b(nums):
    if len(nums) == 0:
        return -1
    else:
        left, right = 0, len(nums) - 1
        middle = left + right // 2
        if middle == 0:
            return 0
        else:
            while nums[middle] > nums[middle - 1]:
                middle = left + right // 2
                if middle == 0:
                    return 0
            return middle

def count_rotations_binary(nums):
    if len(nums) == 0:
        return -1
    else:
        left = 0 
        right = len(nums) - 1
        middle = left + right // 2
        while middle > 0 and nums[middle] > nums[middle - 1]:
            print("left: {} ".format(left), "middle: {}".format(middle), "right: {} ".format(right))
            if nums[middle] > right:
                left = middle + 1
            else:
                right = middle - 1
            middle = left + right//2
        return middle

evaluate_test_case(count_rotations_binary, tests_rotate[2])
