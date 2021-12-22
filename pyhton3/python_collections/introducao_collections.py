def faz_processamento_de_visualizacao(lista = []):
  print(len(lista))
  print(lista)
  lista.append(13)

faz_processamento_de_visualizacao()

faz_processamento_de_visualizacao()

faz_processamento_de_visualizacao()

faz_processamento_de_visualizacao()

def faz_processamento_de_visualizacao(lista = list()):
  print(len(lista))
  print(lista)
  lista.append(13)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()

def faz_processamento_de_visualizacao(lista = None):
  if lista == None:
    lista = list()
  print(len(lista))
  print(lista)
  lista.append(13)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()


class ContaCorrente:
  def __init__(self,conta):
    self.conta = conta
    self.saldo = 0

  def deposita(self,valor):
    self.saldo += valor

  def __str__(self):
    return "[>>Conta {} Saldo {}<<]".format(self.conta, self.saldo)


contaRomeu = ContaCorrente(15)
print(contaRomeu)

contaRomeu.deposita(5000000)
print(contaRomeu)

contaJoao = ContaCorrente(1252)
contaJoao.deposita(12040)


contas = [contaRomeu, contaJoao]
for conta in contas:
  print(conta)

contas2 = [contaRomeu, contaJoao, contaRomeu]

print(contas2[0])

contaRomeu.deposita(100)

print(contaRomeu)

