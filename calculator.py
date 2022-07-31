print("\n********** Python Calculator ***********")

print("\nSelecione o número da operação desejada:")

print("\n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")

menu = int(input("\nDigite a sua opção (1/2/3/4):"))
print(" ")

if menu == 1:
    primeiro = int(input("digite o primeiro número:"))
    segundo = int(input("digite o segundo número:"))
    soma = primeiro + segundo
    print('O resultado de: %s + %r =' %(primeiro, segundo), soma)

elif menu == 2:
    primeiro = int(input("digite o primeiro número:"))
    segundo = int(input("digite o segundo número:"))
    subtracao = primeiro - segundo
    print('O resultado de: %s - %r =' %(primeiro, segundo), subtracao)       

elif menu == 3:
    primeiro = int(input("digite o primeiro número:"))
    segundo = int(input("digite o segundo número:"))
    multiplicacao = primeiro * segundo
    print('O resultado de: %s * %r =' %(primeiro, segundo), multiplicacao)

elif menu == 4:
    primeiro = int(input("digite o primeiro número:"))
    segundo = int(input("digite o segundo número:"))
    divisao = primeiro / segundo
    print('O resultado de: %s / %r =' %(primeiro, segundo), divisao) 

else:
    print("Opção inválida!")
