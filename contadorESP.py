def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    for c in range(i, f + 1, p):
        print(f"{c} ", end="")
    print("FIM!")

contador(1, 10, 2)

