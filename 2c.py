# Utwórz pętlę iterującą po liście zawierającej 10 liczb (rekomendowane
# wykorzystanie funkcji range ), która wyświetla jedynie parzyste elementy.

def onlyEvenNumbers():
    for i in range(10):
        if i%2==0:
            print(i)

onlyEvenNumbers()