from jovian.pythondsa import evaluate_test_case, evaluate_test_cases



# Palandrome
# A phrase is a palindrome if, after converting all uppercase letters 
# into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include
# letters and numbers.

# convert to lowercase letters → remove non-alphanumeric characters → reverse

def test_cases():
    tests = []
    tests.append(
        {"input": {"letters": 'naman'}, "output": True}
    )
    tests.append(
        {"input": {"letters": 'pankaj'}, "output": False}
    )
    tests.append(
        {"input": {"letters": ''}, "output": True}
    )
    tests.append(
        {"input": {"letters": 'pankaj0$'}, "output": False}
    )
    tests.append(
        {"input": {"letters": 'pankaj0'}, "output": False}
    )
    tests.append(
        {"input": {"letters": '0naman0'}, "output": True}
    )
    tests.append(
        {"input": {"letters": 'n@m@n'}, "output": True,}
    )
    tests.append(
        {"input": {"letters": 'A man, a plan, a canal: Panama'}, "output": True,}
    )
    return tests

tests = test_cases()

def ispalindrome(letters):
    if len(letters) == 0:
        return True
    else:
        letters = letters.lower()
        letters = ''.join(letter for letter in letters if letter.isalnum())
        print(letters)
        return letters == letters[::-1]
        
evaluate_test_cases(ispalindrome, tests)