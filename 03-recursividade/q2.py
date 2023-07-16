def inv(palavra):
    if len(palavra) <= 0:
        print(palavra)
        return palavra
    else:
        return inv(palavra[1:])+palavra[0]

print(inv('python'))