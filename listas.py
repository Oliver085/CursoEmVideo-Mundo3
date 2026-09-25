#Listas ficam em colchetes [] e sao mutaveis, ou seja, podem ser alteradas
#Tuplas ficam em parenteses () nao sao mutaveis, ou seja, nao podem ser alteradas
#.append() adiciona um elemento no final da lista
#.insert() adiciona um elemento em uma posicao especifica da lista
#del remove um elemento de uma posicao especifica da lista
#pop remove o ultimo elemento da lista, mas pode remover um elemento de uma posicao especifica da lista
#.remove() remove um elemento especifico da lista
#sorted() coloca os elementos da lista em ordem alfabetica ou numerica, mas nao altera a lista original
#len() retorna a quantidade de elementos da lista

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: '))) 
for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}...')
