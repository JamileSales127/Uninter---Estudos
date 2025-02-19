# Aula 4 - Manipulação de Estruturas de Dados

## Inclusão de Registros
Para realizarmos a tarefa de inserção de dados em uma tabela, utilizamos o comando `INSERT` da Structured Query Language (SQL). O comando `INSERT` também permite a inserção de dados em colunas específicas de uma tabela, desde que sejam respeitadas as restrições de cada coluna, como por exemplo, uma chave primária com a declaração da cláusula `AUTO_INCREMENT` não deve estar incluída no `INSERT`.

### Trabalhando com Chave Estrangeira
É necessário que o valor exista em sua tabela de origem.

## Junção de Tabelas
### Join (junção)
- Usar a cláusula `ON` para fazer a ligação entre as tabelas e deixar as demais condições para a cláusula `WHERE`.
- O uso do `JOIN` é uma junção explícita e o uso do `WHERE` é uma junção implícita. Isso significa que podemos definir dentro do `WHERE` uma condição de junção, omitindo o comando `JOIN` (implícito).
- Os tipos `FULL JOIN` e `CROSS JOIN` geram impacto no desempenho da consulta, dessa forma, devem ser usados somente quando necessário.

### Inner Join
O `INNER JOIN` ou junção natural, por meio de operadores de comparação em uma condição, realiza a combinação de linhas de duas tabelas e retorna apenas as que satisfazem a condição definida no `JOIN`.
```sql
SELECT nomecidade, nomeEstado, sigla 
FROM cidade 
INNER JOIN estado ON cidade.estadoID = estado.id;
```

### Outer Join
Apresenta todas as linhas de uma tabela, mesmo quando elas não satisfazem a condição definida. Logo, permite obter a totalidade das linhas de uma tabela, mesmo sem existir uma linha correspondente na outra tabela.

#### Left Outer Join
Satisfazendo ou não a condição de junção entre as tabelas, todas as linhas da tabela à esquerda do `JOIN` serão incluídas no resultado.
Simulação 1 (`LEFT JOIN`): projetar o nome da cidade, o estado por extenso e a unidade federativa das cidades que possuem ou não estado informado.
```sql
SELECT nomecidade, nomeEstado, sigla 
FROM cidade 
LEFT JOIN estado ON cidade.estadoID = estado.id;
```

#### Right Outer Join
O `RIGHT JOIN` retorna todas as linhas da tabela da direita e apenas as linhas correspondentes da tabela da esquerda.
Simulação (`RIGHT JOIN` inclusive): projetar o nome da cidade, o nome do estado e a sigla do estado que possui ou não cidades relacionadas.
```sql
SELECT nomecidade, nomeEstado, sigla 
FROM cidade 
RIGHT JOIN estado ON cidade.estadoID = estado.id;
```

#### Full Outer Join
Apresenta todas as linhas de ambas as tabelas envolvidas no `JOIN`, mesmo as que não estão relacionadas com a outra tabela.
Simulação: projetar o nome da cidade, o estado por extenso e a sigla dos estados que possuem ou não cidades relacionadas e as cidades que não possuem estados relacionados.
```sql
SELECT nomecidade, nomeEstado, sigla 
FROM cidade 
FULL JOIN estado ON cidade.estadoID = estado.id;
```

### Cross Join
O `CROSS JOIN` gera um resultado formado por todas as combinações possíveis de uma linha da primeira tabela com uma linha da segunda tabela.
Simulação: a empresa criou um questionário contendo diversas perguntas para serem respondidas por todos os funcionários. Baseado nas tabelas Pergunta e Funcionário é necessário cruzarmos essas duas tabelas, realizando combinações e, assim, gerando para cada funcionário todas as perguntas contidas na tabela Pergunta.
```sql
SELECT nomefunc, pergunta 
FROM pergunta 
CROSS JOIN funcionario;
```

### Self Join
A tabela se relacionando com ela mesma. Nesses casos, gera-se uma cópia da tabela e, obrigatoriamente, usamos um alias (apelido) de tabela para distinguir uma tabela da outra.
Simulação: cada funcionário possui um gerente e, obviamente, o gerente exerce o papel de funcionário, ou seja, está registrado na tabela Funcionário. Como poderíamos projetar o nome do funcionário e o nome do gerente correspondente em uma mesma consulta?
```sql
SELECT funcionario.nomefunc, gerente.nomeFunc AS 'gerente' 
FROM funcionario 
INNER JOIN funcionario AS gerente ON funcionario.gerente = gerente.matricula 
ORDER BY funcionario.nomefunc;
```

### Junção com Várias Tabelas
```sql
SELECT nomeFunc, nomecidade, nomeEstado 
FROM funcionario 
INNER JOIN cidade ON funcionario.cidadeID = cidade.id 
INNER JOIN estado ON cidade.estadoID = estado.id 
ORDER BY nomeFunc;
```

