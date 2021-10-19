# Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych
# liczb, każdy jej element pomnoży przez 2, a na końcu ją zwróci. Zadanie
# należy wykonać w 2 wersjach:
# i. Wykorzystując pętle for .
# ii. Wykorzystując listę skłądaną.

def inreaseNumbers(numbers):
    numbersIncreased = [(number*2) for number in numbers]
    print(numbersIncreased)

def inreaseNumbersNested(numbers):
    numbersIncreased = []
    for number in numbers:
        numbersIncreased.append((number*2))
    print(numbersIncreased)

numbers = [1,2,3,4,5]
inreaseNumbers(numbers)
inreaseNumbersNested(numbers)