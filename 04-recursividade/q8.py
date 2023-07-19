# Escreva uma função recursiva que informa se uma String é palíndroma ou não. Um palíndromo é uma string que é lida da
# mesma maneira da esquerda para a direita e da direita para a esquerda. Alguns exemplos de palíndromo são "E até o
# papa poeta é" (se os espaços, pontuação e acentos forem ignorados).

# retira acentos e caracteres especiais
def adequa(palavra):
    
# inverte a palavra
def inverte(palavra):
    if len(palavra) == 0:
        return ""
    else:
        return inverte(palavra[1:]) + palavra[0]
    
# retirar espaços
            
# retorna se a palavra é palindroma
# dica: separa primeira e ultima letra e chama inverter novamente com as letras que restaram, se 1 ou 0 return True
def palindroma(palavra):
    return inverte(palavra) == palavra

# TESTES
print(palindroma('ana'))
print(palindroma('E até o papa poeta é'))
print(palindroma('p'))
print(palindroma(''))

