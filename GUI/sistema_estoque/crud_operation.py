from db_operation import insert, update,delete

class CrudOperation():
    
    def __init__(self, valor):
        self.valor = valor
    
  
    def create(tbl_name,fieldname1, fieldname2, fieldname3, value1, value2, value3):
        insert(tbl_name, fieldname1, fieldname2, fieldname3, value1, value2, value3)

        
    
    def read(self, valor):
        pass



    def update_info(tbl_name, field, old_value, new_value):
        update(tbl_name, field, old_value, new_value)

        

    
    def delete_info(tbl_name, field,value):
        delete(tbl_name, field, value)