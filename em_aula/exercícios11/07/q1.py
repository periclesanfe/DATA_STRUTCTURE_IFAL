# n = int(input('Digite um numero: '))
# resp = 1
# while n != 0:
#     resp=resp*n
#     n -= 1
# print(resp)

def fatorial(n):
    if n ==0:
        return(1)
    else:
        return(n*(fatorial(n-1)))

print(fatorial(int(input())))