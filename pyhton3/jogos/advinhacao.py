from random import randrange


def ler_record():
    f = open("record.txt", "r")
    conteudo = f.read()
    print(conteudo)


def jogar():
    numero_secreto = randrange(1, 101)
    rodada = 1
    pontos = 1000

    print("*******************************")
    print("Bem Vindo ao jogo de Advinhação")
    print("*******************************")
    print("Record")
    ler_record()
    print("Qual seu apelido?")
    apelido = input("Digite seu apelido:")
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina a dificuldade:"))
    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    # print(numero_secreto)
    for rodada in range(1, tentativas + 1):
        print("Tentativa  {} de  {}".format(rodada, tentativas))
        chute_str = input("Digite um número de  1 a 100:")
        chute = int(chute_str)
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if chute <= 0 | chute > 100:
            print("Número não válido! Escolha um número de 1 a 100.")
            continue
        acertou = chute == numero_secreto
        print("Você digitou: ", chute)
        if acertou:
            print(f"Você acertou! Sua pontuação: {pontos}")
            break
        else:
            if maior:
                print("Você Errou! Seu chute foi acima do número secreto!")
                pontos_perdidos = chute - numero_secreto
                pontos = pontos - pontos_perdidos
                # print(pontos)
                # print(pontos_perdidos)
            elif menor:
                print("Você Errou! Seu chute foi abaixo do número sercreto!")
                pontos_perdidos = numero_secreto - chute
                pontos = pontos - pontos_perdidos
                # print(pontos)
                # print(pontos_perdidos)
    if rodada == tentativas:
        print("Acabaram as tentativas!")
        print("O número secreto era: {}".format(numero_secreto))

    print("Fim do Jogo")

    def salvar_record(x, y, z, k):
        f = open("record.txt", "+a")
        f.write(f"{x} - {y} - {z} - {k} \n")
        f.close()

    if rodada != tentativas:
        salvar_record(apelido, pontos, nivel, rodada)


if __name__ == "__main__":
    jogar()
