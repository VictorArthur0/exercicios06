n1 = int(input("(Digite 10 números!). Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
n5 = int(input("Digite o quinto número: "))
n6 = int(input("Digite o sexto número: "))
n7 = int(input("Digite o sétimo número: "))
n8 = int(input("Digite o oitavo número: "))
n9 = int(input("Digite o nono número: "))
n10 = int(input("Digite o décimo número: "))

lista = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]

lista.sort()
print(f"A seguir, a lista dos números solicitados do menor para o maior: {lista}")
print (f"O maior número é {max(lista)}. O menor número é {min(lista)}")