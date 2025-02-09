# Aula 1 (Banco de Dados Relacionais)

## Modelagem Banco de Dados

### Modelos básicos

#### Conceitual
Define quais os dados que precisam estar presentes no Banco de Dados, sem se importar com a implementação do modelo físico. Uma das técnicas mais utilizadas entre os profissionais da área é a abordagem Entidade-Relacionamento (ER), em que o modelo é representado por meio do Modelo Entidade-Relacionamento (MER).

#### Lógico
Todo modelo considerará as limitações e as características particulares do tipo de tecnologia presente no Banco de Dados escolhido.

**Características:**
- Deriva do modelo conceitual;
- Define as chaves primárias das entidades;
- Normalização até a 3ª forma normal;
- Adequação ao padrão de nomenclatura;
- Relações e atributos documentados;
- Dependente do SGBD.

#### Físico
Elaborado a partir do modelo lógico; Pode variar segundo o SGBD; Pode ter tabelas físicas (log);

```sql
create table cliente( 
    codigo int, 
    nome varchar(100), 
    endereco varchar(100), 
    codCidade int
);