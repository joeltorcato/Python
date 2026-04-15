from receitas import (
    carregar_receitas,
    adicionar_receita,
    pesquisar_receita,
    remover_receita,
    atualizar_receita,
)

# Carregar as receitas existentes antes de iniciar o menu
carregar_receitas()

def menu_comidinhas():
    
    while True:
        # Exibir as opções disponíveis para gestão de receitas
        print("\n" + "="*50)
        print("GERIR comidinha - Menu de Opções")
        print("="*50)
        print("1. Inserir nova receita")
        print("2. pesquisar receita por palavra-chave")
        print("3. Remover receita")
        print("="*50)
        
        # Solicitar ao utilizador que escolha uma opção
        opcao = input("Digite o número da opção desejada: ")
        
        # Opção 1: Inserir receita
        if opcao == "1":
            print("Inserir nova receita")
            nome_receita = input("Digite o nome da receita: ")
            ingredientes = []

            while True:
                ingrediente = input("Digite um ingrediente (ou pressione ENTER para terminar): ")
                if ingrediente.strip() == "": # aqui eu verifico se o utilizador pressionou ENTER sem digitar nada, indicando que terminou de inserir ingredientes
                    break
                ingredientes.append(ingrediente.strip())

            comentario = input("Digite um comentário para a receita (opcional): ")
            avaliacao = None

            while True:
                valor = input("Digite uma avaliação de 0 a 20 (opcional, ENTER para pular): ")
                if valor.strip() == "":
                    break
                try:
                    avaliacao = float(valor)
                    if 0 <= avaliacao <= 20:
                        break
                    print("Erro: A avaliação deve estar entre 0 e 20.")
                except ValueError:
                    print("Erro: introduza um número válido para a avaliação.")

            if adicionar_receita(nome_receita, ingredientes, comentario, avaliacao):
                print("Receita adicionada com sucesso!")

        elif opcao == "2":
            print("Pesquisar receita por palavra-chave")
            palavra_chave = input("Digite a palavra-chave para pesquisa: ")
            resultados = pesquisar_receita(palavra_chave)

            if resultados:
                print(f"\nResultados para '{palavra_chave}':")
                for receita in resultados:
                    print(f"- {receita['nome']} (ingredientes: {', '.join(receita['ingredientes'])})")

                atualizar = input("Deseja atualizar alguma receita encontrada? (s/n): ")
                if atualizar.lower().startswith("s"): # aqui eu verifico se a resposta do utilizador começa com "s" (sim), indicando que ele deseja atualizar uma receita
                    nome_atualizar = input("Digite o nome exato da receita que deseja atualizar: ")
                    novos_ingredientes = []
                    while True:
                        ingrediente = input("Digite um ingrediente novo (ou ENTER para terminar): ")
                        if ingrediente.strip() == "":
                            break
                        novos_ingredientes.append(ingrediente.strip())

                    novo_comentario = input("Digite um novo comentário (ou ENTER para manter o anterior): ")
                    nova_avaliacao = None
                    while True:
                        valor = input("Digite uma nova avaliação de 0 a 20 (ou ENTER para pular): ")
                        if valor.strip() == "":
                            break
                        try:
                            nova_avaliacao = float(valor)
                            if 0 <= nova_avaliacao <= 20:
                                break
                            print("Erro: A avaliação deve estar entre 0 e 20.")
                        except ValueError:
                            print("Erro: introduza um número válido para a avaliação.")

                    if atualizar_receita(nome_atualizar, novos_ingredientes or None, novo_comentario or None, nova_avaliacao):
                        print("Receita atualizada com sucesso!")
                    else:
                        print("Não foi possível atualizar a receita. Verifique o nome informado.")
            else:
                print("Nenhuma receita encontrada com essa palavra-chave.")

        elif opcao == "3":
            print("Remover receita")
            nome_receita = input("Digite o nome da receita a remover: ")
            if remover_receita(nome_receita):
                print(f"Receita '{nome_receita}' removida com sucesso!")
            else:
                print(f"Receita '{nome_receita}' não encontrada!")

        elif opcao == "4":
            break
        else:
            print("Opção inválida!")