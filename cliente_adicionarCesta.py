from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem 

import psycopg2
import pandas as pd
import variaveisControle

host = variaveisControle.host
user = variaveisControle.user
password = variaveisControle.password
database = variaveisControle.database
port = variaveisControle.port

class Ui_adicionar(object):
    def setupUi(self, adicionar):
        adicionar.setObjectName("adicionar")
        adicionar.resize(400, 295)

        self.Produto = QtWidgets.QLabel(adicionar)
        self.Produto.setGeometry(QtCore.QRect(90, 100, 51, 20))
        self.Produto.setObjectName("Produto")

        self.search_product = QtWidgets.QLineEdit(adicionar)
        self.search_product.setGeometry(QtCore.QRect(140, 100, 151, 20))
        self.search_product.setObjectName("search_product")

        self.CPFClient = QtWidgets.QLabel(adicionar)
        self.CPFClient.setGeometry(QtCore.QRect(60, 70, 91, 20))
        self.CPFClient.setObjectName("CPFClient")

        self.search_CPF = QtWidgets.QLineEdit(adicionar)
        self.search_CPF.setGeometry(QtCore.QRect(140, 70, 151, 20))
        self.search_CPF.setObjectName("search_CPF")

        self.QntItem = QtWidgets.QLabel(adicionar)
        self.QntItem.setGeometry(QtCore.QRect(50, 130, 91, 20))
        self.QntItem.setObjectName("QntItem")

        self.search_qntItem = QtWidgets.QLineEdit(adicionar)
        self.search_qntItem.setGeometry(QtCore.QRect(140, 130, 151, 20))
        self.search_qntItem.setText("")
        self.search_qntItem.setObjectName("search_qntItem")

        self.cesta_addbutton = QtWidgets.QPushButton(adicionar)
        self.cesta_addbutton.setGeometry(QtCore.QRect(210, 180, 111, 71))
        #self.cesta_addbutton.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo_adicionar/adicionar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cesta_addbutton.setIcon(icon)
        self.cesta_addbutton.setObjectName("cesta_addbutton")

        self.cancelar_button = QtWidgets.QPushButton(adicionar)
        self.cancelar_button.setGeometry(QtCore.QRect(100, 180, 101, 71))
        #self.cancelar_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logo_excluir/excluir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelar_button.setIcon(icon1)
        self.cancelar_button.setObjectName("cancelar_button")

        self.retranslateUi(adicionar)
        QtCore.QMetaObject.connectSlotsByName(adicionar)

    def retranslateUi(self, adicionar):
        _translate = QtCore.QCoreApplication.translate
        adicionar.setWindowTitle(_translate("adicionar", "Form"))
        self.Produto.setText(_translate("adicionar", "Produto:"))
        self.CPFClient.setText(_translate("adicionar", "CPF do Cliente:"))
        self.QntItem.setText(_translate("adicionar", "Quantidade item:"))
        self.cesta_addbutton.setText(_translate("adicionar", "Adicionar a Cesta"))
        self.cancelar_button.setText(_translate("adicionar", "Cancelar"))
        self.cesta_addbutton.clicked.connect(self.AdicionarCesta)
        self.cancelar_button.clicked.connect(lambda: self.sairTela(adicionar))

    def AdicionarCesta(self):
        cpfCliente = self.search_CPF.text()
        produtoCli = self.search_product.text()
        qntItem = self.search_qntItem.text()
        connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)
        mycursor = connection.cursor()
        consultaSQL = "SELECT ADD_ITEMCESTA('"+ cpfCliente + "','" + produtoCli + "'," + qntItem +");"
        print(consultaSQL)       
        try:
            mycursor.execute(consultaSQL)
            connection.commit()
        except:
            print("Error")
            mycursor.close()
        self.search_CPF.setText("")
        self.search_product.setText("")
        self.search_qntItem.setText("")
        mycursor.close()

    def sairTela(self, adicionar):
        adicionar.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adicionar = QtWidgets.QWidget()
    ui = Ui_adicionar()
    ui.setupUi(adicionar)
    adicionar.show()
    sys.exit(app.exec_())
