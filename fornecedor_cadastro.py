import email
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

class Ui_cadastro_fornecedor(object):
    def setupUi(self, cadastro_fornecedor):
        cadastro_fornecedor.setObjectName("cadastro_fornecedor")
        cadastro_fornecedor.resize(363, 210)

        self.nome_fornecedor = QtWidgets.QLabel(cadastro_fornecedor)
        self.nome_fornecedor.setGeometry(QtCore.QRect(10, 10, 111, 20))
        self.nome_fornecedor.setObjectName("nome_fornecedor")

        self.search_nome_fornecedor = QtWidgets.QLineEdit(cadastro_fornecedor)
        self.search_nome_fornecedor.setGeometry(QtCore.QRect(170, 10, 181, 20))
        self.search_nome_fornecedor.setObjectName("search_nome_fornecedor")

        self.telefone_fornecedor = QtWidgets.QLabel(cadastro_fornecedor)
        self.telefone_fornecedor.setGeometry(QtCore.QRect(10, 40, 131, 20))
        self.telefone_fornecedor.setObjectName("telefone_fornecedor")
        
        self.search_telefone_fornecedor = QtWidgets.QLineEdit(cadastro_fornecedor)
        self.search_telefone_fornecedor.setGeometry(QtCore.QRect(170, 40, 181, 20))
        self.search_telefone_fornecedor.setObjectName("search_telefone_fornecedor")

        self.email_fornecedor = QtWidgets.QLabel(cadastro_fornecedor)
        self.email_fornecedor.setGeometry(QtCore.QRect(10, 100, 111, 20))
        self.email_fornecedor.setObjectName("email_fornecedor")

        self.search_email_fornecedor = QtWidgets.QLineEdit(cadastro_fornecedor)
        self.search_email_fornecedor.setGeometry(QtCore.QRect(170, 100, 181, 20))
        self.search_email_fornecedor.setObjectName("search_email_fornecedor")

        self.cnpj_fornecedor = QtWidgets.QLabel(cadastro_fornecedor)
        self.cnpj_fornecedor.setGeometry(QtCore.QRect(10, 130, 111, 20))
        self.cnpj_fornecedor.setObjectName("cnpj_fornecedor")

        self.search_cnpj_fornecedor = QtWidgets.QLineEdit(cadastro_fornecedor)
        self.search_cnpj_fornecedor.setGeometry(QtCore.QRect(170, 130, 181, 20))
        self.search_cnpj_fornecedor.setObjectName("search_cnpj_fornecedor")

        self.cancelar_button_fornecedor = QtWidgets.QPushButton(cadastro_fornecedor)
        self.cancelar_button_fornecedor.setGeometry(QtCore.QRect(100, 160, 71, 41))
        self.cancelar_button_fornecedor.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo_excluir/excluir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelar_button_fornecedor.setIcon(icon)
        self.cancelar_button_fornecedor.setObjectName("cancelar_button_fornecedor")

        self.cadastro_button_fornecedor = QtWidgets.QPushButton(cadastro_fornecedor)
        self.cadastro_button_fornecedor.setGeometry(QtCore.QRect(180, 160, 71, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logo_cadastro/cadastrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastro_button_fornecedor.setIcon(icon1)
        self.cadastro_button_fornecedor.setObjectName("cadastro_button_fornecedor")

        self.search_endereco_fornecedor = QtWidgets.QLineEdit(cadastro_fornecedor)
        self.search_endereco_fornecedor.setGeometry(QtCore.QRect(170, 70, 181, 20))
        self.search_endereco_fornecedor.setObjectName("search_endereco_fornecedor")

        self.endereco_fornecedor = QtWidgets.QLabel(cadastro_fornecedor)
        self.endereco_fornecedor.setGeometry(QtCore.QRect(10, 70, 131, 20))
        self.endereco_fornecedor.setObjectName("endereco_fornecedor")

        self.retranslateUi(cadastro_fornecedor)
        QtCore.QMetaObject.connectSlotsByName(cadastro_fornecedor)

    def retranslateUi(self, cadastro_fornecedor):
        _translate = QtCore.QCoreApplication.translate
        cadastro_fornecedor.setWindowTitle(_translate("cadastro_fornecedor", "Form"))
        self.nome_fornecedor.setText(_translate("cadastro_fornecedor", "Nome do Fornecedor:"))
        self.telefone_fornecedor.setText(_translate("cadastro_fornecedor", "Telefone do Fornecedor:"))
        self.email_fornecedor.setText(_translate("cadastro_fornecedor", "E-mail do Fornecedor:"))
        self.cnpj_fornecedor.setText(_translate("cadastro_fornecedor", "CNPJ do Fornecedor:"))
        self.cancelar_button_fornecedor.setText(_translate("cadastro_fornecedor", "Cancelar"))
        self.cadastro_button_fornecedor.setText(_translate("cadastro_fornecedor", "Cadastro"))
        self.endereco_fornecedor.setText(_translate("cadastro_fornecedor", "Endereço do Fornecedor:"))

        self.cadastro_button_fornecedor.clicked.connect(self.cadastrar_Forne)
        self.cancelar_button_fornecedor.clicked.connect(lambda: self.sairTela(cadastro_fornecedor))

    def cadastrar_Forne(self):
        nameInsert = self.search_nome_fornecedor.text()
        telefoneInsert = self.search_telefone_fornecedor.text()
        enderecoInsert = self.search_endereco_fornecedor.text()
        emailInsert = self.search_email_fornecedor.text()
        cnpjInsert = self.search_cnpj_fornecedor.text()    
        connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)
        mycursor = connection.cursor()
        consultaSql ="SELECT ADD_FORNECEDOR('" + nameInsert + "','" + telefoneInsert + "','" + enderecoInsert + "','" + emailInsert + "','" + cnpjInsert + "');"
        try:
            mycursor.execute(consultaSql)
            connection.commit()
        except:
            print ("erro")
        self.search_nome_fornecedor.setText("")
        self.search_telefone_fornecedor.setText("")
        self.search_endereco_fornecedor.setText("")
        self.search_email_fornecedor.setText("")
        self.search_cnpj_fornecedor.setText("")
        mycursor.close()
        
    def sairTela(self, cadastroFornecedor):
        cadastroFornecedor.close()

from Imagens import imageCadastro

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cadastro_fornecedor = QtWidgets.QWidget()
    ui = Ui_cadastro_fornecedor()
    ui.setupUi(cadastro_fornecedor)
    cadastro_fornecedor.show()
    sys.exit(app.exec_())