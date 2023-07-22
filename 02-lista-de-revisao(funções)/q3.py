# Faça uma função par_ou_impar(numero) que recebe um número inteiro e retorna “par” ou “impar”.

def par_ou_impar(numero):
    return 'par' if numero%2==0 else 'impar'


#testes
print(par_ou_impar(5))
print(par_ou_impar(1))
print(par_ou_impar(0))
print(par_ou_impar(2))
print(par_ou_impar(-200))
