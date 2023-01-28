from crud_operation import CrudOperation
from typing import Final

# Constant areas

TABLE: Final = 'informacoes_filial'
FIELD1: Final = 'nome'
FIELD2: Final = 'tipo'
FIELD3: Final = 'endereco'


class Filial(CrudOperation):
   

    def __init__(self, nome, endereco, tipo):
        
        self.nome = nome
        self.endereco = endereco
        self.tipo = tipo
    
    def create_filial(self, nome, endereco, tipo):
                                  #gambiarra das grandes
            CrudOperation.create(str(TABLE), str(FIELD1), str(FIELD2), str(FIELD3), nome, tipo, endereco)
    
    
filial1 = Filial('filial1', 'ferro', 'avenida do aço')
filial1.create_filial(filial1.nome, filial1.endereco, filial1.tipo)


