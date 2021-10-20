# Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu list .
# Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć duplikaty, każdy
# element podnieść do potęgi 3 stopnia, a następnie zwrócić powstałą listę.

def function(x: list, y:list) -> list:
    tempList = []
    for i in list(set(x+y)):
        tempList.append(i**3)
    return tempList

result = function([1,2,3],[2,3,4])
print(result)