from time import sleep
from random import randint

jogarnovamente = "S"
itens = ("Pedra", "Papel", "Tesoura")

while jogarnovamente == "S":
    computador = randint(0, 2)
    print("\nEscolha entre Pedra, Papel ou Tesoura")
    print("[0] PEDRA   [1] PAPEL   [2] TESOURA")
    jogador = int(input("\nDigite sua escolha: "))

    while jogador > 2:
        print("Escolha Inválida")
        jogador = int(input("\nDigite sua escolha novamente: "))

    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO")    

    print("\nJogador escolheu {}".format(itens[jogador]))
    print("Computador escolheu {}\n".format(itens[computador]))
    if computador == 0:  # Computador escolheu Pedra
        if jogador == 0:
            print("Empate")
        elif jogador == 1:
            print("Jogador venceu")
        else:
            print("Computador venceu")

    elif computador == 1:  # Computador escolheu Papel
        if jogador == 0:
            print("Computador venceu")
        elif jogador == 1:
            print("Empate")
        else:
            print("Jogador venceu")

    elif computador == 2:  # Computador escolheu Tesoura
        if jogador == 0:
            print("Jogador venceu")
        elif jogador == 1:
            print("Computador venceu")
        else:
            print("Empate")

    jogarnovamente = (input("\nDeseja jogar novamente S/N: ")).upper()
print("FIM DE JOGO !!!")
