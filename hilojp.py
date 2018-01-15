# Joguinho do HILO para o meu filho João Pedro
import random

nome = input("Qual é o seu nome? ")

def rodada():
    i = 1
    while i < 8:
        x = input("Tentativa #" + str(i) + ": " )
        if int(x) == numero:
            return 0
        
        elif int(x) > numero:
            print("Atenção. Você chutou muito alto.")
            i += 1
            continue
        elif int(x) < numero:
            print("Atenção. Você chutou muito baixo.")
            i += 1
            continue
    return 1

def jogarDeNovo():
    denovo = input("Gostaria de jogar de novo? (s/n) ")
    while denovo != "s" and denovo!= "n":
        denovo = input("Gostaria de jogar de novo? (s/n) ")
    return denovo

while True:
    # Preâmbulo
    numero = random.randint(1, 100)
    print("\n")
    print("Olá " + nome + "! Tudo bem? Vamos jogar um joguinho divertido?")
    print("Acabei de pensar em um número entre 1 e 100.")
    print("Será que você consegue adivinhar qual o número que pensei?")
    print("Você tem 7 tentativas. Vamos lá!!")

    # Jogo
    jogo = rodada()
    if jogo == 0:
        print("Parabéns!!! Você acertou!!!")
    elif jogo == 1:
        print("Ah... Foi mal. Você perdeu. O número certo era " + str(numero))

    # Conclusão. Repete ou não?
    conclusao = jogarDeNovo()
    if conclusao == "s":
        print("\n")
        continue
    if conclusao == "n":
        print("Obrigado por jogar.")
        break
