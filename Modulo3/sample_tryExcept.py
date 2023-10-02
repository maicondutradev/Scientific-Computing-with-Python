try:
    nota1 = float(input('Insira a nota da P1: '))
    nota2 = float(input('Insira a nota da P2: '))
except ValueError:
    print('Uma das notas que você digitou não é um valor númerico. Tente novamente!')

else:
    media = (nota1 + nota2) / 2
    print('A sua média final do periodo é {}'.format(media)) 