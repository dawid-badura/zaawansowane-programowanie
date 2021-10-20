# Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma dwóch
# pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę informację
# jako typ logiczny bool

def function(x: int, y:int, z:int) -> bool:
    if (x+y)>=z:
        return True
    else: 
        return False

result = function(1,1,3)
print(result)