def cadastrar_produto(produtos):
    nome = str(input("Digite o nome do produto: "))
    descricao = str(input("Descrição: "))
    valor = float(input("Valor: R$"))
    quantidade = int(input("Quantidade: "))
    produtos.append({"nome": nome, "descrição": descricao, "valor": valor, "quantidade": quantidade})
    print("Produto cadastrado com sucesso!")

def listar_produtos(produtos):
    if not produtos:
        print("Não há produtos cadastrados.")
    else:
        print("Lista de Produtos:")
        for cont, produto in enumerate(produtos):
            print(f"{cont+1}. Nome: {produto['nome']} - Descrição: {produto['descrição']} - Preço: R${produto['valor']} - Quantidade em Estoque: {produto['quantidade']}")
            if produto['quantidade'] <1:
                print ('Não disponível')

def main():
    produtos = []
    while True:
        print("\nMenu:")
        print("1. Cadastrar novo produto")
        print("2. Listar produtos")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto(produtos)
        elif opcao == "2":
            listar_produtos(produtos)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
