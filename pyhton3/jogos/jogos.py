import advinhacao
import forca

print("*******************************")
print("Escolha seu jogo!")
print("*******************************")

print("(1) Advinhação (2) Forca")
jogo = int(input("Digite o número do jogo:"))

if jogo == 1:
    print("Jogo Advinhação escolhido!")
    advinhacao.jogar()
elif jogo == 2:
    print("Jogo Forca escolhido!")
    forca.jogar()
else:
    print("Número não válido!")