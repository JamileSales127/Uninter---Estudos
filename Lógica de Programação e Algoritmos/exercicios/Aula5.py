#Exercicio 1
#Escreva uma rotina que crie uma borda ao redor de uma palavra, para destacá-la como sendo um título. 
# A rotina deve receber como parâmetro a palavra a ser destacada. 
# O tamanho da caixa de texto a ser destacada. 
# O tamanho da caixa de texto deverá ser adaptável, de acordo com o tamanho da palavra.

def border(palavra):
    tam = len(palavra)
    print('+', '-' * tam,'+' )
    print('|', palavra , '|')
    print('+', '-' * tam,'+' )

#programa
border('Olá mundo!')
border('Eu amo esse mundinho :)')

#Exercicio 2
# Escreva uma função para validar uma string. Essa função recebe como parâmetro a string, 
# o número mínimo e máximo de caracteres. Retorne verdadeiro se o tamanho da string
# estiver entre os valores de mínimo e máximo, e falso, caso contrário (elaborado com base em Menezes, s. d.)

def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while ((tam < min) or (tam > max)):
        s1 = input(pergunta)
        tam = len(s1)
    return s1

#programa
x = valida_string('Digite uma string: ', 10, 30)
print('Você digitou a string: {}. \n Dado válido. Encerrando o programa...'.format(x))

#Exercicio 3

#Faça uma função lambda que recebe dois valores numéricos como parâmetro. Ao primeiro valor
#sempre some 5. Em seguida multiplique ambos e retorne o resultado

calc = lambda a , b: (a + 5) *b 
print(calc(5, 10))