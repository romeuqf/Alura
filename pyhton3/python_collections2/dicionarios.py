meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto.split()

set(meu_texto.split())

"""# Dicionário (Mapa etc)"""

aparicoes = {
  "Guilherme" : 1,
  "cachorro" : 2,
  "nome" : 2,
  "vindo" : 1
}

type(aparicoes)

aparicoes["Guilherme"]

aparicoes["cachorro"]


aparicoes.get("cachorro", 0)

aparicoes = dict(Guilherme = 2, cachorro = 1)
aparicoes

aparicoes = {
  "Guilherme" : 1,
  "cachorro" : 2,
  "nome" : 2,
  "vindo" : 1
}

aparicoes["Carlos"] = 1

aparicoes

aparicoes["Carlos"] = 2

aparicoes

del aparicoes["Carlos"]

aparicoes

"cachorro" in aparicoes

"Carlos" in aparicoes

for elemento in aparicoes:
  print(elemento)

for elemento in aparicoes.keys():
  print(elemento)

for elemento in aparicoes.values():
  print(elemento)

1 in aparicoes.values()

for elemento in aparicoes.keys():
  valor = aparicoes[elemento]
  print(elemento, valor)

for elemento in aparicoes.items():
  print(elemento)

for chave, valor in aparicoes.items():
  print(chave, "=", valor)

["palavra {}".format(chave) for chave in aparicoes.keys()]

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

aparicoes = {}

for palavra in meu_texto.split():
  ate_agora = aparicoes.get(palavra, 0)
  aparicoes[palavra] = ate_agora + 1

print(aparicoes)

from collections import defaultdict

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
  ate_agora = aparicoes[palavra]
  aparicoes[palavra] = ate_agora + 1

print(aparicoes)

int()

dicionario = defaultdict(int)
print(dicionario['guilherme'])

dicionario['guilherme'] = 15
print(dicionario['guilherme'])

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
  aparicoes[palavra] += 1

print(aparicoes)

class Conta:
  def __init__(self):
    print("Criando uma conta")

contas = defaultdict(Conta)
contas[15]

contas[17]

contas[15]

from collections import Counter

aparicoes = Counter()
for palavra in meu_texto.split():
  aparicoes[palavra] += 1

print(aparicoes)

aparicoes = Counter(meu_texto.split())

print(aparicoes)