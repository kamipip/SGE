from crud_operation import CrudOperation

#Not Necessary Anymore
#from typing import Final

# Constant areas. an .env file is much more better

with open("edit_filial.txt", "r") as arquivo:
    TABLE = arquivo.readline().strip()
    FIELD1 = arquivo.readline().strip()
    FIELD2 = arquivo.readline().strip()
    FIELD3 = arquivo.readline().strip()


class Filial(CrudOperation):
   
    def __init__(self, nome, endereco, tipo):
        
        self.nome = nome
        self.endereco = endereco
        self.tipo = tipo
    
    def create_filial(self, nome, endereco, tipo):
                                  #LOL
            CrudOperation.create(str(TABLE), str(FIELD1), str(FIELD2), str(FIELD3), nome, tipo, endereco)

    #Life is good, but not a strawberry
    def edit_filial(self, old_info, new_info, select_code):
        if select_code == 1:
            CrudOperation.update_info(str(TABLE), str(FIELD1), old_info, new_info) 
        if select_code == 2:
            CrudOperation.update_info(str(TABLE), str(FIELD2), old_info, new_info)
        if select_code == 3:
            CrudOperation.update_info(str(TABLE), str(FIELD3), old_info, new_info)
    
    def delete_filial(self, filial_del):
        CrudOperation.delete_info(str(TABLE), str(FIELD1), filial_del)



    
    
#filial1 = Filial('filial1', 'ferro', 'avenida do aço')

#filial1.create_filial(filial1.nome, filial1.tipo, filial1.endereco)

#filial1.delete_filial(filial1.nome)



