numeros = list()

def sorteia():
    from random import randint
    for c in range(0, 5):
        n = randint(1, 100)
        numeros.append(n)


def somapar():
    s = sum(numeros)
    print(f"A soma dos valores sorteados é {s}")

print("Sorteando 5 valores da lista: ", end="")
sorteia()
print(numeros)
somapar()
print("Fim do programa!")
