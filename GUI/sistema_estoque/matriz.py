from crud_operation import CrudOperation
from typing import Final

# Constant areas. an .env file is much more better
with open("edit_matriz.txt", "r") as arquivo:
        TABLE = arquivo.readline().strip()
        FIELD1 = arquivo.readline().strip()
        FIELD2 = arquivo.readline().strip()
        FIELD3 = arquivo.readline().strip()

class Matriz:
    def __init__(self, nome, tipo, endereco):
        self.nome = nome
        self.tipo = tipo
        self.endereco = endereco

    
    def create_matriz(self, nome, tipo, endereco):
                                  #LOL
        CrudOperation.create(str(TABLE), str(FIELD1), str(FIELD2), str(FIELD3), nome, tipo, endereco)

    #Life is good, but can be better
    def edit_matriz(self, old_info, new_info, select_code):
        if select_code == 1:
            CrudOperation.update_info(str(TABLE), str(FIELD1), old_info, new_info)
        if select_code == 2:
            CrudOperation.update_info(str(TABLE), str(FIELD2), old_info, new_info)
        if select_code == 3:
            CrudOperation.update_info(str(TABLE), str(FIELD3), old_info, new_info)
    
    def delete_matriz(self, matriz_del):
        CrudOperation.delete_info(str(TABLE), str(FIELD1), matriz_del)





    
    

    
