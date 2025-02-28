# Exercicio 1
#  Faça um algoritmo que receba três valores, representando os lados de um 
# triângulo fornecidos pelo usuário. Verifique se os valores formam um triângulo e classifique como:



num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 == 0 or num2 == 0 or num3 == 0:
    print('Valores inválidos, um triângulo não pode ter um dos lados com o valor igual a 0')
else:
    if num1 == num2 == num3:
        print("Equilátero - Todos os lados são iguais")
    elif num1 == num2 or num2 == num3 or num1 == num3:
        print("Isósceles - Dois lados são iguais")
    else:
        print("Escaleno - Todos os lados são diferentes")

# Exercicio 2

print('Calculadora')
print('Escolha a operação:')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

op = int(input('Digite a operação desejada: '))
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if op == 1:
    print('Resultado: ', num1 + num2)
elif op == 2:
    print('Resultado: ', num1 - num2)
elif op == 3:
    print('Resultado: ', num1 * num2)
elif op == 4:
    print('Resultado: ', num1 / num2)
else:
    print('Operação inválida')