# 🌟 Introdução à Lógica e aos Algoritmos 🌟

## 📌 Aula 1 - Fundamentos Essenciais

---

## 🧠 1. Lógica na Computação

A lógica na computação é a maneira pela qual instruções, assertivas e pressupostos são organizados dentro de um algoritmo para viabilizar a implantação de um programa.

### 🔹 O que é um Algoritmo?
Um algoritmo é uma sequência de passos bem definidos para que uma determinada tarefa seja concluída ou um objetivo seja atingido.

---

## 💻 2. Sistemas de Computação

### 🏛 2.1 A Máquina de von Neumann
A arquitetura de von Neumann define a estrutura básica dos computadores modernos e é composta pelos seguintes elementos:

- **Memória (RAM)**: Armazena o programa (algoritmo) em execução e também os dados usados pelo programa. Tudo é armazenado em codificação binária.
- **Unidade Lógica e Aritmética (ULA)**: Responsável por todos os cálculos aritméticos e lógicos do computador. Dentro desta unidade temos o acumulador, que armazena temporariamente os resultados das operações.
- **Unidade de Controle (UC)**: Gerencia o fluxo de execução dos programas dentro do computador, definindo qual será a próxima instrução a ser executada e onde ela se encontra na memória.
- **Dispositivos de Saída**: Permitem a comunicação dos resultados de um programa com o usuário, como monitor ou lâmpadas indicativas.
- **Processador (CPU)**: A ULA e a UC formam o processador (CPU), que é a unidade central de processamento do computador. Atualmente, CPUs modernas possuem memórias cache embutidas para melhorar o desempenho.

### 🖥 2.2 O Bit, o Byte e a Palavra
Os computadores baseados na arquitetura de von Neumann operam em **código binário** e trabalham apenas com os dígitos **0 e 1**.
- **Bit**: Menor unidade de armazenamento de um computador.
- **Byte**: Conjunto de 8 bits.
- **Palavra (Word)**: Unidade mínima de manipulação da CPU, que pode variar conforme a tecnologia do processador (ex.: 64 bits = 8 bytes).

### 🖥 2.3 O Sistema Operacional
O sistema operacional desempenha um papel fundamental no funcionamento do computador:
1. Permite ou não a execução de um software.
2. Gerencia o uso da memória e do processador por cada programa.
3. Abstrai o hardware tanto para o usuário quanto para o programador, facilitando a interação com o sistema.

---

## 📜 3. Representações dos Algoritmos

### 📝 3.1 Descrição Narrativa
Os algoritmos podem ser representados através de linguagem natural, como no exemplo abaixo:

1. Ler dois valores (x e y).
2. Verificar se x e y são iguais.
3. Se forem iguais, exibir "Valores iguais!".
4. Se forem diferentes, exibir "Valores diferentes!".
5. Fim!

### 💡 3.2 Pseudocódigo
O pseudocódigo é uma forma estruturada de representar um algoritmo sem se preocupar com a sintaxe específica de uma linguagem de programação:

```pseudo
Algoritmo Exemplo
Var
   x, y: inteiro
Início
   Ler (x, y)
   Se (x = y) então
      Mostrar ("Valores iguais!")
   Se não
      Mostrar ("Valores diferentes!")
Fim
```
### 🔄 3.3 Fluxograma
Os fluxogramas são representações gráficas de um algoritmo utilizando símbolos padronizados para facilitar a organização do raciocínio lógico.

![Fluxograma Exemplo](/assets/fluxograma.jpg)

## 🛠 4. Linguagens de Programação e Compiladores

### 📌 4.1 Software de Compilação

Na programação, para que um código seja entendido e executado pelo computador, ele precisa ser convertido de linguagem de alto nível para linguagem de máquina (binário). Existem duas formas principais para isso:

#### 🔹 Compilador
- Um **compilador** recebe um código escrito em uma linguagem de programação e o traduz completamente para um arquivo binário executável.
- O processo de **compilação** gera um arquivo final, normalmente um **.exe** no Windows, pronto para ser executado sem necessidade do código-fonte original.
- Esse método é mais rápido na execução, pois o programa já está traduzido previamente para a linguagem de máquina.

📌 **Exemplo do Processo de Compilação:**  
![Processo de Compilação](/assets/processoDeCompilacao.jpg)

#### 🔹 Interpretador
- Um **interpretador**, diferente do compilador, não gera um arquivo binário final.
- Ele lê e executa o código **linha por linha**, convertendo-o dinamicamente à medida que é requisitado.
- Linguagens como **Python e JavaScript** utilizam interpretadores.

---

Ambas as abordagens têm suas vantagens e desvantagens. Enquanto compiladores oferecem melhor desempenho, interpretadores permitem maior flexibilidade e facilidade de depuração.

🚀 **Exemplo de Linguagens Compiladas:** C, C++, Go  
💡 **Exemplo de Linguagens Interpretadas:** Python, JavaScript, Ruby  


