import random

def jogar():
    print("*******************************")
    print("Bem Vindo ao jogo de Forca")
    print("*******************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    palavra_secreta = palavras[random.randrange(1, len(palavras))]
    enforcou = False
    acertou = False
    palavra_secreta_list = list(palavra_secreta)
    palavra_tentativa = ["_" for x in palavra_secreta]
    tentativas = 6

    print(f"A palavra secreta tem {len(palavra_tentativa)} letras")

    while not enforcou and not acertou:
        chute = input("Qual a letra você quer tentar?").lower().strip()
        if "_" not in palavra_tentativa:
                acertou = "_" not in palavra_tentativa
                print("Parabéns!")
        if chute in palavra_secreta_list:
            for letra in palavra_secreta_list:
                if chute == letra:
                    posicao = palavra_secreta_list.index(chute)
                    palavra_tentativa[posicao] = chute
                    palavra_secreta_list[posicao] = "_"
                    if "_" not in palavra_tentativa:
                        acertou = "_" not in palavra_tentativa
                        print("Parabéns!")
                elif "_" not in palavra_tentativa:
                    acertou = "_" not in palavra_tentativa
                    print("Parabéns!")
            print(palavra_tentativa)
        else:
            tentativas -= 1
            enforcou = tentativas == 0
            print("Não há essa letra na palavra secreta")
            if tentativas == 0:
                print("Não há mais tentativas!")

    print("Fim do jogo!")


if __name__ == "__main__":
    jogar()
