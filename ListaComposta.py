idade = []
peso = []
nome = []

while True:
    nome.append(input('Nome: '))
    idade.append(int(input('Idade: ')))
    peso.append(float(input('Peso: ')))
    resp = input('Quer continuar? [S/N] ')
    if resp.strip().upper().startswith('N'):
        break

menor = min(peso)
maior = max(peso)

mais_leves = []
mais_pesadas = []

for i in range(len(peso)):
    if peso[i] == menor:
        mais_leves.append(nome[i])
    if peso[i] == maior:
        mais_pesadas.append(nome[i])

print(f'Foram cadastradas {len(nome)} pessoas.')
print(f'O menor peso foi {menor}kg. Peso de: {mais_leves}')
print(f'O maior peso foi {maior}kg. Peso de: {mais_pesadas}')