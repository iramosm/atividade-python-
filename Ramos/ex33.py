# Exercício 33
# Somar números até digitar 0

soma = 0

while True:
    número = int(input("Digite um número ( 0 para sair ): "))

    if número == 0:
        break

    soma = soma + número

    print("Soma:" , soma)
    