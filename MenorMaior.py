lista = [int(input('Digite um valor: ')) for cont in range(0, 5)]
print(f'O maior valor digitado foi {max(lista)}')
print(f'O menor valor digitado foi {min(lista)}')
for c,v in enumerate(lista):
    if v == max(lista):
        print(f'O maior valor digitado foi {v} na posicao {c}')
    if v == min(lista):
        print(f'O menor valor digitado foi {v} na posicao {c}')
