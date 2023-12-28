class Utilizador:

    #Construtor
    def __init__(self, nome, interesses, artigos_disponiveis):
        self.nome = nome
        self.interesses = interesses
        self.artigos_disponiveis = artigos_disponiveis
        self.pycoins = 50
        self.avaliacao = 0


    #Altera os interesses e/ou os artigos de um utilizador
    def editar_conta(self, novos_interesses, novos_artigos):
        self.interesses = novos_interesses
        self.artigos = novos_artigos

    #Adiciona uma nova avaliação, podendo incluir um comentário
    def deixar_avaliacao(self, estrelas, comentario):
        self.estrelas = estrelas
        self.comentario = comentario
        avaliacao = {'usuario': usuario, 'estrelas': estrelas, 'comentario': comentario}
        self.avaliacao.append(avaliacao)
        print(f"Avaliação deixada por {self.utilizador}: {estrelas} estrelas - {comentario}")

    #Apresenta todas as avaliações e comentários
    def listar_avaliacoes(self):
        print(f"Avaliações de {self.nome}:")
        for avaliacao in self.avaliacoes:
            print(f"Estrelas: {avaliacao['estrelas']}, Comentário: {avaliacao['comentario']}")

    #Apresenta todos os interesses
    def mostrar_interesses(self):
        print("Introduza um nome de utilizador para consultar os seus interesses:")
        mostrar_interesses = input("")
        print(f"Interesses de {self.mostrar_insteresses}: {', '.join(self.interesses)}")

    #Apresenta todos os artigos
    def mostrar_artigos(self):
        print(f"Artigos disponíveis para troca por {self.username}:")
        for artigo, preco in self.artigos_disponiveis.items():
            print(f"  - {artigo}: {preco} PyCoins")
            
    #Altera o número de pycoins
    def alterar_pycoins(self, numero_pycoins):
        self.numero_pycoins = numero_pycoins
        print(f"{self.utilizador} agora possui {self.pycoins} PyCoins.")

    #Apresenta o número de pycoins
    def mostrar_pycoins(self):
        print("Introduza um nome de utilizador para consultar os seus Pycoins:")
        mostrar_pycoins_nome = input("")
        print(f"{self.nome} tem {self.pycoins} PyCoins.")
        

class Artigos:

    #Construtor
    def __init__(self, nome, preco, tipologia, quantidade):
        self.nome = nome
        self.preco = preco
        self.tipologia = tipologia
        self.quantidade = quantidade

    #Altera o nome de um artigo para o novo nome recebido
    def editar_nome(self, nome):
        self.nome = nome

    #Altera o preço de um artigo de acordo com a percentagem dada
    def ajustar_preco(self, percentagem_alteracao):
        self.percentagem_alteracao = percentagem_alteracao


    #Altera o preço para o novo preço recebido
    def editar_preco(self, preco):
        pass

    #Apresenta o preço do artigo
    def mostrar_preco(self):
        pass

    #Altera a quantidade
    def editar_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade

    #Apresenta a quantidade do artigo
    def mostrar_quantidade(self):
        pass

    #Altera a tipologia
    def editar_tipo (self, novo_tipo):
        self.tipo = novo_tipo

    #Apresenta a tipologia do artigo
    def mostrar_tipo (self):
        pass

class FeiraVirtual:

    #Construtor
    def __init__(self):
        self.utilizador = []
        self.artigos_disponíveis = {}

    #Adiciona um novo utilizador recebendo o nome, interesses e artigos
    def registar_utilizador (self, nome, interesses, artigos_disponiveis):
        novo_utilizador = Utilizador(nome, interesses, artigos_disponiveis)
        self.utilizador.append(novo_utilizador)

    #Importa uma lista de utilizadores a partir de um ficheiro
    def importar_utilizadores(self):
        Utilizadores = open("biblioteca.txt","r")
        linhas = Utilizadores.split("\n")[1:]
        for linha in linhas:
        partes = linha.split(";")
        nome = partes[0]
        interesses = eval(partes[1]) if partes[1] else []
        artigos = eval(partes[2])

        FeiraVirtual.registar_utilizador(nome, interesses, artigos)

    #Importa uma lista de artigos a partir de um ficheiro
    def eliminar_conta(self, nome_utilizador):
        self.nome_utilizador = nome_utilizador

    #Apresenta todos os artigos disponíveis ordenados por preço
    def listar_artigos(self):
        pass

    #Efetua uma compra de um artigo. O comprador e o vendedor são os nomes de dois utilizadores registados
    def comprar_artigo(self, comprador, vendedor, artigo):
        self.comprador = comprador
        self.vendedor = vendedor
        self.artigo = artigo

    #Calcula a reputação de um utilizador com base nas suas avaliações
    def calcular_reputacao(self, utilizador):
        self.utilizador = utilizador

    #Coloca um artigo à venda. O vendedor é o nome de um utilizador
    def colocar_artigo_para_venda(self, vendedor, artigo, preco):
        self.vendedor = vendedor
        self.artigo = artigo
        self.preco = preco


    #Encontra os nomes de utilizadores interessados no artigo recebido
    def encontrar_compradores_interessados(self, artigo):
        self.artigo = artigo

    #Exporta a lista de artigos para um ficheiro ordenados por quantidade
    def exportar_artigos_preco(self, nome_ficheiro):
        self.ficheiro = nome_ficheiro

    #Exporta a lista de utilizadores para um ficheiro ordenados por reputação
    def exportar_utilizadores(self):
        pass

