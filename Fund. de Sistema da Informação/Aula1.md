# 📚 Aula 3: Variáveis, Dados e Seus Tipos

## 1️⃣ VARIÁVEIS, DADOS E SEUS TIPOS
As variáveis são espaços na memória do computador onde armazenamos valores. Cada variável possui um **tipo de dado**, que define o que pode ser armazenado nela.

- **📊 Numérico** – Representa números inteiros ou decimais (ponto flutuante). Deve ser usado quando operações aritméticas forem necessárias.
- **🔤 Caractere (String)** – Representa letras, caracteres especiais e até mesmo números (quando não forem utilizados para cálculos).
- **✅ Booleano (True/False)** – Representa valores lógicos: **verdadeiro (True) ou falso (False)**, geralmente usados em condições e decisões.

## 1.1 ✏️ Regras para nomes de variáveis

📌 **Regras importantes:**
✔️ O nome deve começar com uma letra ou underscore (_).  
✔️ Pode conter letras, números e underscores (_) apenas.  
✔️ Não pode conter espaços ou caracteres especiais.  
✔️ Não pode ser uma palavra reservada da linguagem de programação.  
✔️ Deve ser descritivo e seguir um padrão (exemplo: `idade_usuario`, `valor_total`).  


---

## 2️⃣ Variáveis de Cadeia de Caracteres (**Strings**)
O **Unicode** permite representar caracteres de diversas línguas, símbolos especiais e até **emojis**! 🎉 Isso garante compatibilidade global na manipulação de textos.

```python
texto = "Olá, 🌎!"
print(texto)  # Saída: Olá, 🌎!
```

---

## 3️⃣ Composição com **f-strings**
As **f-strings** permitem inserir expressões diretamente dentro de uma string usando `{}`.

```python
nome = "Jamile"
idade = 25
print(f"Olá, meu nome é {nome} e eu tenho {idade} anos.")
```
📝 **Vantagens das f-strings:**
- São mais fáceis de ler e escrever.
- Permitem cálculos e expressões dentro das chaves `{}`.

---

## 4️⃣ Fatiamento (**String Slicing**)
Podemos extrair partes de uma string usando índices.

```python
s1 = "Lógica de Programação e Algoritmos"
print(s1[0:6])  # Saída: Lógica
```
📌 **Regras do fatiamento:**
- `s1[início:fim]` → Retorna caracteres do índice **início** até **fim-1**.
- `s1[:fim]` → Retorna do começo até **fim-1**.
- `s1[início:]` → Retorna do **início** até o final.
- `s1[::-1]` → Retorna a string invertida.

---

## 5️⃣ Tamanho da String (**len()**)
Para saber quantos caracteres uma string possui, usamos a função `len()`.

```python
s1 = "Lógica de Programação e Algoritmos"
tamanho = len(s1)
print(tamanho)  # Saída: 32
```

---

## 6️⃣ Convertendo dados de entrada (**Casting**)
📌 Quando recebemos entrada do usuário, ela vem como **string**. Precisamos convertê-la para o tipo correto:

```python
idade = input("Digite sua idade: ")  # Entrada como string
idade = int(idade)  # Conversão para inteiro
print(f"Ano que vem, você terá {idade + 1} anos!")
```

🚀 Agora você já domina o uso de variáveis, strings e manipulação de dados em Python! 💡🐍
