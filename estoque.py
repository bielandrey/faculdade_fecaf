estoque = []  

def adicionar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade: "))
    produto = [nome, preco, quantidade]
    estoque.append(produto)
    print("Produto adicionado com sucesso!")

def atualizar_produto():
    nome = input("Digite o nome do produto a atualizar: ")
    encontrado = False
    for p in estoque:
        if p[0] == nome:
            p[1] = float(input("Novo preço: "))
            p[2] = int(input("Nova quantidade: "))
            print("Produto atualizado.")
            encontrado = True
    if not encontrado:
        print("Produto não encontrado.")

def excluir_produto():
    nome = input("Digite o nome do produto a excluir: ")
    indice = -1
    for i in range(len(estoque)):
        if estoque[i][0] == nome:
            indice = i
    if indice != -1:
        del estoque[indice]
        print("Produto excluído.")
    else:
        print("Produto não encontrado.")

def visualizar_estoque():
    if len(estoque) == 0:
        print("Estoque vazio.")
    else:
        print("\n--- ESTOQUE ---")
        for p in estoque:
            print("Nome:", p[0])
            print("Preço:", p[1])
            print("Quantidade:", p[2])
            print("---------------------")

# ===================== MENU PRINCIPAL =====================
opcao = 0
while opcao != 5:
    print("\n--- MENU ESTOQUE ---")
    print("1 - Adicionar produto")
    print("2 - Atualizar produto")
    print("3 - Excluir produto")
    print("4 - Visualizar estoque")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        adicionar_produto()
    elif opcao == 2:
        atualizar_produto()
    elif opcao == 3:
        excluir_produto()
    elif opcao == 4:
        visualizar_estoque()
    elif opcao == 5:
        print("Saindo do sistema...")
    else:
        print("Opção inválida.")
