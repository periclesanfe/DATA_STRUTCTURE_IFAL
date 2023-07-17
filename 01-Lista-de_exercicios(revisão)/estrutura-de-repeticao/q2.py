# Faça um programa que leia um nome de usuário e a sua senha e não aceite a
# senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
# pedir as informações.

while True:
    login = input("Nome: ")
    password = input("Senha: ")
    if login != password:
        break
    print("ERRO: nome e login são iguais!")
print("Cadastro Efetuado!")
