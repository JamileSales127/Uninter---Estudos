# 📚 Aula - 6 Tuplas, listas, dicionários e strings

## 1 - Variáveis

**Simples:** armazenam somente um dado  
**Compostas:** armazenam um conjunto de dados

### 1.1 Estrutura de dados

É um conjunto de dados organizados de uma maneira específica na memória do programa.

### 1.2 Tupla

- Estrutura de dados estática
- A tupla é imutável
- Representada em Python por parênteses

**Exemplo:**

```python
mochila = ('machado', 'martelo', 'Carne', 'Casaco')
print(mochila) 
print(mochila[0,2])
```

**Percorrendo tupla:**

```python
for item in mochila:
    print(f'Na minha mochila tem: {item}')
```

### 1.3 Desempacotamento de parâmetros em funções

- Suponha que você quer realizar o somatório de diversos valores, porém não sabe quantos valores serão somados. Pode ser que sejam somente 2, ou então 10. Como criar uma função capaz de receber um número tão variável de parâmetros? 🤔

**Exemplo:**

```python
def soma(*num):
    acumulador = 0
    print(f'Tupla: {num}')
    for i in num:
        acumulador += i
    return acumulador
#Programa
print(f'Resultado: {soma(1,2)}\n')
print(f'Resultado: {soma(1,2,3,4,5,6,7,8.9)}\n')
```
## 2 - Listas

- Estrutura de dados dinâmica 📈
- Podemos alterar dados e tamanho 🔄
- Indexadas por valores numéricos inteiros 🔢
- Representadas em Python por colchetes []

**Exemplo: mudando dado da lista**

```python
mochila = ['machado', 'martelo', 'Carne', 'Casaco']
mochila[2] = 'caju'
print('Lista: ', mochila)
```
###  2.1 Manipulando listas:

- `mochila.append('Ovos')` 🍳: adiciona no final da lista
- `mochila.insert(1, 'faca')` 🔪: insere na posição informada
- `del mochila[1]` 🗑️: deleta do índice informado
- `mochila.remove('Ovos')` ❌🍳: deleta dado informado

###  2.2 Cópia de Listas

```python
# Cópia
lista_original = [5, 6, 4, 2]
lista_referenciada = lista_original[:]
print(lista_original)
print(lista_referenciada)
```
###  2.3 O que são métodos 

- Uma lista é um objeto de uma classe dentro do Python 🐍
- Paradigmas de programação orientada a objetos 🧩
- Método é equivalente à função 🛠️
## 3 - Strings e listas dentro de listas 📜📋
![strings dentro de listas](/assets/stringDentroDeListas.png)

###  3.1 Dupla indexação

- O primeiro índice é referente a cada item da lista 📋
- O segundo índice é referente a cada caractere da string 🔤
- Assim, podemos acessar não só cada dado dentro da lista, mas também cada caractere das strings de um índice da lista 🔍

## 4 - Dicionários

- Estruturas de dados dinâmica 📊
- Podemos alterar dados e tamanho 🔄
- Indexados por chaves (palavras-chave) 🔑
- Representados em Python por chaves {}

**Exemplo:**

```python
mochila = {'laptop': 1, 'Celular': 2, 'Carregador': 3}
print('Dicionário: ', mochila)
```
**Exemplo:**

```python
game = {'nome': 'Super Mario', 
        'desenvolvedora': 'Nintendo',
        'ano': 1990}
print(game)
```
```python
#acessando um atributo por vez
print(game['nome'])
#trazendo só os valores
for values in game.values():
print(values)
#trazendo só as chaves
for keys in game.keys():
print(keys)
# trazendo values + keys
for keys, values in game.items():
print(f'{keys} = {values}')
```

###  4.1 Listas com dicionários

```python
games = []
game1 = {'nome': 'Super Mario', 
        'desenvolvedora': 'Nintendo',
        'ano': 1990}
game2 = {'nome': 'Pokemon', 
        'desenvolvedora': 'Nintendo',
        'ano': 1995}

games = [game1, game2]
print(games)
```

###  4.2 Dicionários com listas

```python
games = {'nome' : ['Super Mario', 'Zelda Ocarina of Time', 'Pokemon'],
        'videogame': ['Super Nintendo', 'Game Boy'],
        'ano' : ['1990', '1999']}
print(games)
```

## 5 - Trabalhando com métodos em strings

- Uma string é imutável ❌
- Mas, com listas, podemos alterá-la 🔄

```python
s1 = list('Algoritmos')
print(s1)
print(''.join(s1)) # print agrupado
s1[0] = 'a'
print(''.join(s1))
```
###  5.1 Relação de métodos para validação de dados em strings
![validacao strings](/assets/validacaoDadosEmStrings.png)
![validacao strings](/assets/validacaoDadosString2.png)