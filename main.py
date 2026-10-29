from funcoes import (
    carregar_dados,
    cadastrar_vaga,
    listar_vagas,
    alugar_vaga,
    registrar_pagamento,
    consultar_pagamentos,
    liberar_vaga,
)


def mostrar_menu():
    print("\n========== LOCAVIA ==========")
    print("1 - Cadastrar vaga")
    print("2 - Listar vagas")
    print("3 - Alugar vaga")
    print("4 - Registrar pagamento")
    print("5 - Consultar pagamentos")
    print("6 - Liberar vaga")
    print("0 - Sair")


def executar():
    dados = carregar_dados()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_vaga(dados)

        elif opcao == "2":
            listar_vagas(dados)

        elif opcao == "3":
            alugar_vaga(dados)

        elif opcao == "4":
            registrar_pagamento(dados)

        elif opcao == "5":
            consultar_pagamentos(dados)

        elif opcao == "6":
            liberar_vaga(dados)

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    executar()