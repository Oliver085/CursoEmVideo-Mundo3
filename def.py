def voto():
    idade = int(input("Digite sua idade: "))
    if idade < 16:
        print("Você não pode votar.")
    elif 16 <= idade < 18 or idade >= 70:
        print("O voto é opcional para você.")
    else:
        print("O voto é obrigatório para você.")

voto()