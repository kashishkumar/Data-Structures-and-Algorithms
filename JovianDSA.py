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
def test_cases_b():
    tests = []
    tests.append(
        {"input": {"cards": [0, 1, 3, 4, 7, 11, 12, 13], "query": 7}, "output": 3}
    )
    tests.append(
        {"input": {"cards": [0, 1, 3, 4, 7, 11, 12, 13], "query": 13}, "output": 0}
    )
    tests.append(
        {"input": {"cards": [0, 1, 3, 4, 7, 11, 12, 13], "query": 0}, "output": 7}
    )
    tests.append({"input": {"cards": [13], "query": 13}, "output": [0]})
    tests.append(
        {"input": {"cards": [0, 1, 3, 4, 7, 11, 12, 13], "query": 19}, "output": -1}
    )
    tests.append({"input": {"cards": [], "query": 7}, "output": [-1]})
    return tests
tests_b = test_cases_b()

def locate_cards_b(cards, query):
    if len(cards) == 0:
        return -1
    else:
        left, right = 0, len(cards)-1 
        middle = (left + right)//2
        while cards[middle] != query:
            if cards[middle] > query:
                right = middle - 1    
            elif cards[middle] < query:
                left = middle+1
            else:
                
            middle = (left + right)//2
        return middle
    
        
evaluate_test_case(locate_cards_b, tests_b[0])