# Escreva uma função recursiva que permita inverter uma palavra N. "Python" -->> "nohtyP"

# palavra = input()
# invertida = ''.join(palavra[::-1])
# print(invertida)

def inverter(p):
    invertida = p
    if n > len(p):
        return(invertida)
    else:
        invertida[n] = p[len(p)-n]
        n += 1

print(inverter(input()))