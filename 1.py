# Stworzyć funkcję, która przyjmuje 2 argumenty (typu string ) name i surname , a
# następnie zwróci stringa zgodnie ze wzorem Cześć {name} {surname}! Należy
# uruchomić funkcję, wynik wykonania funkcji zapisać do zmiennej, a następnie go
# wyświetlić ( print )

def function(name: str, surname: str) -> str:
    return("Cześć %s %s!" % (name,surname)) 

result = function("Dawid", "Badura")
print(result)