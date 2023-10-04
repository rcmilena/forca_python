print("Jogo da forca")
palavra="batata"
tracinhos = "_ " * len(palavra)
lista = ["""
+---+
|   |
    |
    |
    |
    |
=======
""",
"""
+---+
|   |
O   |
    |
    |
    |
=========
""",
"""
+---+
|   |
O   |
|   |
    |
    |
=========
""",
"""
+---+
|   |
O   |
/|   |
    |
    |
=========
""",
"""
 +---+
 |   |
 O   |
/|\  |
    |
    |
=========
""",
"""
+---+
|   |
O   |
/|\  |
/    |
    |
=========
""",
"""
+---+
|   |
O   |
/|\  |
/ \  |
    |
=========
"""]
resposta=input("Quer jogar? ")
if resposta=="s":
    print(lista[0]) 
    print(tracinhos)
    vida = 7
    while vida > 0:
        acertou = False
        escolha = input("escolha uma letra: ")
        novo_tracinhos = ''
        for i in range(len(palavra)):
            if palavra[i] == escolha:  
                novo_tracinhos += escolha
                acertou = True
            else:
                novo_tracinhos += tracinhos[i]
        tracinhos = novo_tracinhos
        if acertou:
            print(tracinhos)
            if tracinhos == palavra:
                print("Parabéns, você ganhou!")
                break
        else:
            print("Você errou, menos uma vida.")
            vida = vida - 1
            print(lista[7-vida])
    while 
elif resposta == "n":
    print("tchau")