from TAD_Conta import Conta, lista_contas


conta_pericles = Conta('Pericles', 1000)
conta_joao = Conta('Joao', 2000)
conta_maria = Conta('Maria', 3000)
conta_silva = Conta('Silva', 4000)
print(lista_contas)

for conta in lista_contas:
    if conta.saldo > maior_saldo:
        maior_saldo = conta.saldo
        nome_maior_saldo = conta.nome_correntista
print(f'O correntista com maior saldo é {nome_maior_saldo} com saldo de {maior_saldo}')