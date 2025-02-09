# Aula 2 - Modelagem de Banco de Dados

## Modelo Lógico ou Relacional
Parte do princípio de que todos os dados estão armazenados em tabelas e pode ser refinado através de um processo de normalização.

### Modelos de Dados Relacional
Um Banco de Dados relacional é composto de:
- **Atributos**: Nome que identifica o dado armazenado, ou seja, o nome de cada coluna na tabela.
- **Domínio**: Tipo de dado (inteiro, caractere, decimal, data, etc.) que define o tamanho e os valores que cada atributo pode receber.
- **Tupla**: Conjunto horizontal de dados presentes nos atributos, ou seja, o registro ou linha.
- **Relações**: Conjunto de tuplas que formam uma relação (tabela). Cada relação está vinculada a um objeto específico dentro do Banco de Dados.

**OBS**: A terminologia na modelagem relacional é diferente da usada na modelagem conceitual. Antes, trabalhávamos com os termos entidade, campo e registro. No modelo relacional, utilizamos relação, atributo e tupla.

## Modelo Físico
Neste modelo, deve-se levar em consideração as limitações do Sistema Gerenciador de Bancos de Dados (SGBD) escolhido para o armazenamento dos dados. São criadas restrições (chaves primárias e estrangeiras), visualizações, índices, gatilhos e procedimentos. Um modelo físico bem estruturado resulta em dados com melhor qualidade, além de atualizações e manutenções menos complexas.

### Arquivo Físico
O arquivo físico contém mais do que apenas os dados propriamente ditos, pois armazena também o dicionário de dados, que é uma descrição da forma como os dados devem ser apresentados e manipulados. Além do arquivo com os dados, existem SGBDs que armazenam outros tipos de arquivos, como o arquivo de log das transações.

## SCHEMAS

## Modelagem Dimensional
Os modelos dimensionais abarcam um conjunto de dados desnormalizados, projetados para a recuperação de dados de um Data Warehouse. O modelo dimensional permite a visualização das mesmas informações a partir de ângulos distintos, como um cubo, em que cada face representa uma análise da informação.

### Tabela Dimensão
Conjunto de objetos que descrevem e classificam os fatos por meio de seus atributos. Por exemplo, os atributos de uma dimensão restaurante podem incluir uma hierarquia de bairro, cidade e estado, além de atributos descritivos, como o nome do restaurante.

### Tabela Fato
Geralmente englobam dados numéricos e aditivos, ou seja, dados que podem ser reunidos por soma, média ou pela aplicação de outras funções. São as principais tabelas do modelo dimensional, onde as métricas (indicativos) que interessam à empresa serão armazenadas.

### Modelos
- **Estrela (Star Schema)**: Todas as dimensões se relacionam diretamente com a tabela fato. As dimensões não são normalizadas, podendo conter dados redundantes, nulos, entre outros.
- **Floco de Neve (Snow Flake)**: As dimensões podem se relacionar com outras dimensões, além da tabela fato. Os dados são mais normalizados, ocupando menos espaço.
- **Constelação (Fact Constellation)**: Apresenta mais de uma tabela fato, utilizado para representar os fatos com um nível de detalhamento (granularidade) diferente.

## STRUCTURED QUERY LANGUAGE (SQL)
### Divisão do SQL
- **Data Definition Language (DDL)**: Comandos para criação, alteração ou exclusão dos objetos (create, drop, alter, truncate).
- **Data Manipulation Language (DML)**: Manipulação de tabelas, através de inserções, exclusões e alterações em linhas (insert, update, delete, merge).
- **Data Query Language (DQL)**: Possibilita a consulta dos dados (select).
- **Data Control Language (DCL)**: Controle de acesso dos usuários aos objetos e dados (grant, revoke).
- **Data Transaction Language (DTL)**: Permitem a confirmação ou o cancelamento de uma transação, podendo conter um ou mais comandos SQL (commit, rollback, savepoint).

## Normalização
Das 5 formas normais, aplicamos somente as três primeiras, uma vez que a sua aplicação é suficiente para resolver quase que a totalidade dos problemas de modelagem.

### Benefícios
- Minimização de redundâncias e de inconsistências.
- Melhoria na manipulação do Banco de Dados.
- Redução do tamanho físico do banco de dados.

### Primeira Forma Normal – 1FN
Regras:
- Cada tupla (linha) de dados deve ter um identificador único (Chave Primária/Estrangeira).
- Cada tupla de dados deve conter dados atômicos (não repetitivos).

### Segunda Forma Normal – 2FN
Regras:
- Estar em conformidade com a 1FN.
- Não apresentar nenhum atributo dependente de parte da chave primária.

### Terceira Forma Normal – 3FN
Regras:
- Conformidade com a 2FN.
- Não possuir nenhum atributo dependente de outros atributos que não sejam chaves da relação.

### Restrições de Integridade
- **Integridade referencial**: Presença de chave estrangeira, isto é, um atributo que faz relação com a chave primária de outra relação (tabela).
- **Restrição de unicidade**: Garantia de ausência de valores repetidos, como o atributo CPF.
- **Restrições de atributos e padrões**: Nenhuma chave primária ou estrangeira poderá conter valor nulo (not null); Valor padrão (default); Validação (check).
- **Integridade de chave**: Toda tupla apresenta um conjunto de atributos que a identifica de maneira única na relação, com a presença de chave primária.

### Chaves
- **Chave Composta**: Deriva de uma relação n:n (muitos para muitos), em que é necessário gerar uma entidade associativa. Essa nova relação produz agregação das chaves primárias de cada relação envolvida.