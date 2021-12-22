teste = set([1,2,4,5])
print('Teste: {}'.format(teste))
usuarios_data_science = {15,23,43,56}
usuarios_machine_learning = {13,23,56,42}

print('Data Science: {}'.format(usuarios_data_science))
print('Machine Learning {}'.format(usuarios_machine_learning))

print('Aparece em ambos: {}'.format(usuarios_machine_learning | usuarios_data_science))

print('Fez os dois: {}'.format(usuarios_machine_learning & usuarios_data_science))

print('Fez só em Data Science: {}'.format(usuarios_data_science - usuarios_machine_learning))

print('Fez apenas um curso: {}'.format(usuarios_data_science ^ usuarios_machine_learning))

usuarios = set([1,15,56,78,95,65,13])
print(usuarios)
usuarios.add(99)
print(usuarios)

# não dá pra adicionar um item em um frozenset
usuarios2 = frozenset({1,15,56,78,95,65,13})
print(usuarios2)

