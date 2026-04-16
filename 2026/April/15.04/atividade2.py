from receitas import carregar_receitas, adicionar_receita, pesquisar_receita, remover_receita, atualizar_receita

carregar_receitas()


def menu_comidinhas():
    while True:
        print("\n" + "=" * 50)
        print("gerir comidinha - menu de opcoes")
        print("=" * 50)
        print("1. inserir nova receita")
        print("2. pesquisar receita por palavra-chave")
        print("3. remover receita")
        print("=" * 50)
        opcao = input("digite o numero da opcao desejada: ").strip()
        if opcao == "1":
            print("inserir nova receita")
            nome_receita = input("digite o nome da receita: ").strip().lower()
            ingredientes = []
            while True:
                ingrediente = input("digite um ingrediente (ou pressione enter para terminar): ").strip()
                if ingrediente == "":
                    break
                ingredientes.append(ingrediente.lower())
            comentario = input("digite um comentario para a receita (opcional): ").strip().lower()
            avaliacao = None
            while True:
                valor = input("digite uma avaliacao de 0 a 20 (opcional, enter para pular): ").strip()
                if valor == "":
                    break
                try:
                    avaliacao = float(valor)
                    if 0 <= avaliacao <= 20:
                        break
                    print("erro: a avaliacao deve estar entre 0 e 20.")
                except ValueError:
                    print("erro: introduza um numero valido para a avaliacao.")
            if adicionar_receita(nome_receita, ingredientes, comentario or None, avaliacao):
                print("receita adicionada com sucesso!")
        elif opcao == "2":
            print("pesquisar receita por palavra-chave")
            palavra_chave = input("digite a palavra-chave para pesquisa: ").strip().lower()
            resultados = pesquisar_receita(palavra_chave)
            if resultados:
                print(f"\nresultados para '{palavra_chave}':")
                for receita in resultados:
                    print(f"- {receita['nome']} (ingredientes: {', '.join(receita['ingredientes'])})")
                atualizar = input("deseja atualizar alguma receita encontrada? (s/n): ").strip().lower()
                if atualizar.startswith("s"):
                    nome_atualizar = input("digite o nome exato da receita que deseja atualizar: ").strip().lower()
                    novos_ingredientes = []
                    while True:
                        ingrediente = input("digite um ingrediente novo (ou enter para terminar): ").strip()
                        if ingrediente == "":
                            break
                        novos_ingredientes.append(ingrediente.lower())
                    novo_comentario = input("digite um novo comentario (ou enter para manter o anterior): ").strip().lower()
                    nova_avaliacao = None
                    while True:
                        valor = input("digite uma nova avaliacao de 0 a 20 (ou enter para pular): ").strip()
                        if valor == "":
                            break
                        try:
                            nova_avaliacao = float(valor)
                            if 0 <= nova_avaliacao <= 20:
                                break
                            print("erro: a avaliacao deve estar entre 0 e 20.")
                        except ValueError:
                            print("erro: introduza um numero valido para a avaliacao.")
                    if atualizar_receita(nome_atualizar, novos_ingredientes or None, novo_comentario or None, nova_avaliacao):
                        print("receita atualizada com sucesso!")
                    else:
                        print("nao foi possivel atualizar a receita. verifique o nome informado.")
            else:
                print("nenhuma receita encontrada com essa palavra-chave.")
        elif opcao == "3":
            print("remover receita")
            nome_receita = input("digite o nome da receita a remover: ").strip().lower()
            if remover_receita(nome_receita):
                print(f"receita '{nome_receita}' removida com sucesso!")
            else:
                print(f"receita '{nome_receita}' nao encontrada!")
        elif opcao == "4":
            break
        else:
            print("opcao invalida!")


if __name__ == "__main__":
    menu_comidinhas()