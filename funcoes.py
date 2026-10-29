import json
import os

ARQUIVO_DADOS = "dados.json"


def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return {"vagas": []}

    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        if "vagas" not in dados:
            dados["vagas"] = []

        return dados

    except json.JSONDecodeError:
        print("O arquivo de dados está inválido.")
        return {"vagas": []}


def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)


def buscar_vaga(dados, numero):
    for vaga in dados["vagas"]:
        if vaga["numero"] == numero:
            return vaga

    return None


def cadastrar_vaga(dados):
    numero = input("Número ou identificação da vaga: ").strip()

    if not numero:
        print("A identificação não pode ficar vazia.")
        return

    if buscar_vaga(dados, numero):
        print("Já existe uma vaga com essa identificação.")
        return

    valor_texto = input("Valor mensal do aluguel: R$ ").strip()
    valor_texto = valor_texto.replace(",", ".")

    try:
        valor = float(valor_texto)

        if valor <= 0:
            print("O valor deve ser maior que zero.")
            return

    except ValueError:
        print("Digite um valor válido.")
        return

    vaga = {
        "numero": numero,
        "valor_mensal": valor,
        "locacao": None,
        "pagamentos": []
    }

    dados["vagas"].append(vaga)
    salvar_dados(dados)

    print("Vaga cadastrada com sucesso.")


def listar_vagas(dados):
    if not dados["vagas"]:
        print("Nenhuma vaga cadastrada.")
        return

    print("\n--- VAGAS ---")

    for vaga in dados["vagas"]:
        locacao = vaga["locacao"]

        if locacao is None:
            status = "Livre"
            mensalista = "-"
        else:
            status = "Ocupada"
            mensalista = locacao["nome"]

        print(
            f'Vaga: {vaga["numero"]} | '
            f'Valor mensal: R$ {vaga["valor_mensal"]:.2f} | '
            f'Situação: {status} | '
            f'Mensalista: {mensalista}'
        )


def alugar_vaga(dados):
    numero = input("Número da vaga: ").strip()
    vaga = buscar_vaga(dados, numero)

    if vaga is None:
        print("Vaga não encontrada.")
        return

    if vaga["locacao"] is not None:
        print("Essa vaga já está ocupada.")
        return

    nome = input("Nome do mensalista: ").strip()
    telefone = input("Telefone: ").strip()
    placa = input("Placa do veículo: ").strip()
    dia_texto = input("Dia de vencimento (1 a 28): ").strip()

    if not nome or not telefone or not placa:
        print("Nome, telefone e placa são obrigatórios.")
        return

    try:
        dia_vencimento = int(dia_texto)

        if dia_vencimento < 1 or dia_vencimento > 28:
            print("O vencimento deve ser entre os dias 1 e 28.")
            return

    except ValueError:
        print("Digite um dia válido.")
        return

    vaga["locacao"] = {
        "nome": nome,
        "telefone": telefone,
        "placa": placa,
        "dia_vencimento": dia_vencimento
    }

    salvar_dados(dados)
    print("Locação registrada com sucesso.")


def registrar_pagamento(dados):
    numero = input("Número da vaga: ").strip()
    vaga = buscar_vaga(dados, numero)

    if vaga is None:
        print("Vaga não encontrada.")
        return

    if vaga["locacao"] is None:
        print("Não há uma locação ativa para essa vaga.")
        return

    competencia = input("Mês do pagamento (AAAA-MM): ").strip()

    if len(competencia) != 7 or competencia[4] != "-":
        print("Use o formato AAAA-MM, por exemplo 2026-10.")
        return

    if competencia in vaga["pagamentos"]:
        print("O pagamento dessa competência já foi registrado.")
        return

    vaga["pagamentos"].append(competencia)
    salvar_dados(dados)

    print(
        f'Pagamento de {competencia} registrado para '
        f'{vaga["locacao"]["nome"]}.'
    )


def consultar_pagamentos(dados):
    numero = input("Número da vaga: ").strip()
    vaga = buscar_vaga(dados, numero)

    if vaga is None:
        print("Vaga não encontrada.")
        return

    if not vaga["pagamentos"]:
        print("Nenhum pagamento registrado para essa vaga.")
        return

    print(f'\n--- PAGAMENTOS DA VAGA {vaga["numero"]} ---')

    for competencia in vaga["pagamentos"]:
        print(f"{competencia}: pago")


def liberar_vaga(dados):
    numero = input("Número da vaga: ").strip()
    vaga = buscar_vaga(dados, numero)

    if vaga is None:
        print("Vaga não encontrada.")
        return

    if vaga["locacao"] is None:
        print("Essa vaga já está livre.")
        return

    nome = vaga["locacao"]["nome"]
    confirmacao = input(
        f"Deseja encerrar a locação de {nome}? (s/n): "
    ).strip().lower()

    if confirmacao != "s":
        print("Operação cancelada.")
        return

    vaga["locacao"] = None
    salvar_dados(dados)

    print("Vaga liberada. O histórico de pagamentos foi mantido.")