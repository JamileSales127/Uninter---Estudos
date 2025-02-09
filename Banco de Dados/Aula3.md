# Aula 3 - Construção de Estruturas de Dados

## SQL DATA TYPES
Todo objeto que tem a função de armazenamento de dados sempre terá um tipo de dado associado ao mesmo.

### MySQL tipos de dados suportados
- Tipo numérico.
- Tipo cadeia de caracteres ou valor string.
- Tipo valor temporal.

Os objetos que têm tipos de dados associados são:
- Colunas em tabelas e exibições;
- Parâmetros em procedimentos;
- Variáveis;
- Funções que retornam um ou mais valores de dados de um tipo de dado específico.

A atribuição de um tipo de dado a um objeto define as características de uma coluna, isto é:
- O tipo de dado contido pelo objeto;
- O comprimento ou tamanho do valor a ser armazenado (bits ou bytes);
- A precisão e a escala do número (apenas dados numéricos):
  - **Precisão**: Refere-se ao total de dígitos em um número;
  - **Escala**: É o número de dígitos à direita da casa decimal.

### Tipo Numérico
Podem assumir:
- Valores inteiros: `bit`, `tinyint`, `smallint`, `int`, `mediumint` e `bigint`.
- Ponto flutuante: `float` e `double`.
- Ponto fixo: Representados pelo tipo de dado `decimal`.

### Tipo Cadeia de Caracteres ou Valor String
Os valores string são subdivididos em duas categorias:
- Valores binários: `binary`, `varbinary` e `blob` (16 bits, mais 2 de controle).
- Valores não binários: Representados pelos tipos de dados `char`, `nchar`, `varchar`, `nvarchar` e `text`.

### Tipo Valor Temporal
Em termos de comprimento, eles requerem um tamanho de armazenamento de 1 a 8 bytes.
- `date`: Utilizado exclusivamente para datas sem a declaração de hora.
- `time`: Apenas para hora. Formato padrão: hh:mm:ss (hora:minuto:segundo).
- `datetime`: Utilizado para valores de data e hora, baseando-se no calendário e hora do relógio. Não considera o fuso horário.
- `timestamp`: Semelhante ao `datetime`, porém baseado no fuso horário.
- `year`: Armazena apenas o ano, podendo utilizar 2 ou 4 dígitos.

## SQL PK, FK e UK
### Declarando uma chave primária (PK) em uma tabela:
```sql
create table estado (
    id integer not null,
    descricao varchar(100),
    sigla char(02),
    primary key(id)
);
```
### Declarando chaves estrangeiras (FK) em uma tabela:
```sql
create table cidade (
    id integer not null,
    estado_id integer not null,
    descricao varchar(150),
    primary key(id),
    foreign key(estado_id) references estado(id) on delete no action on update no action
);
```
### Declaração de chaves únicas (Unique Key – UK) em uma tabela:
```sql
create table entregador (
    id integer not null,
    cidade_id integer not null,
    cnh integer unique,
    nome varchar(150)
);
```
## ALTERAÇÕES, AUTO INCREMENT, ENTRE OUTROS
### Alter Table
A sintaxe do `ALTER TABLE` sempre é acompanhada por um dos seguintes comandos:
- **Add**: Adiciona uma coluna em uma tabela existente;
- **Change**: Renomeia e altera as definições de uma coluna existente (nome, tipo da coluna, entre outros);
- **Modify**: Modifica as definições de uma coluna existente, mas não permite alterar o seu nome;
- **Alter**: Altera uma coluna existente em uma tabela;
- **Drop**: Exclui uma coluna pertencente a uma tabela.

Sintaxe:
```sql
ALTER TABLE ntabela ADD ncoluna tipodado(tamanho);
```
Na inclusão de novas colunas, não é possível adicionar a restrição `NOT NULL` em uma tabela existente que já possua dados armazenados.

## Propriedades Especiais
- **Unsigned**: Essa propriedade não permite o recebimento de valores negativos (inferior a zero) para colunas do tipo de dado inteiro.
- **Zerofill**: Insere o autopreenchimento com zeros nos espaços ociosos, ou seja, que não estão sendo utilizados. É importante ressaltar que a declaração `ZEROFILL` em uma coluna, automaticamente a torna `UNSIGNED` (apenas valores positivos).
- **Auto_increment**: Propriedade bastante utilizada em chaves primárias, cuja característica é gerar automaticamente um número inteiro e incrementá-lo a partir da inclusão de uma nova linha, não havendo a inclusão manual desse valor na coluna.

## SQL Constraints
A restrição é utilizada para limitar e padronizar o recebimento de um dado, evitando, assim, que dados inválidos sejam inseridos no banco. As restrições dividem-se em:
- **Restrição em nível de coluna**: Fazendo referência a uma única coluna da tabela.
- **Restrição em nível de tabela**: Referenciam uma ou mais colunas da tabela, especificando as colunas às quais se aplicam.

## SQL na Prática
### Comandos Úteis para Iniciar
- Apresentando os Bancos de Dados existentes: `SHOW`
- Acessando um Banco de Dados (conexão): `USE`
- Descobrindo o Banco de Dados que você está conectado: `SELECT`
- Apresentando o dicionário de dados de uma tabela: `DESCRIBE`

### Principais Comandos
- **Criando um Banco de Dados**:
  ```sql
  CREATE DATABASE [IF NOT EXISTS] bdados;
  ```
  Dica: Podemos incrementar a query, referente ao `CREATE`, com o objetivo de realizar uma pré-verificação da existência de um Banco de Dados com o mesmo nome. Para isso, basta utilizar o comando `IF NOT EXISTS`.

- **Incluindo dados na tabela**:
  ```sql
  INSERT INTO ntabela (coluna1, coluna2, ...) VALUES (valor1, valor2, ...);
  ```

- **Consultando dados na tabela**:
  ```sql
  SELECT * FROM ntabela ORDER BY coluna ASC|DESC;
  ```
  Para apresentar os dados em uma determinada ordem (ascendente ou descendente), utilizamos a expressão `ORDER BY`.

- **Excluindo objetos em SQL**:
  ```sql
  DROP TABLE ntabela;
  ```