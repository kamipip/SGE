
class Produto:
    def __init__(self, nome, descricao, valor, quantidade):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.quantidade = quantidade
    
    def transferir_produto(self, nome, quantidade, valor):
        if quantidade == 0:
            print("Produto não disponível no estoque")
        else:
            print("")
