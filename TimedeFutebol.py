times = 'Flamengo', 'Vasco', 'Fluminense', 'Botafogo', 'Palmeiras', 'Santos', 'Corinthians', 'São Paulo', 'Cruzeiro', 'Atlético-MG', 'Grêmio', 'Internacional', 'Bahia', 'Sport Recife', 'Vitória', 'Ceará SC', 'Fortaleza EC', 'Atlético-PR', 'Coritiba'

primeiros = times[0:5]
print(f'Os cinco primeiros colocados são: {primeiros}')

ultimos = times[-4:]
print(f'Os quatro ultimos colocados sao: {ultimos}')

ordemAZ = sorted(times)
print(f'Os times em ordem alfabética são: {ordemAZ}')

posicao = times.index('Ceará SC') + 1
print(f'O Ceará SC está na {posicao}ª posição')