print("Sistema de Estoque")

produtos = []
def mostrar_menu():
   print("1- Cadastrar Produto")
   print("2- Listar Produtos")
   print("3- Buscar produtos")
   print("4- Alterar quantidade de produtos")
   print("5- Remover produtos")
   print("6- Sair")

def cadastrar_produto():
   nome = str(input("Digite o nome do produto: "))
   preco = float(input("Digite o preço do produto: "))
   quantidade = int(input("Digite a quantidade de produto que você quer: "))

   produto = {
   "nome": nome,
   "preco": preco,
   "quantidade": quantidade,
   }
   produtos.append(produto)


def listar_produtos():
   if produtos == []:
    print("Nenhum produto foi cadastrado")
   else:
      for produto in produtos:
         print(produto)

def buscar_produtos():
   busca_do_produto = str(input("Digite o produto que você quer encontrar: "))
   encontrado = False
   for produto in produtos:
    if produto ["nome"] == busca_do_produto:
     encontrado = True
     print(produto)

     if encontrado == False:
        print("Nenhum produto foi encontrado!")

def alterar_quantidade():
   produto_novo = str(input("Digite um novo produto: "))
   quantidade_nova = int(input("Digite a quantidade nova que você quer:"))
   produto_encontrado = False
   
   for produto in produtos:
      if produto ["nome"] == produto_novo:
        produto ["quantidade"] = quantidade_nova
        produto_encontrado = True
        print(produto)

      if produto_encontrado == False:
         print("Nenhum produto foi encontrado")


def remover_produtos():
   apagar_produto = str(input("Digite o produto que você quer remover:"))
   apagar = False


   for produto in produtos:
     if produto ["nome"] == apagar_produto:
        produtos.remove(produto)
        apagar = True
      
     if apagar == False:
         print("O produto não pode ser removido, pois não foi encontrado")
      


def finalizar_programa():
   print("Programa encerrado")

while True:
    mostrar_menu()
    opcao = int(input("Digite a opção que vc deseja: "))
    if opcao == 1:
       cadastrar_produto()

    elif opcao == 2:
       listar_produtos()

    elif opcao == 3:
       buscar_produtos()

    elif opcao == 4:
       alterar_quantidade()

    elif opcao == 5:
       remover_produtos()

    elif opcao == 6:
       finalizar_programa()
       break

    else: 
       print("Opção inválida, tente novamente")


