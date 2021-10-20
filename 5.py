# Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi typu int
# . Funkcja ma sprawdzić, czy lista z parametru pierwszego zawiera taką wartość
# jaką przekazano w parametrze drugim.

def function(list: list, int:int):
    if int in list:
        return True
    else:
        return False

result = function([1,2,3],4)
print(result)