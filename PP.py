#Construtor
def __init__(self, nome, interesses, artigos_disponiveis):
#Altera os interesses e/ou os artigos de um utilizador
def editar_conta(self, novos_interesses, novos_artigos):
#Adiciona uma nova avaliação, podendo incluir um comentário
def deixar_avaliacao(self, estrelas, comentario):
#Apresenta todas as avaliações e comentários
def listar_avaliacoes(self):
#Apresenta todos os interesses
def mostrar_interesses(self):
#Apresenta todos os artigos
def mostrar_artigos(self):
#Altera o número de pycoins
def alterar_pycoins(self, numero_pycoins):
#Apresenta o número de pycoins
def mostrar_pycoins(self):

#Construtor
def __init__(self, nome, preco, tipologia, quantidade):
#Altera o nome de um artigo para o novo nome recebido
def editar_nome(self, nome):
#Altera o preço de um artigo de acordo com a percentagem dada
def ajustar_preco(self, percentagem_alteracao):
#Altera o preço para o novo preço recebido
def editar_preco(self, preco):
#Apresenta o preço do artigo
def mostrar_preco(self):
#Altera a quantidade
def editar_quantidade(self, nova_quantidade):
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

def main():

#Construtor
def __init__(self):
#Adiciona um novo artigo
def adicionar_artigo(self, artigo):
#Elimina um artigo
def remover_artigo(self, artigo):
#Mostra o nome, preço e quantidade do artigo recebido
def mostrar_artigo(self, artigo):
