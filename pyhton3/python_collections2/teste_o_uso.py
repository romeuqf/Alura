from collections import Counter

texto1 = "Imagine que você precise desenvolver uma funcionalidade no seu projeto, mas essa mesma funcionalidade já foi desenvolvida por uma outra pessoa (ou um grupo de pessoas) e disponibilizada na internet para que qualquer um também possa utilizar. Logo, em vez de desenvolver essa funcionalidade do zero, você pode utilizar essa solução proposta, “importando” essa funcionalidade para a sua aplicação/código."

texto2 = 'Portanto, utilizar uma dependência externa, quando necessário, é muito importante para o desenvolvimento do seu projeto, já que simplifica muito a utilização de determinada funcionalidade. Assim, conseguimos reutilizar um código já desenvolvido por terceiros, otimizando o tempo na criação de uma nova funcionalidade.'

aparicoes_texto1 = Counter(texto1.lower())
print((aparicoes_texto1))
total_aparicoes = sum(aparicoes_texto1.values())


for letra, valor in aparicoes_texto1.items():
    tupla = (letra,valor/total_aparicoes)
    print(tupla)


proporcoes = [(letra,valor/total_aparicoes) for letra, valor in aparicoes_texto1.items()]
proporcoes = Counter(dict(proporcoes)).most_common(10)
print(proporcoes)

def analisa_frequencia_de_letras(texto):
  aparicoes = Counter(texto.lower())
  total_de_caracteres = sum(aparicoes.values())

  proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
  proporcoes = Counter(dict(proporcoes))
  mais_comuns = proporcoes.most_common(10)
  for caractere, proporcao in mais_comuns:
    print("{} => {:.2f}%".format(caractere, proporcao * 100))

analisa_frequencia_de_letras(texto1)

analisa_frequencia_de_letras(texto2)