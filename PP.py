class Utilizador:

    #Construtor
    def __init__(self, nome, interesses, artigos_disponiveis):
        self.nome = nome
        self.interesses = interesses
        self.artigos_disponiveis = artigos_disponiveis
        self.pycoins = 50
        self.avaliacao = []

    #Altera os interesses e/ou os artigos de um utilizador
    def editar_conta(self, novos_interesses, novos_artigos):
        self.interesses = novos_interesses
        if len(novos_artigos)==0:
            self.novos_artigos = []
        else:
            sep = novos_artigos.split("&")
            self.novos_artigos = [Artigo(*a.split('')) for a in sep]

    #Adiciona uma nova avaliação, podendo incluir um comentário
    def deixar_avaliacao(self, estrelas, comentario):
        self.estrelas = estrelas
        self.comentario = comentario
        avaliacao = {'estrelas': estrelas, 'comentario': comentario}
        self.avaliacao.append(avaliacao)
        print(f"Avaliação deixada por {self.utilizador}: {estrelas} estrelas - {comentario}")

    #Apresenta todas as avaliações e comentários
    def listar_avaliacoes(self):
        print(f"Avaliações de {self.nome}:")
        for avaliacao in self.avaliacoes:
            print(f"Estrelas: {avaliacao['estrelas']}, Comentário: {avaliacao['comentario']}")

    #Apresenta todos os interesses
    def mostrar_interesses(self):
        print(f"Interesses: {', '.join(self.interesses)}")

    #Apresenta todos os artigos
    def mostrar_artigos(self):
        print(self.artigos_disponiveis)


    #Altera o número de pycoins
    def alterar_pycoins(self, numero_pycoins):
        self.numero_pycoins = numero_pycoins
        print(f"{self.utilizador} agora possui {self.pycoins} PyCoins.")

    #Apresenta o número de pycoins
    def mostrar_pycoins(self):
        print(f"{self.nome} tem {self.pycoins} PyCoins.")

    def encontrar_utilizador(utilizador,nome):
        for utilizador in Utilizador:
            if utilizador.nome == nome:
                return utilizador
        return None

class Artigo:

    #Construtor
    def __init__(self, nome_artigo, preco, tipologia, quantidade):
        self.nome_artigo = nome_artigo
        self.preco = preco
        self.tipologia = tipologia
        self.quantidade = quantidade

    #Altera o nome de um artigo para o novo nome recebido
    def editar_nome(self, nome):
        self.nome = nome

    #Altera o preço de um artigo de acordo com a percentagem dada
    def ajustar_preco(self, percentagem_alteracao):
        self.preco = self.preco * percentagem_alteracao

    #Altera o preço para o novo preço recebido
    def editar_preco(self, preco):
        self.preco = preco

    #Apresenta o preço do artigo
    def mostrar_preco(self):
        print(f"O preço do artigo {self.nome_artigo} é {self.preco}")

    #Altera a quantidade
    def editar_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade

    #Apresenta a quantidade do artigo
    def mostrar_quantidade(self):
        print(f"A quantidade do artigo {self.nome_artigo} é {self.quantidade}")

    #Altera a tipologia
    def editar_tipo (self, novo_tipo):
        self.tipo = novo_tipo

    #Apresenta a tipologia do artigo
    def mostrar_tipo (self):
        print(f"A tipologia do artigo {self.nome_artigo} é {self.tipologia}")
    
    def encontrar_artigo(artigos_disponiveis,nome_artigo):
        for artigos_disponiveis in Artigo:
            if artigos_disponiveis.nome_artigo == nome_artigo:
                return artigos_disponiveis
        return None

