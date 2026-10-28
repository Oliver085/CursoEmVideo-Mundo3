import moeda

n = int(input("Digite um valor: R$ "))
print(f"Aumentando 10% de {n}, temos R$ {moeda.aumentar(n)}")
print(f"Diminuindo 10% de {n}, temos R$ {moeda.diminuir(n)}")
print(f"O dobro de {n} é R$ {moeda.dobro(n)}")
print(f"A metade de {n} é R$ {moeda.metade(n)}")