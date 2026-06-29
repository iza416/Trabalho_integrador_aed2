import os

Arquivo_dados_txt = "ocorrencias.txt"
lista_geral = []       
insercao_fila_chegada = []      
registro_pilha_historico = []   


tabela_hash_tipo = [[] for _ in range(10)]


def calcular_hash(tipo_string):
   
    soma = sum(ord(char) for char in tipo_string.lower())
    return soma % 10


def cadastrar_ocorrencia():
    print("\nCADASTRO DE OCORRÊNCIA")
    try:
        
        id = int(input("ID da Ocorrência: "))
        solicitante = input("Nome do Solicitante: ")
        tipo = input("Tipo/Categoria (Ex: internet, computador, projetor...): ").strip()
        descricao = input("Descrição do problema: ")
        prioridade = int(input("Prioridade (1-Baixa, 2-Média, 3-Alta): "))
        data = input("Data de Abertura (DD/MM/AAAA): ")
        
       
        ocorrencia = {
            "id": id,
            "solicitante": solicitante,
            "tipo": tipo,
            "descricao": descricao,
            "prioridade": prioridade,
            "status": "Aberto",
            "data": data
        }

       
        
        
        lista_geral.append(ocorrencia)
        
        
        insercao_fila_chegada.append(ocorrencia)
        
       
        indice = calcular_hash(tipo)
        
        tabela_hash_tipo[indice].append(ocorrencia)
        
        
        registro_pilha_historico.append(f"Cadastro da ocorrência ID {id}")

        print(f" Chamado ID {id} enviado com sucesso!")
    except ValueError:
        print(" Erro: ID e Prioridade precisam ser números inteiros!")


def listar_ocorrencias():
    print("\n LISTAGEM GERAL")
    if not lista_geral:
        print("Nenhum chamado registrado.")
        return
        
    for occ in lista_geral:
        print(f"[ID: {occ['id']}] Categoria: {occ['tipo']} | Solicitante: {occ['solicitante']}")
        print(f"Descrição: {occ['descricao']} | Status: {occ['status']}")
        


def ordem_chegada():
    print("\nATENDIMENTO POR ORDEM DE CHEGADA")
    
    if len(insercao_fila_chegada) == 0:
        print("Fila de atendimento vazia!")
        return
        
    chamado_atendido = insercao_fila_chegada.pop(0)
    chamado_atendido["status"] = "Resolvido"
    
    
    registro_pilha_historico.append(f"Atendimento da ocorrência ID {chamado_atendido['id']}")
    
    print(f"Solicitante: {chamado_atendido['solicitante']} | Problema: {chamado_atendido['descricao']}")


def buscar_por_tipo_hash():
    print("\nBUSCA POR TIPO")
    tipo_busca = input("Digite o tipo que quer buscar (Ex: computador, projetor, documentação, internet...): ").strip()
    
    
    indice = calcular_hash(tipo_busca)
    local = tabela_hash_tipo[indice]
    
    encontrados = False
    for occ in local:
       
        if occ["tipo"].lower() == tipo_busca.lower():
            print(f" Encontrado: ID {occ['id']} - Solicitante: {occ['solicitante']} | Status: {occ['status']}")
            encontrados = True
            
    if not encontrados:
        print(f"Nenhum chamado encontrado para o tipo '{tipo_busca}'.")


def ordenar_ocorrencias():
    print("\nORDENAÇÃO POR ID")
    if not lista_geral:
        print("Sem dados para ordenar.")
        return

    
    copia_lista = list(lista_geral)
    n = len(copia_lista)
    
    
    for i in range(1, n):
        for i in range(1, n):
            variavel_chave = copia_lista[i]
            j = i - 1
            
            while j >= 0 and copia_lista[j]["id"] > variavel_chave["id"]:
                copia_lista[j + 1] = copia_lista[j]
                j -= 1
                
            copia_lista[j + 1] = variavel_chave
                
    print(" Chamados ordenados por ID:")
    for occ in copia_lista:
        print(f"ID: {occ['id']} | Tipo: {occ['tipo']} | Solicitante: {occ['solicitante']}")


