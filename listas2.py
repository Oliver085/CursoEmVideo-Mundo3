dados = list()
dados.append('Pedro')
dados.append(25)

pessoas = list()
pessoas.append(dados[:])  # Adiciona uma cópia da lista 'dados
dados[0] = 'Maria'
dados[1] = 19

pessoas.append(dados[:])  # Adiciona uma cópia da lista 'dados' novamente

print(pessoas[0][0])  # Saída: Pedro