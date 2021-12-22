from abc import ABCMeta, abstractmethod
from functools import total_ordering

@total_ordering
class Conta(metaclass=ABCMeta):
  def __init__(self,conta):
    self._conta = conta
    self._saldo = 0

  def deposita(self,valor):
    self._saldo += valor

  @abstractmethod
  def passa_o_mes(self):
      pass

  def extrai_saldo(self):
    return self._saldo

  def __lt__(self, other):
    if self._saldo != other._saldo:
      return self._saldo < other._saldo
    return self._conta < other._conta

  def __eq__(self, other):
    if not isinstance(other, Conta):
      return False

    return self._conta == other._conta and self._saldo == other._saldo

  def __str__(self):
    return "[>>Conta {} Saldo {}<<]".format(self._conta, self._saldo)

class ContaCorrente(Conta):
  def passa_o_mes(self):
    self._saldo -= 2

class ContaPoupanca(Conta):
  def passa_o_mes(self):
    self._saldo *= 1.01
    self._saldo -= 3

class ContaInvestimento(Conta):
  # def passa_o_mes(self):
    pass

conta16 = ContaCorrente(16)
conta16.deposita(1000)

conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

contas = [conta16, conta17]

for conta in contas:
  conta.passa_o_mes()
  print(conta)


contaA = ContaCorrente(1)
contaB = ContaCorrente(1)

print(contaA == contaB)

print(isinstance(conta17, Conta))