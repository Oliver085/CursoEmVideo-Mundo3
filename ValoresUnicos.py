valor = int(input('Digite um valor: '))
lista = [valor]
if valor in lista:
    print('Valor duplicado! Nao vou adicionar...')
else:
    lista.append(valor)
    print('Valor adicionado com sucesso...')
print('-='*30) 
print(f'Os valores digitados foram {sorted(lista)}')