class Mercado:

    #Construtor
    def __init__(self):
        self.mercado = Mercado()
    #Adiciona um novo artigo
    def adicionar_artigo(self, artigo):
        self.artigo = artigo

    #Elimina um artigo
    def remover_artigo(self, artigo):
        self.artigo = artigo

    #Mostra o nome, preço e quantidade do artigo recebido
    def mostrar_artigo(self, artigo):
        self.artigo = artigo


def main():
    print("Bem-vindo/a à Feira Virtual. Pretende aceder a:\n1 - Utilizadores\n2 - Artigos\n3 - Mercado")
    opcao1 = int(input())
    if opcao1 == 1:
        print("Pretende aceder a:\n1 – Registo de utilizadores\n2 – Alteração de um utilizador\n3 – Eliminação de conta de um utilizador\n4 – Lista de utilizadores\n5 – Mostrar artigos de um utilizador\n6 – Mostrar interesses de um utilizador\n7 – Mostrar Pycoins de um utilizador\nV – Voltar atrás\nS – Sair")
        opcao11 = input("")
        if opcao11 == 1:
            print("1 – Registo manual\n2 – Registo por ficheiro")
            opcao12 = input("")
            if opcao12 == 1:
                pass
            if opcao12 == 2:
                while opcao12 < 1 or opcao12 > 2:
                    opcao12 = input("")
        elif opcao11 == 2:
            pass
        elif opcao11 == 3:
            pass
        elif opcao11 == 4:
            pass
        elif opcao11 == 5:
            print("Introduza um utilizador para consultar os seus artigos:")
            opcao15 = input("")
            print("Artigo: n, Preço: n, Quantidade: n")
        elif opcao11 == 6:
            pass
        elif opcao11 == 7:
            pass
        elif opcao21 := "V":
            print("Bem-vindo/a à Feira Virtual. Pretende aceder a:\n1 - Utilizadores\n2 - Artigos\n3 - Mercado")
            opcao1 = input("")
        elif opcao21 := "S":
            quit()
        else:
            print("Opção inálida")
            quit()

    elif opcao1 == 2:
        print("Pretende aceder a: \n1 – Mostrar preço de um artigo\n2 – Mostrar quantidade de um artigo\n3 – Mostrar tipo de um artigo\nV – Voltar atrás\nS – Sair")
        opcao21 = input("")
        if opcao21 == 1:
            pass
        elif opcao21 == 2:
            pass
        elif opcao21 == 3:
            pass
        elif opcao21 == "V":
            print("Bem-vindo/a à Feira Virtual. Pretende aceder a:\n1 - Utilizadores\n2 - Artigos\n3 - Mercado")
            opcao1 = input("")
        elif opcao21 == "S":
            quit()
        else:
            print("Opção inálida")
            quit()
            
    elif opcao1 == 3:
        print("Pretende aceder a:\n1 – Adicionar Artigo ao Mercado\n2 – Remover Artigo do Mercado\n3 – Listar Artigos do Mercado\nV – Voltar atrás\nS – Sair")
        opcao31 = input("")
        if opcao31 == 1:
            print("Insira os detalhes do artigo para adicionar ao mercado (nome, tipologia, preço,quantidade):")
            opcao311 = input("")
        elif opcao31 == 2:
            pass
        elif opcao31 == 3:
            print("Artigos Disponíveis no Mercado:\n1. xxx \n2. xxx \n3. xxx")
        elif opcao31 == "V":
            print("Bem-vindo/a à Feira Virtual. Pretende aceder a:\n1 - Utilizadores\n2 - Artigos\n3 - Mercado")
            opcao1 = input("")
        elif opcao31 == "S":
            quit()
        else:
            print("Insira os detalhes do artigo para adicionar ao mercado (nome, tipologia, preço,quantidade):")
            opcao31 = input("")

    else:
        print("Opção inválida")
        quit()
    

if __name__=="__main__":
    main()
