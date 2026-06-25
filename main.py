import sistema_ti

def executar_sistema():
    while True:
        print("\n" + "="*50)
        print("  SISTEMA DE SUPORTE DE TI UNIVERSITÁRIO")
        print("="*50)
        print("1. Cadastrar Ocorrência")
        print("2. Listar Todas as Ocorrências")
        print("3. Atender por Ordem de Chegada")
        print("4. Buscar Ocorrências por Tipo")
        print("5. Ordenar Ocorrências por ID")
        print("6. Ver Histórico de Ações")
        print("7. Desfazer Última Ação")
        print("8. Carregar Dados em um Arquivo")
        print("9. Salvar Dados em um arquivo")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1": sistema_ti.cadastrar_ocorrencia()
        elif opcao == "2": sistema_ti.listar_ocorrencias()
        elif opcao == "3": sistema_ti.ordem_chegada()
        elif opcao == "4": sistema_ti.buscar_por_tipo_hash()
        elif opcao == "5": sistema_ti.ordenar_ocorrencias()
        elif opcao == "6": sistema_ti.historico_pilha()
        elif opcao == "7": sistema_ti.desfazer_ultima_acao()
        elif opcao == "8": sistema_ti.carregar_dados_txt()
        elif opcao == "9": sistema_ti.salvar_dados_txt()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    executar_sistema()