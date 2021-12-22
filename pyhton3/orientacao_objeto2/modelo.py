class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    # def imprime(self):
    #     print(f'{self._nome} - {self.ano} - {self._likes}')

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    # def imprime(self):
    #     print(f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes}')

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    # def imprime(self):
    #     print(f'{self._nome} - {self.ano} - {self.temporadas} temporadas- {self._likes}')

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas- {self._likes}'


# class PlayList(list):
#     def __init__(self, nome, programas):
#         self.nome = nome
#         super().__init__(programas)

class PlayList:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)




vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmp = Filme('todo mundo em pânico', 2000, 100)
demolidor = Serie('demolidor',2019,3)

tmp.dar_likes()
tmp.dar_likes()
tmp.dar_likes()
tmp.dar_likes()
tmp.dar_likes()
tmp.dar_likes()
tmp.dar_likes()
tmp.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()


filmes_e_series = [vingadores, atlanta, demolidor, tmp]
playlist_fim_de_semana = PlayList('Fim de Semana', filmes_e_series)


for x in playlist_fim_de_semana:
    print(x)
print(len(playlist_fim_de_semana))

print(demolidor in playlist_fim_de_semana)