class FeiraVirtual:

    #Construtor
    def __init__(self):
        self.utilizadores = []
        self.artigos_disponiveis = {}

    #Adiciona um novo utilizador recebendo o nome, interesses e artigos
    def registar_utilizador(self,nome,interesses,artigos_disponiveis):
        self.utilizadores.append(Utilizador(nome,interesses,artigos_disponiveis))
        
    #Importa uma lista de utilizadores a partir de um ficheiro
    def importar_utilizadores(self,nome_ficheiro):
        Utilizador = open(nome_ficheiro,"r")
        texto = Utilizador.read()
        linhas = texto.split("\n")[1:]
        for linha in linhas:
            partes = linha.split(";")
            nome = partes[0]
            interesses = partes[1].strip("[]").split(",") if partes[1] else []
            artigos_disponiveis = partes[2].strip("[]") if partes[1] else ""
            if len(artigos_disponiveis)==0:
                self.artigos = []
            else:
                sep = artigos_disponiveis.split("&")
                self.artigos_disponiveis = [Artigo(*a.split(',')) for a in sep]
            
            self.registar_utilizador(nome,interesses,artigos_disponiveis)
    
    #Importa uma lista de artigos a partir de um ficheiro
    def eliminar_conta(self, nome_utilizador):
        for utilizador in self.utilizadores:
            if utilizador.nome == nome_utilizador:
                self.utilizadores.remove(utilizador)
                break

    #Apresenta todos os artigos disponíveis ordenados por preço
    def listar_artigos(self):
        print("Lista de artigos:")
        
        n = 1
        for artigo in self.artigos:
            print(f"{n} - Nome: {artigo.nome_artigo}, Preço: {artigo.preco}, Tipologia: {artigo.tipologia}, Quantidade: {artigo.quantidade}")
            n = n + 1

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

    def mostrar_artigo(self):
        print("Introduza o nome do utilizador para ver os seus:")
        nome_utilizador_input = input("")
        for utilizador in self.utilizadores:
            if utilizador.nome == nome_utilizador_input:
                utilizador.mostrar_artigos()
                break
                    

    def mostrar_preco_artigo(self, nome_artigo):
        for artigo in self.artigos_disponiveis:
            if artigo.nome_artigo == nome_artigo:
                print(f"O preço do artigo {nome_artigo} é {artigo.preco}")
                return
        print(f"Artigo {nome_artigo} não encontrado.")


    def mostrar_tipologia_artigo(self):
        print("Introduza o nome do artigo que deseja ver a tipologia: ")
        nome_artigo_input = input("")
        artigo_selecionado = None
        for artigo in self.artigos_disponiveis:
            if artigo.nome_artigo == nome_artigo_input:
                artigo_selecionado = artigo
                break

        if artigo_selecionado:
            print(f"A tipologia do artigo é {artigo_selecionado.mostrar_tipo()}")

    def listar_todos_artigos(self):
        todos_artigos = []
        for utilizador in self.utilizadores:
            todos_artigos.extend(utilizador.artigos_disponiveis)
        return todos_artigos

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

    def mostrar_artigo(self, artigo):
    #Mostra o nome, preço e quantidade do artigo recebido
        self.artigo = artigo

