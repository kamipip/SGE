from abc import ABC, abstractmethod
from db_operation import insert

class CrudOperation():
    
    def __init__(self, valor):
        self.valor = valor
    
    @abstractmethod
    def create(tbl_name,fieldname1, fieldname2, fieldname3, value1, value2, value3):
        insert(tbl_name, fieldname1, fieldname2, fieldname3, value1, value2, value3)

        
    
    @abstractmethod
    def read(self, valor):
        pass

    @abstractmethod
    def update(self, valor, novo_valor):
        pass

    @abstractmethod
    def delete(self, valor):
        pass