def contagem_regressiva(n):
    if n == 0: 
        print("Fogo!")
    else: 
        print("%d..."%n)
        contagem_regressiva(n-1)
contagem_regressiva(3)