def historico_pilha():
    print("\nHISTÓRICO DE AÇÕES")
    if not registro_pilha_historico:
        print("Nenhuma ação no histórico.")
        return
        
    
    for acao in reversed(registro_pilha_historico):
        print(f" {acao}")


def desfazer_ultima_acao():
    print("\n DESFAZER ÚLTIMA AÇÃO")
    if not registro_pilha_historico:
        print("Não há ações para desfazer.")
        return
        
    
    ultima_acao = registro_pilha_historico.pop()
    print(f" Ação removida: \"{ultima_acao}\"")
    
    
def salvar_dados_txt():
    print("\nSALVANDO DADOS EM ARQUIVO .TXT")
    try:
        with open(Arquivo_dados_txt, "w", encoding="utf-8") as arquivo:
            for occ in lista_geral:
                linha = f"{occ['id']};{occ['solicitante']};{occ['tipo']};{occ['descricao']};{occ['prioridade']};{occ['status']};{occ['data']}\n"
                arquivo.write(linha)
        print(f"Sucesso: {len(lista_geral)} ocorrência(s) salva(s)'{Arquivo_dados_txt}'.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}") 
        
def carregar_dados_txt():
    print("\nCARREGANDO DADOS DO ARQUIVO")
    if not os.path.exists(Arquivo_dados_txt):
        print(f"O arquivo '{Arquivo_dados_txt}' ainda não existe. Nenhum dado foi carregado.")
        return

    try:
        
        lista_geral.clear()
        insercao_fila_chegada.clear()
        for lista in tabela_hash_tipo:
            lista.clear()

        with open(Arquivo_dados_txt, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                
                
                partes = linha.split(";")
                
                ocorrencia = {
                    "id": int(partes[0]),
                    "solicitante": partes[1],
                    "tipo": partes[2],
                    "descricao": partes[3],
                    "prioridade": int(partes[4]),
                    "status": partes[5],
                    "data": partes[6]
                }
                
                
                lista_geral.append(ocorrencia)
                
                
                if ocorrencia["status"] == "Aberto":
                    insercao_fila_chegada.append(ocorrencia)
                
                
                indice_hash = calcular_hash(ocorrencia["tipo"])
                tabela_hash_tipo[indice_hash].append(ocorrencia)
                
        print(f"Sucesso: {len(lista_geral)} ocorrência(s) carregada(s)!")
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")        
    
def gerar_relatorio_ordenado():
    print("\nGERANDO RELATÓRIO...")

    if not lista_geral:
        print("Nenhuma ocorrência cadastrada.")
        return

    copia_lista = list(lista_geral)

    n = len(copia_lista)

    for i in range(1, n):
        chave = copia_lista[i]
        j = i - 1

        while j >= 0 and copia_lista[j]["id"] > chave["id"]:
            copia_lista[j + 1] = copia_lista[j]
            j -= 1

        copia_lista[j + 1] = chave

    with open("relatorio_final.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("RELATÓRIO DE OCORRÊNCIAS\n")
        arquivo.write("=" * 60 + "\n\n")

        for occ in copia_lista:
            arquivo.write(f"ID: {occ['id']}\n")
            arquivo.write(f"Solicitante: {occ['solicitante']}\n")
            arquivo.write(f"Tipo: {occ['tipo']}\n")
            arquivo.write(f"Descrição: {occ['descricao']}\n")
            arquivo.write(f"Prioridade: {occ['prioridade']}\n")
            arquivo.write(f"Status: {occ['status']}\n")
            arquivo.write(f"Data: {occ['data']}\n")
            arquivo.write("-" * 60 + "\n")

    print("Relatório gerado com sucesso em 'relatorio_final.txt'.")