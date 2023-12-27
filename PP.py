#Construtor
def __init__(self, nome, interesses, artigos_disponiveis):
    self.nome = nome
    self.interesses = interesses
    self.artigos_disponiveis = artigos_disponiveis
#Altera os interesses e/ou os artigos de um utilizador
def editar_conta(self, novos_interesses, novos_artigos):
    self.interesses = novos_interesses
    self.artigos_disponiveis = novos_artigos
#Adiciona uma nova avaliação, podendo incluir um comentário
def deixar_avaliacao(self, estrelas, comentario):
    self.estrelas = estrelas
    self.comentario = comentario
#Apresenta todas as avaliações e comentários
def listar_avaliacoes(self):
#Apresenta todos os interesses
def mostrar_interesses(self):
    print("Introduza um nome de utilizador para consultar os seus interesses:")
    mostrar_interesses = input("")
    print(f"Interesses de {self.mostrar_insteresses}: {', '.join(self.interesses)}")
#Apresenta todos os artigos
def mostrar_artigos(self):
    
#Altera o número de pycoins
def alterar_pycoins(self, numero_pycoins):
    self.numero_pycoins = numero_pycoins
    print(f"{self.utilizador} agora possui {self.pycoins} PyCoins.")
#Apresenta o número de pycoins
def mostrar_pycoins(self):
    print("Introduza um nome de utilizador para consultar os seus Pycoins:")
    mostrar_pycoins_nome = input("")
    print(f"{self.nome} tem {self.pycoins} PyCoins.")
        

#Construtor
def __init__(self, nome, preco, tipologia, quantidade):
    self.nome = nome
    self.preco = preco
    self.tipologia = tipologia
    self.quantidade = quantidade
#Altera o nome de um artigo para o novo nome recebido
def editar_nome(self, nome):
    self.nome = novo_nome
     if artigo in self.artigos_disponiveis
        preco = self.artigos_disponiveis[artigo]

#Altera o preço de um artigo de acordo com a percentagem dada
def ajustar_preco(self, percentagem_alteracao):
    self.
#Altera o preço para o novo preço recebido
def editar_preco(self, preco):
    self.preco = novo_preco
#Apresenta o preço do artigo
def mostrar_preco(self):
#Altera a quantidade
def editar_quantidade(self, nova_quantidade):
    self.quantidade = nova_quantidade
#Apresenta a quantidade do artigo
def mostrar_quantidade(self):
#Altera a tipologia
def editar_tipo (self, novo_tipo):
#Apresenta a tipologia do artigo
def mostrar_tipo (self):

#Construtor
def __init__(self):
#Adiciona um novo utilizador recebendo o nome, interesses e artigos
def registar_utilizador (self, nome, interesses, artigos_disponiveis):
#Importa uma lista de utilizadores a partir de um ficheiro
def importar_utilizadores(self, nome_ficheiro):
#Importa uma lista de artigos a partir de um ficheiro
def importar_artigos(self, nome_ficheiro):
#Elimina um utilizador
def eliminar_conta(self, nome_utilizador):
#Apresenta todos os artigos disponíveis ordenados por preço
def listar_artigos(self):
#Efetua uma compra de um artigo. O comprador e o vendedor são os nomes de
dois utilizadores registados
def comprar_artigo(self, comprador, vendedor, artigo):
#Calcula a reputação de um utilizador com base nas suas avaliações
def calcular_reputacao(self, utilizador):
#Coloca um artigo à venda. O vendedor é o nome de um utilizador
def colocar_artigo_para_venda(self, vendedor, artigo, preco):
#Encontra os nomes de utilizadores interessados no artigo recebido
def encontrar_compradores_interessados(self, artigo):
#Exporta a lista de artigos para um ficheiro ordenados por quantidade
def exportar_artigos_preco(self, nome_ficheiro):
#Exporta a lista de utilizadores para um ficheiro ordenados por reputação
def exportar_utilizadores(self):
#Início da feira. O grupo deve apresentar testes do projeto nesta função

