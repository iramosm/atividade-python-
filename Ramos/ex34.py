# Exercício 34
# Contar quantos números foram digitados 

contador = 0

while True:
    número = int(input("Digite um número ( 0 PARA SAIR ): "))
    
    if número == 0:
        break

    contador = contador + 1 

    print("Quantidade:", contador)
    