produtos = []
produto_estoque = []
produtos_falta = []


quantidade = int(input("quantos produtos seram cadastrados:  "))

n = 1
for i in range(quantidade):

    nome = input(f"\nindique o nome do {n}°produto: ")
    n_produto = int(input(f"quantos(as) |{nome}| tem no estoque: "))

    while n_produto < 0:
        print("a quantidade de produtos não pode ser negativo \n TEMTE NOVAMENTE")
        n_produto = int(input(f"quantos(as) |{nome}| tem no estoque: "))

    produtos.append(nome)
    produto_estoque.append(n_produto)
    n = n + 1

for i in range(len(produto_estoque)):
    if produto_estoque[i] < 5:

        produtos_falta.append(produtos[i])
        

for i in range(len(produtos)):
    print(f"\nproduto: {produtos[i]} | quantidade no estoque: {produto_estoque[i]}")

print(f"\nprodutos que estão com falta no estoque {produtos_falta}")