#Construtor
def __init__(self):
#Adiciona um novo artigo
def adicionar_artigo(self, artigo):
    self.artigo = adicionar_artigo
#Elimina um artigo
def remover_artigo(self, artigo):
    self.artigo = remover_artigo
#Mostra o nome, preço e quantidade do artigo recebido
def mostrar_artigo(self, artigo):
    mostrar_artigo = artigo

def main():
    FeiraVirtual = FeiraVirtual()
    user = Utilizador(input[""], [""], [""])
    print("Bem-vindo/a à Feira Virtual. Pretende aceder a:\1 - Utilizadores\2 - Artigos\3 - Mercado")
    opcao1 = int(input())
    if opcao1 == 1:
        print("Pretende aceder a:\n1 – Registo de utilizadores\n2 – Alteração de um utilizador\n3 – Eliminação de conta de um utilizador\n4 – Lista de utilizadores\n5 – Mostrar artigos de um utilizador\n6 – Mostrar interesses de um utilizador\n7 – Mostrar Pycoins de um utilizador\nV – Voltar atrás\nS – Sair")
        opcao11 = input("")
        if opcao11 == 1:
            print("1 – Registo manual\n2 – Registo por ficheiro")
            opcao12 = input("")
            if opcao12 == 1:
            if opcao12 == 2:
            while opcao12 < 1 or opcao12 > 2:
                opcao12 = input("")
        if opcao11 == 2:
        if opcao11 == 3:
        if opcao11 == 4:
        if opcao11 == 5:
            print("Introduza um utilizador para consultar os seus artigos:")
            opcao15 = input("")
            print("Artigo: n, Preço: n, Quantidade: n")
        if opcao11 == 6:
            for utilizador in self.nome:
            utilizador.mostrar_interesses()
        if opcao11 == 7:
        if opcao21 == "S":
            print("Bem-vindo/a à Feira Virtual. Pretende aceder a:\1 - Utilizadores\2 - Artigos\3 - Mercado")
            opcao1 = input("")
        if opcao21 == "V":
            quit()

    if opcao1 == 2:
        print("Pretende aceder a: \n1 – Mostrar preço de um artigo\n2 – Mostrar quantidade de um artigo\n3 – Mostrar tipo de um artigo\nV – Voltar atrás\nS – Sair")
        opcao21 = input("")
        if opcao21 == 1:
        if opcao21 == 2:
        if opcao21 == 3:
        if opcao21 == "S":
            print("Bem-vindo/a à Feira Virtual. Pretende aceder a:\1 - Utilizadores\2 - Artigos\3 - Mercado")
            opcao1 = input("")
        if opcao21 == "V":
            quit()
            
    if opcao1 == 3:
        print("Pretende aceder a:\n1 – Adicionar Artigo ao Mercado\n2 – Remover Artigo do Mercado\n3 – Listar Artigos do Mercado\nV – Voltar atrás\nS – Sair")
        opcao31 = input("")
        if opcao31 == 1:
            print("Insira os detalhes do artigo para adicionar ao mercado (nome, tipologia, preço,quantidade):")
            opcao311 = input("")
        if opcao31 == 2:
        if opcao31 == 3:
            print("Artigos Disponíveis no Mercado:\n1. xxx \n2. xxx \n3. xxx")
        if opcao31 == "S":
            print("Bem-vindo/a à Feira Virtual. Pretende aceder a:\1 - Utilizadores\2 - Artigos\3 - Mercado")
            opcao1 = input("")
        if opcao31 == "V":
            quit()

    else:
        print("Bem-vindo/a à Feira Virtual. Pretende aceder a:\1 - Utilizadores\2 - Artigos\3 - Mercado")
        opcao1 = input("")
    
    
if __name__=="__main__":
    main()
