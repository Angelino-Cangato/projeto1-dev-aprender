casa = float(input("Qual é o valor da casa: "))
salario = float(input("Salario do comprador: "))
anos = int(input("Quantos anos de financiamneto: "))

prestao = casa / (anos * 12)
minimo = salario * 30 / 100

print('Para pagar uma casa de {:.2f} em {} anos'.format(casa, anos), end='')
print('A precisão será  de {:.2f}'.format(prestao))

if prestao <= minimo:
    print("O emprestimo pode ser concedido")
else:
    print("Emprestimo negado!")
