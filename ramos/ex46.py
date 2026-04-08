def menu():
    print("Escolha a camisa :")
    print("1 - polo ")
    print("2 - regata")
    print("3 - manga longa ")
    print("4 - gola alta ")
    print("5 - forma de pagamentor")
    print("6 - sair")

    pedido = input("Informe o nº da opção desejada: ")

    if pedido == "1":
        print("Você escolheu polo ")
    
    elif pedido == "2":
        print("Você escolheu regata  ")
    
    elif pedido == "3":
        print("Você escolheu manga longa  ")
    
    elif pedido == "4":
        print("Você escolheu gola alta")
    
    elif pedido == "5":
        print("Encerrando o pedido...")
    
    else:
        print("Opção inválida!")

menu()