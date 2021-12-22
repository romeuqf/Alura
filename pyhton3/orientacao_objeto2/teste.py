class Pessoa:
    tamanho_cpf = 11

p = Pessoa()

print(p.tamanho_cpf)

p.tamanho_cpf = 12

print(p.tamanho_cpf)

print(Pessoa.tamanho_cpf)


class Relatorio:
    def gera_relatorio(self):
        print('Relatório geral')


class RelatorioUsuarios(Relatorio):
    def gera_relatorio(self):
        print('Relatório dos usuários')


class RelatorioCustos(Relatorio):
    def gera_relatorio(self):
        print('Relatório de custos')


relatorio1 = RelatorioUsuarios()
relatorio2 = RelatorioCustos()
relatorio3 = RelatorioUsuarios()
relatorio4 = RelatorioUsuarios()
relatorio5 = Relatorio()

relatorios = [relatorio1, relatorio2, relatorio3, relatorio4, relatorio5]
for rel in relatorios:
    rel.gera_relatorio()


