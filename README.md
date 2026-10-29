# Locavia

Sistema simples de gestão de vagas de garagem com aluguel mensal, desenvolvido em Python e executado pelo terminal.

O projeto utiliza funções, listas, dicionários e arquivos JSON.

## Funcionalidades

- Cadastrar vagas com identificação e valor mensal.
- Listar vagas disponíveis e ocupadas.
- Registrar a locação de uma vaga, informando nome, telefone, placa e dia de vencimento.
- Registrar o pagamento integral de uma competência mensal.
- Consultar as competências marcadas como pagas de uma vaga.
- Encerrar uma locação e liberar a vaga.
- Salvar os dados localmente em um arquivo JSON.

## Tecnologias

- Python 3.
- Módulos `json` e `os`, da biblioteca padrão do Python.
- Arquivo JSON para persistência de dados.


## Estrutura do projeto

```text
locavia/
├── main.py       # Menu e execução do programa
├── funcoes.py    # Funções de cadastro, consulta e persistência
└── dados.json    # Arquivo criado automaticamente ao salvar dados
```

## Como executar

1. Instale o Python 3, caso ainda não esteja instalado.
2. Baixe o projeto e abra um terminal na pasta que contém `main.py`.
3. Execute:

```bash
python main.py
```

Dependendo da configuração do ambiente, utilize:

```bash
python3 main.py
```

O arquivo `dados.json` é salvo na pasta de trabalho do terminal. Execute o programa sempre a partir da pasta do projeto para utilizar o mesmo arquivo de dados.

## Menu

```text
========== LOCAVIA ==========
1 - Cadastrar vaga
2 - Listar vagas
3 - Alugar vaga
4 - Registrar pagamento
5 - Consultar pagamentos
6 - Liberar vaga
0 - Sair
```

## Exemplo de uso

1. Escolha a opção `1` e cadastre uma vaga com a identificação `A01` e o valor mensal `250,00`.
2. Escolha a opção `3`, informe `A01` e preencha os dados do mensalista.
3. Escolha a opção `4`, informe a vaga e uma competência no formato `AAAA-MM`, como `2026-10`.
4. Escolha a opção `5` para consultar os pagamentos registrados.
5. Ao finalizar o aluguel, escolha a opção `6` para liberar a vaga.

## Regras implementadas

- A identificação da vaga não pode estar vazia ou se repetir exatamente.
- O valor mensal deve ser maior que zero.
- Uma vaga ocupada não pode ser alugada novamente antes de ser liberada.
- Nome, telefone e placa são obrigatórios para registrar uma locação.
- O dia de vencimento deve estar entre 1 e 28.
- A competência deve ser informada no formato `AAAA-MM`.
- Uma competência já registrada na lista de pagamentos da vaga não pode ser registrada novamente.
- A liberação da vaga exige confirmação e mantém a lista de pagamentos existente.

## Objetivo acadêmico

Praticar funções, estruturas condicionais, laços de repetição, listas, dicionários, validação de entradas e leitura e escrita de arquivos em Python.
