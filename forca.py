print("Jogo da forca")
palavra="batata"
tracinhos = "_ " * len(palavra)
resposta=input("Quer jogar?")
if resposta=="s":
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
    print(lista[0]) 
    print(tracinhos)
while true:
     print("tracinhos".join(palavra))
        letra = input("Digite uma letra: ")

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            forca += 1
            print(f"Errou! Forca: {forca}")
    
        
  
elif resposta=="n":
    print("ok, até mais!")


