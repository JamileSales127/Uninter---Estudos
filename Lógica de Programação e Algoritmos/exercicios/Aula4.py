# Escreva um algoritmo que imprima na tela somente valores dentro de um intervalo especificado 
# peo usuário e que sejam números pares

from tokenize import Double


inicio = int(input('Qual valor deseja iniciar a contagem? '))
final = int(input('Qual valor deseja finalizar a contagem? '))

x = inicio
while (x <= final):
    if(x % 2 == 0):
        print(x)
    x += 1

# Exercicio 2
#Escreva um algoritmo que calcule a sua média de notas em determinada disciplina
# Vamos assumir que a média final é dada pela média aritmética de cinco notas digitadas

soma = 0
cont = 1
while (cont <= 5):
    x = float(input(f'Digite a {cont}° nota: '))
    soma = soma + x
    cont = cont + 1
media = soma / 5
print(f'Média final: {media}')

# Exercicio 3
# Escreva um algoritmo que calcule a média dos números pares de 1 até 100
#(1 e 100 inclusos). Implemente o laço usando for

soma = 0
qtd = 0
for i in range(1, 101):
    if(i % 2 == 0):
        soma =+ i
        qtd =+ 1
media = soma / qtd
print(f'Média dos números pares de 1 até 100: {media}')
