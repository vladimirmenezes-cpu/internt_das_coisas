tarefas = []

while True:
    print("\n--- MENU ---")
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Mostrar tarefas")
    print("0 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
        tarefa = input("Digite a tarefa que deseja remover: ")

        if tarefa in tarefas:
            tarefas.remove(tarefa)
            print("Tarefa removida com sucesso!")
        else:
            print("Essa tarefa não está na lista.")

    elif opcao == "3":
        print(f"\nTarefas: {tarefas}")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")