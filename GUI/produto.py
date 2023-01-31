
from crud_operation import CrudOperation
from typing import Final


with open("edit_pdt.txt", "r") as arquivo:
    TABLE = arquivo.readline().strip()
    FIELD1 = arquivo.readline().strip()
    FIELD2 = arquivo.readline().strip()
    FIELD3 = arquivo.readline().strip()
    
class Produto:
    def __init__(self, nome, valor, quantidade):

        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade





    def create_product(self, nome, valor, quantidade):
         CrudOperation.create(str(TABLE), str(FIELD1), str(FIELD2), str(FIELD3), nome, valor, quantidade)

    def edit_product(self,old_info, new_info, select_code):
        if select_code == 1:
            CrudOperation.update_info(str(TABLE), str(FIELD1), old_info, new_info)
        if select_code == 2:
            CrudOperation.update_info(str(TABLE), str(FIELD2), old_info, new_info)
        if select_code == 3:
            CrudOperation.update_info(str(TABLE), str(FIELD3), old_info, new_info)
    
    def delete_product(self, product_name):
        CrudOperation.delete_info(str(TABLE), str(FIELD1), product_name)





    