#Kernel Manipulation Module
import sys

#Visual Modules
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, 
    QTableWidgetItem, QDockWidget, QFormLayout, 
    QLineEdit, QWidget, QPushButton, QSpinBox, 
    QMessageBox, QToolBar, QMessageBox
)
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtGui import QIcon, QAction

from PyQt6.QtWidgets import *

import sqlite3
from sistema_estoque.db_operation import read_table






#Modules to Create, Read and Update
#from filial import Filial
#from produto import Produto
#from matriz import Matriz



#Style Module
#from qt_material import apply_stylesheet

class MainWindow2(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Sistema de Cadastro de Matriz e Filial')
        self.setGeometry(100, 100, 600, 400)

        #Produto Teste
        products = [
            {'Local': 'Area 52', 'Endereço': 'R.Perimental Nosso Refugio', 'Tipo': 'Filial'},
        ]

        self.table = QTableWidget(self)
        self.setCentralWidget(self.table)

        self.table.setColumnCount(3)
        self.table.setColumnWidth(0, 90)
        self.table.setColumnWidth(1, 90)
        self.table.setColumnWidth(2, 90)

        self.table.setHorizontalHeaderLabels(products[0].keys())
        self.table.setRowCount(len(products))
        self.loaddata()

        #Lock Maximaze button
        #Not Working 
        #MainWindow.setWindowFlags(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.WindowMinimizeButtonHint)



        row = 0
        for e in products:
            self.table.setItem(row, 0, QTableWidgetItem(e['Local']))
            self.table.setItem(row, 1, QTableWidgetItem(e['Endereço']))
            self.table.setItem(row, 2, QTableWidgetItem(e['Tipo']))
            row += 1

        dock = QDockWidget('Salvar Produto')
        dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)

        # create form
        form = QWidget()
        layout = QFormLayout(form)
        form.setLayout(layout)


        self.local = QLineEdit(form)
        self.endereco = QLineEdit(form)
        self.tipo = QLineEdit(form)

        layout.addRow('Local:', self.local)
        layout.addRow('Endereço:', self.endereco)
        layout.addRow('Tipo:', self.tipo)


        btn_add = QPushButton('Salvar Produto')
        btn_add.clicked.connect(self.add_product)
        layout.addRow(btn_add)

        # add delete & edit button
        toolbar = QToolBar('main toolbar')
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)


        delete_action = QAction(QIcon('./assets/exclude.png'), '&Delete', self)
        delete_action.triggered.connect(self.delete)
        toolbar.addAction(delete_action)
        dock.setWidget(form)

        change_window_action = QAction(QIcon('./assets/product.png'), '&Change to Matriz System', self)
        change_window_action.triggered.connect(self.change)
        toolbar.addAction(change_window_action)
        dock.setWidget(form)

        


    def delete(self):
        current_row = self.table.currentRow()
        if current_row < 0:
            return QMessageBox.warning(self, 'Deletar')

        button = QMessageBox.question(
            self,
            'Alerta',
            'Deseja Apagar o produto cadastrado',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
            
        )
        if button == QMessageBox.StandardButton.Yes:
            self.table.removeRow(current_row)



    def valid(self):
        local = self.local.text().strip()
        endereco = self.endereco.text().strip()
        tipo = self.tipo.text().strip()

        
        if not local:
            QMessageBox.critical(self, 'Error', 'Insira o nome do Local')
            self.local.setFocus()
            return False

        if not endereco:
            QMessageBox.critical(self, 'Error', 'Insira o endereço do local')
            self.endereco.setFocus()
            return False

        if not tipo:
            QMessageBox.critical(self, 'Error', 'Insira se é Matriz o Filial/Matriz')
            self.endereco.setFocus()
            return False

        #try:
            #qnt = int(self.qnt.text().strip())
        #except ValueError:
            #QMessageBox.critical(self, 'Error', 'Insira a quantidade correta ')
            #self.age.setFocus()
            #return False

         #Something to not buffer overflow   
        #if qnt <= 0 or qnt >= 1000000:
            #QMessageBox.critical(
                #self, 'Error', 'Valor de Produto Ultrapassado')
            #return False

        return True

    def reset(self):
        self.local.clear()
        self.endereco.clear()
        #self.qnt.clear()
        self.tipo.clear()



    def add_product(self):
        if not self.valid():
            return

        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(
            self.local.text().strip())
        )
        self.table.setItem(
            row, 1, QTableWidgetItem(self.endereco.text())
        )

        self.table.setItem(
            row, 2, QTableWidgetItem(self.tipo.text())
        )

        self.reset()

    def loaddata(self):
        connection = sqlite3.connect('test_database.db')
        cur = connection.cursor()
        sqlstr = "SELECT a.product_name, b.price FROM products a LEFT JOIN prices b ON a.product_id = b.product_id "

        tablerow=0
        results = cur.execute(sqlstr)
        self.table.setRowCount(8)
        for row in results:
            self.table.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.table.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            #self.table.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            #self.table.setItem(tablerow, 2, QTableWidgetItem(row[3]))
            tablerow+=1

    def change(self):
        self.window = MainWindow2()
        self.window.show()
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #apply_stylesheet(app, theme='dark_teal.xml')
    window = MainWindow2()
    window.show()
    sys.exit(app.exec())