## Exclusão e Modificação de Registros
A melhor prática no uso do comando `DELETE` é a inclusão da cláusula `WHERE`, ou seja, aplicando um filtro para limitarmos o impacto sofrido pelos registros dentro de uma base de dados.

## Restrição de Consultas

### Operadores Lógicos
- **OR**: Teste lógico entre dois operandos. Retorna verdadeiro (true) caso um dos operandos seja verdadeiro.
- **AND**: Teste lógico entre dois operandos. Retorna verdadeiro (true) se todos os operandos são verdadeiros.
- **NOT**: Testa se o operando é verdadeiro (true) e retorna falso (false).

### Operadores Relacionais
- **<> ou !=**: Diferente.
- **IN**: Operando da esquerda pertence ao da direita.
- **NOT IN**: Operando não pertence ao operador da direita.
- **LIKE**: Operando da esquerda for compatível com o da direita.
- **BETWEEN / AND**: Operando da esquerda estiver entre o segundo e o terceiro operando.
- **IS NULL**: Operando for nulo.
- **EXISTS**: Subconsulta retornando no mínimo uma linha.
- **ANY**: Comparação com qualquer elemento do conjunto.
- **ALL**: Comparação com todos os elementos do conjunto.

### Order By
A cláusula `ORDER BY` tem por objetivo ordenar o resultado de um `SELECT`. Tal ordenação poderá ser apresentada de forma ascendente (`ASC`) ou descendente (`DESC`), sendo que a declaração `ASC` é padrão, podendo ser omitida. Além disso, o `ORDER BY` será sempre a última cláusula a ser declarada. O `ORDER BY` ainda permite que possamos ordenar a consulta sem declararmos o nome da coluna, usando apenas a sua posição no `SELECT`.
```sql
SELECT nome, salario, email 
FROM cliente 
ORDER BY 3 ASC;
```

## Outros Comandos e Recomendações

### Alias (Apelido das Tabelas e Colunas)
Recurso que permite renomear uma tabela ou uma coluna. Utiliza-se alias nas tabelas para simplificar o nome das tabelas e/ou reduzir a escrita dos comandos.
```sql
-- Sem alias
SELECT nomeFunc, salarioFunc, salarioFunc * 1.10 
FROM funcionario;

-- Com alias
SELECT nomeFunc AS 'Nome do Funcionário', 
       salarioFunc AS 'Salário atual', 
       salarioFunc * 1.10 AS 'Novo salário' 
FROM funcionario;
```

### Limit
A cláusula `LIMIT` é utilizada para determinar o número de linhas que devem ser retornadas na consulta.
```sql
SELECT * 
FROM funcionario 
LIMIT 3, 2;
```

### Distinct
A cláusula `DISTINCT`, quando usada no `SELECT`, elimina as linhas repetidas, ou seja, se houver duas ou três linhas iguais, somente uma irá retornar no resultado.
Simulação 1: projetar o nome dos clientes por ordem alfabética, comparando o uso do `DISTINCT`.
```sql
SELECT nome 
FROM cliente 
ORDER BY nome;

SELECT DISTINCT nome 
FROM cliente 
ORDER BY nome;
```

### Case
Em consultas SQL podem ocorrer situações em que seja necessário realizarmos algum tipo de teste lógico.
```sql
SELECT nomeFunc, 
       CASE 
           WHEN sexoFunc = 'M' THEN 'Masculino' 
           WHEN sexoFunc = 'F' THEN 'Feminino' 
           ELSE 'Outros' 
       END AS 'Genero' 
FROM funcionario;
```

### Union e Union All
Permite que a consulta realizada em vários `SELECTs` seja exibida em um único resultado. Para isso, necessita atender os seguintes requisitos:
- As colunas devem ser do mesmo tipo, isto é, `VARCHAR` com `VARCHAR`, `INT` com `INT`, e assim sucessivamente.
- Todos os comandos `SELECT` devem possuir o mesmo número de colunas.

Por padrão, o `UNION` elimina do resultado as linhas duplicadas. Usa-se a cláusula `ALL` para que elas sejam incluídas no resultado.
```sql
-- Usando apenas o UNION
SELECT nome, dataNascimento 
FROM cliente 
UNION 
SELECT nomeFunc, NascFunc 
FROM funcionario;

-- Usando a cláusula ALL (linhas duplicadas)
SELECT nome, dataNascimento, 'cliente' 
FROM cliente 
UNION ALL 
SELECT nomeFunc, NascFunc, 'funcionario' 
FROM funcionario 
ORDER BY 1;
```

### Recomendações – Boas Práticas
- Não use o asterisco (*) no comando `SELECT`, pois isso gera um impacto no desempenho da consulta.
- Sempre que possível use filtros (`WHERE`) nos comandos `DELETE` e `UPDATE`.
- Evite criar um `INSERT` contendo muitas linhas, pois esse processo aumenta muito o tamanho do Banco de Dados.