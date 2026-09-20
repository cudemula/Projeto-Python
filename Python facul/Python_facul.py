idosos = []

def cadastrar_idoso():
    print("\n--- CADASTRO DE IDOSO ---")

    nome = input("Nome completo: ")
    idade = input("Idade: ")
    telefone = input("Telefone: ")
    observacoes = input("Observacoes: ")

    idoso = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "observacoes": observacoes
    }

    idosos.append(idoso)

    print("\nCadastro realizado com sucesso!")


def listar_idosos():
    print("\n--- IDOSOS CADASTRADOS ---")

    if len(idosos) == 0:
        print("Nenhum idoso cadastrado.")
        return

    for numero, idoso in enumerate(idosos, start=1):
        print("\nCadastro:", numero)
        print("Nome:", idoso["nome"])
        print("Idade:", idoso["idade"])
        print("Telefone:", idoso["telefone"])
        print("Observacoes:", idoso["observacoes"])


def buscar_idoso():
    print("\n--- BUSCAR IDOSO ---")

    nome = input("Digite o nome do idoso: ")

    encontrado = False

    for idoso in idosos:
        if nome.lower() in idoso["nome"].lower():
            print("\nNome:", idoso["nome"])
            print("Idade:", idoso["idade"])
            print("Telefone:", idoso["telefone"])
            print("Observacoes:", idoso["observacoes"])

            encontrado = True

    if encontrado == False:
        print("\nNenhum cadastro encontrado.")


def excluir_idoso():
    listar_idosos()

    if len(idosos) == 0:
        return

    try:
        numero = int(input("\nDigite o numero do cadastro que deseja excluir: "))

        if numero >= 1 and numero <= len(idosos):
            removido = idosos.pop(numero - 1)
            print("\nCadastro de", removido["nome"], "excluido com sucesso!")
        else:
            print("\nNumero de cadastro invalido.")

    except ValueError:
        print("\nDigite apenas numeros.")


def menu():
    while True:
        print("\n==============================")
        print(" SISTEMA DA CASA DE APOIO")
        print("==============================")
        print("1 - Cadastrar idoso")
        print("2 - Listar idosos")
        print("3 - Buscar idoso")
        print("4 - Excluir cadastro")
        print("5 - Sair")
        print("==============================")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            cadastrar_idoso()

        elif opcao == "2":
            listar_idosos()

        elif opcao == "3":
            buscar_idoso()

        elif opcao == "4":
            excluir_idoso()

        elif opcao == "5":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpcao invalida.")


menu()