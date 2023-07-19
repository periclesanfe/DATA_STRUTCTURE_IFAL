# Escreva uma função recursiva que calcule o Nésimo 10 termo da sequencia de Fibonacci. A sequência de Fibonacci é
# 0,1, 1, 2, 3, 5, 8, 13, 21,...


# def fibonacci(n):
#    pri = 1
#    sec = 1
#    print(pri)
#    print(sec)
#    for i in range(0, n - 2):
#        ter = sec + pri
#        pri = sec
#        sec = ter
#        print(ter)


# def fibonacci(n, pri, sec):
#    if n == 0:
#        print(sec + pri)
#    else:
#        ter = sec + pri
#        pri = sec
#        sec = ter
#        print(ter)
#        fibonacci(n - 1, pri, sec)


def fibonacci(n, pri=1, sec=1):
    if n == 1:
        return pri
    else:
        return str(pri) + " " + str(fibonacci(n - 1, sec, sec + pri))


# TESTE
print(fibonacci(6))
print(fibonacci(5))
print(fibonacci(10))
