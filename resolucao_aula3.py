sexo = str(input("Qual é o seu sexo: [M/F]: ")).strip().upper()[0]
while sexo not in "MmfF":
    sexo = str(input("Dados incorretos por favor tente novamente: ")).strip().upper()[0]
print("sexo {} registrado com sucesso".format(sexo))