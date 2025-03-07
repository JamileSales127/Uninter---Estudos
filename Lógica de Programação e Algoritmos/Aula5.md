# Aula 4 - Funções

## 1. Funções
Funções são rotinas de códigos que podem ser executadas quando têm seu nome invocado dentro do programa.

## 2. Parâmetros
### Parâmetros opcionais:
```python
def soma(x=0, y=0, z=0):
    res = x + y + z
    print(res)

soma(1, 2)
```

## 3. Escopo de variáveis
Um escopo é a propriedade que determina onde uma variável pode ser utilizada dentro de um programa.

### 3.1 Escopo local
Criado sempre que uma função é chamada. Variáveis criadas, seja no campo de um parâmetro ou dentro do corpo da função, fazem parte do escopo local daquela função e são chamadas de variáveis locais. Essas variáveis só existem dentro daquela própria função.

### 3.2 Escopo global
Criado no programa principal. Variáveis globais pertencem a um escopo global e são variáveis criadas dentro do programa principal. Uma variável global existe também em todas as funções invocadas ao longo do programa.

### 3.3 A instrução global
Força nosso programa a não criar uma variável local de mesmo nome e manipular somente a global dentro de uma função:
```python
def omelete():
    global ovos
    ovos = 6

# Programa
ovos = 12
omelete()
print(ovos)
```
## 4. Retorno de valores em funções
### 4.1 Função x procedimento
- **Procedimento (procedure)**: uma rotina sem retorno.
- **Função**: uma rotina que retorna um dado a quem a invocou.
```python
def soma(x=0, y=0, z=0):
    res = x + y + z
    return res

# Programa
retornado = soma(1, 2, 3)
print(retornado)

# Forma alternativa simplificada
print(soma(2, 3))
```
## 5. Recursos avançados com funções

### 5.1 Erro de sintaxe
Ocorre quando o programador comete algum erro de digitação, esquece alguma palavra-chave, caractere ou erra na indentação do código.

### 5.2 Exceção
Neste tipo de erro, a sintaxe está correta, porém um erro durante a execução do programa ocorre, normalmente devido a um dado digitado de maneira inválida e não tratado durante o programa.

#### 5.2.1 Exceções comuns em Python
- **ZeroDivisionError**: erro de divisão por zero.
- **ValueError**: erro de um dado não esperado sendo digitado.
- **IndexError**: erro de índice inexistente sendo acessado.

### 5.3 Tratando exceções no Python
```python
while True:
    try:
        x = int(input('Digite um número: '))
        break
    except ValueError:
        print('Ops!!! Número inválido. Tente novamente...')
    finally:
        print(f'Tentativa {i}')
        i += 1
```
#### Obs: o **finally** sempre acontece
## 6. Funções lambda
Funções mais simples, sem nome, chamadas de funções lambda. Elas podem ser escritas em uma só linha de código e dentro do programa principal.

### Exemplo 1:
```python
res = lambda x: x * x
print(res(3))
```
### Exemplo 2:
```python
soma = lambda x, y: x + y
print(soma(3, 5))
```