class Conta:
    def __init__(self, numero, titular, saldo, limite):
        # print("Construindo objeto {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def extrato(self):
        print("Saldo: {}".format(self.saldo))

    def deposito(self, valor):
        self.__saldo += valor

    def __teste_saque(self, valor_saque):
        valor_disponivel = self.__saldo + self.__limite
        return valor_saque <= valor_disponivel

    def __utilizacao_limite(self, valor):
        valor_maior = abs(self.__saldo - valor)
        if valor > self.__saldo:
            return print("Limite utilizado em {}".format(valor_maior))
        else:
            return print("Valor ultrapassou o ")

    def saque(self, valor):
        if self.__teste_saque(valor):
            self.__utilizacao_limite(valor)
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite".format(valor))

    def transferir(self, conta_destino, valor):
        self.saca(valor)
        conta_destino.deposito(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"