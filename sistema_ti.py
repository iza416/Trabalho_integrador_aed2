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
        # Adiciona a ocorrência na tabela hash
        tabela_hash_tipo[indice].append(ocorrencia)
        
        # empilha a descrição no histórico
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
        

# remove o primeiro chamado que entrou no sistema e altera o  status
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

# utilizei o bublle sort para ordenar por id 
def ordenar_ocorrencias():
    print("\nORDENAÇÃO POR ID")
    if not lista_geral:
        print("Sem dados para ordenar.")
        return

    
    copia_lista = list(lista_geral)
    n = len(copia_lista)
    
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if copia_lista[j]["id"] > copia_lista[j+1]["id"]:
                
                copia_lista[j], copia_lista[j+1] = copia_lista[j+1], copia_lista[j]
                
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