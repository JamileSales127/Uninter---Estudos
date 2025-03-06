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


