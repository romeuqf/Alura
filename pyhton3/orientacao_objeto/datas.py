class Data:
    def __init__(self,dia, mes, ano):
        self.dia = str(dia)
        self.mes = str(mes)
        self.ano = str(ano)

    def formatada(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))
