# Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w parametrze jest
# parzysta i zwróci tą informację jako typ logiczny bool ( True / False ). Należy
# uruchomić funkcję, wynik wykonania zapisać do zmiennej, a następnie
# wykorzystując warunek logiczny wyświetlić prawidłowy tekst "Liczba parzysta" /
# "Liczba nieparzysta"

def function(number: int) -> bool:
    if number%2==0:
        return True
    else: 
        return False

result = function(7)
if result == True :
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")