def main():

    ###artigo = Artigo(nome, preco, tipologia, quantidade)
    fv = FeiraVirtual()
    

    while 1:

        opcao1 = None

        if not opcao1:
            print("Bem-vindo/a à Feira Virtual. Pretende aceder a:\n1 - Utilizadores\n2 - Artigos\n3 - Mercado")
            opcao1 = input("")
        if opcao1 == "1":
            print("Pretende aceder a:\n1 – Registo de utilizadores\n2 – Alteração de um utilizador\n3 – Eliminação de conta de um utilizador\n4 – Lista de utilizadores\n5 – Mostrar artigos de um utilizador\n6 – Mostrar interesses de um utilizador\n7 – Mostrar Pycoins de um utilizador\nV – Voltar atrás\nS – Sair")
            opcao11 = input("")

            if opcao11 == "1":
                print("1 – Registo manual\n2 – Registo por ficheiro")
                opcao12 = input("")

                if opcao12 == "1":
                    nome = input("Introduza o seu nome de utilizador: ")
                    interesses = input("Introduza os seus interesses: ")
                    artigos_disponiveis = input("Introduza os seus artigos da forma (nome artigo, preco, tipologia, quantidade):")
                    fv.utilizadores.append(Utilizador(nome,interesses,artigos_disponiveis))
                    
                if opcao12 == "2":
                    ficheiro = "biblioteca.txt"
                    fv.importar_utilizadores(ficheiro)

            elif opcao11 == "2":
                print("Introduza o nome do artigo que deseja alterar: ")
                nome_utilizador_input = input("")
                utilizador_selecionado = None
                for utilizador in fv.utilizadores:
                    if utilizador.nome == nome_utilizador_input:
                        utilizador_selecionado = utilizador
                        break

                if utilizador_selecionado:
                    novos_interesses = input("Introduza os novos interesses do utilizador (separados por vírgulas): ").split(",")
                    novos_artigos = input("Introduza os novos artigos do utilizador (separados por vírgulas e & para separar diferentes artigos): ")
                    utilizador_selecionado.editar_conta(novos_interesses, novos_artigos)

            elif opcao11 == "3":
                nome_utilizador_input = input("Introduza o nome do utilizador que deseja remover: ")
                fv.eliminar_conta(nome_utilizador_input)

            elif opcao11 == "4":
                for utilizador in fv.utilizadores:
                    print(f"Nome: {utilizador.nome}, Interesses: {', '.join(utilizador.interesses)}")

            elif opcao11 == "5":
                fv.mostrar_artigo()

            elif opcao11 == "6":
                print("Introduza um nome de utilizador para consultar os seus interesses:")
                nome_utilizador_input = input("")
                utilizador_selecionado = None
                for utilizador in fv.utilizadores:
                    if utilizador.nome == nome_utilizador_input:
                        utilizador_selecionado = utilizador
                        break
                if utilizador_selecionado:
                    utilizador_selecionado.mostrar_interesses()

            elif opcao11 == "7":
                print("Introduza um nome de utilizador para consultar os seus pycoins:")
                nome_utilizador_input = input("")
                utilizador_selecionado = None
                for utilizador in fv.utilizadores:
                    if utilizador.nome == nome_utilizador_input:
                        utilizador_selecionado = utilizador
                        break
                if utilizador_selecionado:
                    utilizador_selecionado.mostrar_pycoins()

            elif opcao11 == "V" or opcao11 == "v":
                opcao1 = None
                main()

            elif opcao11 == "S" or opcao11 == "s":
                quit()

            else:
                print("Opção inálida")
                quit()

        elif opcao1 == "2":
            print("Pretende aceder a: \n1 – Mostrar preço de um artigo\n2 – Mostrar quantidade de um artigo\n3 – Mostrar tipo de um artigo\nV – Voltar atrás\nS – Sair")
            opcao21 = input("")

            if opcao21 == "1":
                print("Introduza o artigo que deseja ver o preço: ")
                nome_artigo_input = input("")
                artigo_selecionado = None
                for artigo in fv.artigos_disponiveis:
                    if artigo.nome_artigo == nome_artigo_input:
                        artigo_selecionado = artigo
                        break
                if artigo_selecionado:
                    artigo_selecionado.mostrar_preco()
                

            elif opcao21 == "2":
                nome_artigo_input = input("Introduza o artigo que deseja ver a quantidade: ")
                artigo_selecionado = None
                for artigo in fv.artigos_disponiveis:
                    if artigo.nome_artigo == nome_artigo_input:
                        artigo_selecionado = artigo
                        break
                if artigo_selecionado:
                    artigo_selecionado.mostrar_quantidade()                 

            elif opcao21 == "3":
                print("Introduza o artigo que deseja ver a quantidade: ")
                nome_artigo_input = input("")
                artigo_selecionado = None
                for artigo in fv.artigos_disponiveis:
                    if artigo.nome_artigo == nome_artigo_input:
                        artigo_selecionado = artigo
                        break
                if artigo_selecionado:
                    artigo_selecionado.mostrar_quantidade()

            elif opcao21 == "V" or opcao21 == "v":
                opcao1 = None
                main()

            elif opcao21 == "S" or opcao21 == "s":
                quit()

            else:
                print("Opção inválida")
                quit()
                
        elif opcao1 == "3":
            print("Pretende aceder a:\n1 – Adicionar Artigo ao Mercado\n2 – Remover Artigo do Mercado\n3 – Listar Artigos do Mercado\nV – Voltar atrás\nS – Sair")
            opcao31 = input("")

            if opcao31 == "1":
                print("Insira os detalhes do artigo para adicionar ao mercado (nome, preco, tipologia, quantidade):")
                nome_artigo_input = input("")
                artigo_selecionado = None
                for artigo in Mercado:
                    if utilizador.nome == nome_artigo_input:
                        artigo_selecionado = artigo
                        break
                if artigo_selecionado:
                    artigo_selecionado.adicionar_artigo()

            elif opcao31 == "2":
                print("Introduza o artigo que deseja remover:")
                nome_artigo_input = input("")
                artigo_selecionado = None
                for artigo in Artigo:
                    if utilizador.nome == nome_artigo_input:
                        artigo_selecionado = artigo
                        break
                if artigo_selecionado:
                    artigo_selecionado.remover_artigo()

            elif opcao31 == "3":
                fv.listar_artigos()

            elif opcao31 == "V" or opcao31 == "v":
                opcao1 = None
                main()

            elif opcao31 == "S" or opcao31 == "s":
                quit()

            else:
                print("Opção inválida")
                quit()

        else:
            print("Opção inválida")
            quit()


if __name__=="__main__":
    main()
