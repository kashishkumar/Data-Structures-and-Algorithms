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
        {"input": {"cards": [13, 11, 12, 13, 4, 13, 1, 0], "query": 13}, "output": [0,3,5]}
    )
    return tests
tests = test_cases()
    
def locate_cards(cards,query):
    indices=[]
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
