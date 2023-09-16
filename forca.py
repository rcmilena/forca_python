print("Jogo da forca")
palavra="batata"
resposta=input("Quer jogar?")
if resposta=="s":
    print("escolher tema")
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
    """]
    for item in lista:
        print(item)  
elif resposta=="n":
    print("ok, até mais!")


