# 🌟 Aula 4 - Estruturas de Repetição: While 🌟

## 🔄 While
O comando `while` repete um bloco de instruções enquanto determinada condição se mantiver verdadeira. Caso contrário, ocorre o desvio para a primeira linha de código após este bloco de repetição.

### 📌 Exemplo:
```python
x = 1
while x <= 5:
    print(x)
    x = x + 1
```

### 📝 Variável de Controle

A **variável de controle** é aquela que define a **condição de parada** do laço.  
Geralmente, ela **conta** quantas vezes o laço foi executado. Em alguns casos, essa variável é chamada de **iterador**. ⏱️

---

### 🔢 Variáveis Contadoras

**Contadoras** são variáveis que **acumulam valores constantes** ao longo do tempo.  
Por exemplo, em um laço que conta até 10, você pode incrementar uma contadora de 1 em 1. 📈

---

### ➕ Variáveis Acumuladoras

**Acumuladoras** são variáveis que **somam valores** ao longo do tempo, como um **somatório**.  
Um exemplo seria somar os números de 1 até 100. 🧮

# 🌟 Estruturas de Repetição

## ⛔ Instrução `break`

A instrução **`break`** serve para **encerrar um laço de repetição abruptamente**, independentemente do estado da variável de controle do laço.

```python
print('Digite uma mensagem que irei repetir para você!') 
print('Para encerrar, escreva "sair"')
while True:
    mensagem = input('')
    print(mensagem)
    if mensagem == 'sair':
        break
    print('Encerrando o programa...')
```
```python
while True:
    nome = input('Qual o seu nome?')
    if nome != 'Jamile':
        continue
    senha = input('Qual a sua senha?')
    if senha == '123':
        break
print('Acesso permitido')

```
# 🔍 Valores **Truthy** e **Falsey**

Dados não booleanos também podem ser tratados como **True** ou **False** em uma condição, seja esta de uma estrutura condicionada ou de um laço.

### **Falsey** / **False**
- Número **zero** (int ou float) e **string vazia**.

### **Truthy** / **True**
- Qualquer outro dado.

---

### Exemplo:

```python
nome = ''  # Falsey
while not nome:  # not Falsey (truthy/true)
    # Encerra o loop quando o usuário digitar um nome
    nome = input('Digite o seu nome: ')
```
```python
valor = int(input('Digite um número qualquer: '))
if valor:  # Equivalente a if valor != 0:
    print('Você digitou um número diferente de zero')
else:
    print('Você digitou zero')
```
    
# 🔁 Estrutura `for` (Para)

Assim como o `while`, essa estrutura repete um bloco de instruções enquanto uma condição se mantiver verdadeira.  
No entanto, diferentemente do `while`, o `for` é empregado em situações em que o número de vezes que o laço irá executar é **finito** e bem definido.

---

### Exemplo:

```python
for i in range(6):
    print(i)
```
📌 **Python com três parãmetros:**  
![for três parâmetros](/assets/3parametros.png)

# 🔡 Varredura de String

Podemos passar por todos os caracteres de uma string usando um laço `for`.

---

### Exemplo:

```python
frase = "Lógica de Programação e Algoritmos"
for i in range(0, len(frase), 1):
    print(frase[i], end="")
```
# 🧑‍💻 Estruturas de Repetição Aninhadas

Podemos **inserir laços dentro de outros laços**.  
Não existe limite para quantos laços podemos colocar dentro de outro laço. Também podemos misturar `while` e `for`.

---

### Exemplo: Calcular a Tabuada de 1 a 10

Escreva um algoritmo em Python que calcule a tabuada de todos os números de **1 a 10**, e, para cada número, calcule a tabuada multiplicando-o pelo intervalo de **1 a 10**. Existem 3 possíveis soluções.

---

#### 1. Usando **2x `while`**:

```python
tabuada = 1
while tabuada <= 10:
    print(f'Tabuada do {tabuada}')
    i = 1
    while i <= 10:
        print(f'{tabuada} x {i} = {tabuada * i}')
        i += 1
    tabuada += 1
```
#### 1. Usando **2x `for`**:

```python
for tabuada in range(1, 11):
    print(f'Tabuada do {tabuada}')
    for i in range(1, 11):
        print(f'{tabuada} x {i} = {tabuada * i}')
```
#### 1. Usando **`for` + `while`**:
```python
tabuada = 1
while tabuada <= 10:
    print(f'Tabuada do {tabuada}')
    for i in range(1, 11):
        print(f'{tabuada} x {i} = {tabuada * i}')
    tabuada += 1
```