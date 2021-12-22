idades = [15, 87, 32, 65, 56, 32, 49, 37]

for i in range(len(idades)):
    print(i, idades[i])

range(len(idades))  # lazy...

enumerate(idades)  # lazy

list(range(len(idades)))  # forcei a geração dos valores

list(enumerate(idades))

for indice, idade in enumerate(idades):  # unpacking da nossa tupla
    print(indice, "x", idade)

usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

for nome, idade, nascimento in usuarios:  # ja desempacotando
    print(nome)

for nome, _, _ in usuarios:  # ja desempacotando, ignorando o resto
    print(nome)

print(sorted(idades))

print(list(reversed(idades)))

print(sorted(idades, reverse=True))

print(list(reversed(sorted(idades))))

from herenca_polimorfismo import ContaCorrente

conta1 = ContaCorrente(1)
conta1.deposita(100)

conta2 = ContaCorrente(2)
conta2.deposita(1000)

conta3 = ContaCorrente(3)
conta3.deposita(2000)

contas = [conta2, conta1, conta3]

for conta in sorted(contas, key=ContaCorrente.extrai_saldo):
    print(conta)

# usar o attrgetter para trazer um atributo do método
from operator import attrgetter

for conta in sorted(contas, key=attrgetter('_saldo')):
    print(conta)

# criar a função __lt__ no encapsulamento
for conta in sorted(contas):
    print(conta)

# usar o attrgetter com duas classificações
conta4 = ContaCorrente(4)
conta4.deposita(100)

contas2 = [conta2, conta1, conta3, conta4]

for conta in sorted(contas2, key=attrgetter('_saldo', '_conta')):
    print(conta)

for conta in sorted(contas2):
    print(conta)

# FUNCTOOLS
