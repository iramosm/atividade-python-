# Exercício 24 - Total do pedido 

produto = input("Digite o nome do produto: ")
preço = float(input("Digite o preço do produto: R$ "))
quantidade = int(input("Digite a quantidade: "))

total = preço * quantidade

print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"total:  R$ {total:.2}")
