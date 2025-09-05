# BLACKJACK
import random
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

fim_de_jogo = {
    "empate": "Houve empate!",
    "ganhou": "Você ganhou!",
    "perdeu": "Você perdeu...",
    "blackjack mesa": "Mesa conseguiu Blackjack, você perdeu...",
    "blackjack jogador": "Você venceu com Blackjack!",
}

def dar_carta():
    return random.choice(cartas)

def calcular_total(mao):
    total = sum(mao)
    while total > 21 and 11 in mao:
        mao[mao.index(11)] = 1
        total = sum(mao)
    return total

def mostrar_maos(jogador, mesa, final=False):
    print(f"\tSeu jogo: {jogador}, soma: {calcular_total(jogador)}")
    if final:
        print(f"\tMesa: {mesa}, soma: {calcular_total(mesa)}")
    else:
        print(f"\tMesa: [{mesa[0]}, ?]")

def comparar_cartas(jogador, mesa, cartas_jogador, cartas_mesa):
    if jogador == mesa:
        return fim_de_jogo["empate"]
    elif jogador == 21 and len(cartas_jogador) == 2:
       return fim_de_jogo["blackjack jogador"]
    elif mesa == 21 and len(cartas_mesa) == 2:
        return fim_de_jogo["blackjack mesa"]
    elif jogador > 21:
        return fim_de_jogo["perdeu"]
    elif mesa > 21:
        return fim_de_jogo["ganhou"]
    elif jogador > mesa:
        return fim_de_jogo["ganhou"]
    else: # mesa > jogador
        return fim_de_jogo["perdeu"]

while True:
    clear_terminal()
    cartas_jogador = [dar_carta(), dar_carta()]
    cartas_mesa = [dar_carta(), dar_carta()]

    total_jogador = calcular_total(cartas_jogador)
    total_mesa = calcular_total(cartas_mesa)

    mostrar_maos(cartas_jogador, cartas_mesa)

    # Jogador compra cartas
    while total_jogador < 21:
        if input("\nDeseja pedir mais uma carta? 's' ou 'n': ").lower() == 's':
            cartas_jogador.append(dar_carta())
            total_jogador = calcular_total(cartas_jogador)
            mostrar_maos(cartas_jogador, cartas_mesa)
        else:
            break

    # Mesa compra cartas
    while total_mesa < 17:
        cartas_mesa.append(dar_carta())
        total_mesa = calcular_total(cartas_mesa)

    print("\nResultado final: " + comparar_cartas(total_jogador, total_mesa, cartas_jogador, cartas_mesa))
    mostrar_maos(cartas_jogador, cartas_mesa, final=True)

    if input("\nQuer jogar novamente? 's' ou 'n': ").lower() == 'n':
        break