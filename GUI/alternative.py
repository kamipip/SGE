import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, 
    QTableWidgetItem, QDockWidget, QFormLayout, 
    QLineEdit, QWidget, QPushButton, QSpinBox, 
    QMessageBox, QToolBar, QMessageBox
)
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtGui import QIcon, QAction

#Module from dark mode or style
#from qt_material import apply_stylesheet

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Sistema de Cadastro')
        self.setGeometry(100, 100, 600, 400)

        products = [
            {'Produto': 'Metal', 'Valor R$': '1000', 'U': 25},
        ]

        self.table = QTableWidget(self)
        self.setCentralWidget(self.table)

        self.table.setColumnCount(3)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 50)

        self.table.setHorizontalHeaderLabels(products[0].keys())
        self.table.setRowCount(len(products))

        row = 0
        for e in products:
            self.table.setItem(row, 0, QTableWidgetItem(e['Produto']))
            self.table.setItem(row, 1, QTableWidgetItem(e['Valor R$']))
            self.table.setItem(row, 2, QTableWidgetItem(str(e['U'])))
            row += 1

        dock = QDockWidget('Salvar Produto')
        dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)

        # create form
        form = QWidget()
        layout = QFormLayout(form)
        form.setLayout(layout)


        self.product = QLineEdit(form)
        self.value = QLineEdit(form)
        self.qnt = QSpinBox(form, minimum=18, maximum=67)
        self.qnt.clear()

        layout.addRow('Produto', self.product)
        layout.addRow('Valor R$', self.value)
        layout.addRow('U', self.qnt)

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

        delete_action = QAction(QIcon('./assets/industry.png'), '&Delete', self)
        delete_action.triggered.connect(self.delete)
        toolbar.addAction(delete_action)
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
        product = self.product.text().strip()
        value = self.value.text().strip()

        
        if not product:
            QMessageBox.critical(self, 'Error', 'Insira o nome do produto')
            self.product.setFocus()
            return False

        if not value:
            QMessageBox.critical(self, 'Error', 'Insira o valor do produto')
            self.value.setFocus()
            return False

        try:
            qnt = int(self.qnt.text().strip())
        except ValueError:
            QMessageBox.critical(self, 'Error', 'Insira a quantidade correta ')
            self.age.setFocus()
            return False

         #Something to not buffer overflow   
        if qnt <= 0 or qnt >= 1000000:
            QMessageBox.critical(
                self, 'Error', 'Valor de Produto Ultrapassado')
            return False

        return True

    def reset(self):
        self.product.clear()
        self.value.clear()
        self.qnt.clear()

    def add_product(self):
        if not self.valid():
            return

        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(
            self.product.text().strip())
        )
        self.table.setItem(
            row, 1, QTableWidgetItem(self.value.text())
        )
        self.table.setItem(
            row, 2, QTableWidgetItem(self.qnt.text())
        )

        self.reset()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #apply_stylesheet(app, theme='dark_teal.xml')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())