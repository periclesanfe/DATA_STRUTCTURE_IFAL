# Tendo como dado de entrada a altura(h) de uma pessoa, construa um algoritimo
# que calcule seu peso ideal, utilizando as seguintes fórmulas:
# - para homens: (72.7*h) - 58
# - para mulhere: (62.1*h) - 44.7

altura = float(input('Informe a sua altura em metros: '))
if (input('Qual seu sexo? (h/m): ')) == 'h':
    print('Seu peso ideial é {:.2f}kg'.format((altura*72.7)-58))
else:
    print('Seu peso ideal é {:.2f}kg'.format((altura*61.1)-44.7))