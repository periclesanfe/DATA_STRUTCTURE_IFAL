# Armazene em uma lista todos os multiplos de 3, entre 1 e 100
# imprima cada elemento da lista, um por linha

multiplos = []
for i in range(1, 100):
    if i % 3 == 0:
        multiplos.append(i)
        print(i)
print(multiplos)
