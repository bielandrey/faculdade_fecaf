eventos = []

def cadastrar_evento():
    nome = input("Nome do evento: ")
    data = input("Data do evento: ")
    descricao = input("Descrição: ")
    vagas = int(input("Número máximo de vagas: "))
    evento = [nome, data, descricao, vagas, []]
    eventos.append(evento)
    print("Evento cadastrado com sucesso!")

def atualizar_evento():
    nome = input("Digite o nome do evento a atualizar: ")
    achou = False
    for e in eventos:
        if e[0] == nome:
            e[1] = input("Nova data: ")
            e[3] = int(input("Novo número de vagas: "))
            print("Evento atualizado.")
            achou = True
    if achou == False:
        print("Evento não encontrado.")

def visualizar_eventos():
    if len(eventos) == 0:
        print("Nenhum evento cadastrado.")
    else:
        print("\n--- EVENTOS DISPONÍVEIS ---")
        for e in eventos:
            vagas_restantes = e[3] - len(e[4])
            print("Nome:", e[0])
            print("Data:", e[1])
            print("Descrição:", e[2])
            print("Vagas restantes:", vagas_restantes)
            print("-------------------")

def inscrever_em_evento():
    nome = input("Nome do evento para inscrição: ")
    pessoa = input("Digite seu nome: ")
    achou = False
    for e in eventos:
        if e[0] == nome:
            achou = True
            if len(e[4]) < e[3]:
                e[4].append(pessoa)
                print("Inscrição realizada!")
            else:
                print("Não há vagas disponíveis.")
    if achou == False:
        print("Evento não encontrado.")

def ver_inscritos():
    nome = input("Nome do evento: ")
    achou = False
    for e in eventos:
        if e[0] == nome:
            achou = True
            print("Inscritos no evento", nome)
            if len(e[4]) == 0:
                print("Nenhum inscrito.")
            else:
                for inscrito in e[4]:
                    print("-", inscrito)
    if achou == False:
        print("Evento não encontrado.")

def excluir_evento():
    nome = input("Nome do evento a excluir: ")
    indice = -1
    for i in range(len(eventos)):
        if eventos[i][0] == nome:
            indice = i
    if indice != -1:
        del eventos[indice]
        print("Evento excluído.")
    else:
        print("Evento não encontrado.")


# ===================== MENU PRINCIPAL =====================
opcao = 0
while opcao != 7:
    print("\n--- MENU EVENTOS ---")
    print("1 - Cadastrar evento")
    print("2 - Atualizar evento")
    print("3 - Visualizar eventos disponíveis")
    print("4 - Inscrever-se em evento")
    print("5 - Ver inscritos de um evento")
    print("6 - Excluir evento")
    print("7 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_evento()
    elif opcao == 2:
        atualizar_evento()
    elif opcao == 3:
        visualizar_eventos()
    elif opcao == 4:
        inscrever_em_evento()
    elif opcao == 5:
        ver_inscritos()
    elif opcao == 6:
        excluir_evento()
    elif opcao == 7:
        print("Saindo do sistema...")
    else:
        print("Opção inválida.")