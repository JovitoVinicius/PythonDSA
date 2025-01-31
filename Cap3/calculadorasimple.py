#Calculadora Simples com as 4 principais operações

print("Bem-vindo a Calculadora Simples")
print("1 - Soma | 2 - Subtração | 3 - Multiplicação | 4 - Divisão")
print("Qual operação deseja realizar?")
operacao = int(input())


if operacao == 1 or operacao == 2 or operacao == 3 or operacao == 4:
    if operacao == 1:
        a = float(input("Digite o primeiro valor: "))
        b = float(input("Digite o segundo valor: "))

        resultado = a + b
        print("O resultado da soma é ", resultado)
    if operacao == 2:
        a = float(input("Digite o primeiro valor: "))
        b = float(input("Digite o segundo valor: "))

        resultado = a - b
        print("O resultado da subtração é ", resultado)
    if operacao == 3:
        a = float(input("Digite o primeiro valor: "))
        b = float(input("Digite o segundo valor: "))

        resultado = a * b
        print("O resultado da multiplicação é ", resultado)
    if operacao == 4:
        a = float(input("Digite o primeiro valor: "))
        b = float(input("Digite o segundo valor: "))

        resultado = a / b
        print("O resultado da divisão é ", resultado)
else:
    print("Opção invalida!")