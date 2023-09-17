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
        
  
elif resposta=="n":
    print("ok, até mais!")


