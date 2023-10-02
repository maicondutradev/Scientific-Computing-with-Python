hours = float(input("Digite a quantidade de horas: "))
rate = float(input("Digite a taxa: "))

if hours > 40:
    rate = rate * 1.5
    
pay = hours * rate
print("O valor a se pagar é R${}".format(pay))