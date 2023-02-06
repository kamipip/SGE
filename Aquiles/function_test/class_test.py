from GUI.sistema_estoque.filial import Filial
from animations.loading import Animation
from GUI.sistema_estoque.matriz import Matriz
from GUI.sistema_estoque.produto import Produto

class Func_T():
    
    def __init__(self):
        self
    
    def test_f_f():
        f = Filial()
        f.create_filial('Area 51', 'Rua Perimental', 'Filial')
        Animation.loading()

    def test_f_m():
        m = Matriz()
        m.create_matriz('Area 67', 'Rua Nova Esperança', 'Matriz')
        Animation.loading()

    def test_f_p():
        p = Produto()
        p.create_product('Cuscuz', '1.00', '888', 'Area 52')
        Animation.loading()
    