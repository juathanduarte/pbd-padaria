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

class Ui_cadastro_cli(object):
    def setupUi(self, cadastro_cli):
        cadastro_cli.setObjectName("cadastro_cli")
        cadastro_cli.resize(351, 235)

        self.NameClient = QtWidgets.QLabel(cadastro_cli)
        self.NameClient.setGeometry(QtCore.QRect(40, 40, 91, 20))
        self.NameClient.setObjectName("NameClient")

        self.search_name = QtWidgets.QLineEdit(cadastro_cli)
        self.search_name.setGeometry(QtCore.QRect(130, 40, 181, 20))
        self.search_name.setObjectName("search_name")

        self.TelefoneClient = QtWidgets.QLabel(cadastro_cli)
        self.TelefoneClient.setGeometry(QtCore.QRect(30, 70, 101, 20))
        self.TelefoneClient.setObjectName("TelefoneClient")

        self.search_telefone = QtWidgets.QLineEdit(cadastro_cli)
        self.search_telefone.setGeometry(QtCore.QRect(130, 70, 181, 20))
        self.search_telefone.setObjectName("search_telefone")

        self.EmailClient = QtWidgets.QLabel(cadastro_cli)
        self.EmailClient.setGeometry(QtCore.QRect(40, 100, 91, 20))
        self.EmailClient.setObjectName("EmailClient")

        self.search_Email = QtWidgets.QLineEdit(cadastro_cli)
        self.search_Email.setGeometry(QtCore.QRect(130, 100, 181, 20))
        self.search_Email.setObjectName("search_Email")

        self.CPFClient = QtWidgets.QLabel(cadastro_cli)
        self.CPFClient.setGeometry(QtCore.QRect(40, 130, 91, 20))
        self.CPFClient.setObjectName("CPFClient")

        self.search_cpf = QtWidgets.QLineEdit(cadastro_cli)
        self.search_cpf.setGeometry(QtCore.QRect(130, 130, 181, 20))
        self.search_cpf.setObjectName("search_cpf")
        
        self.cancelar_button = QtWidgets.QPushButton(cadastro_cli)
        self.cancelar_button.setGeometry(QtCore.QRect(40, 170, 81, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo_excluir/excluir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelar_button.setIcon(icon)
        self.cancelar_button.setObjectName("cancelar_button")

        self.cadastroCli_button = QtWidgets.QPushButton(cadastro_cli)
        self.cadastroCli_button.setGeometry(QtCore.QRect(230, 170, 81, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logo_cadastro/cadastrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastroCli_button.setIcon(icon1)
        self.cadastroCli_button.setObjectName("cadastroCli_button")

        self.retranslateUi(cadastro_cli)
        QtCore.QMetaObject.connectSlotsByName(cadastro_cli)

    def retranslateUi(self, cadastro_cli):
        _translate = QtCore.QCoreApplication.translate
        cadastro_cli.setWindowTitle(_translate("cadastro_cli", "Form"))
        self.NameClient.setText(_translate("cadastro_cli", "Nome do Cliente"))
        self.TelefoneClient.setText(_translate("cadastro_cli", "Telefone do Cliente:"))
        self.EmailClient.setText(_translate("cadastro_cli", "E-mail do Cliente:"))
        self.CPFClient.setText(_translate("cadastro_cli", "CPF do Cliente:"))
        self.cancelar_button.setText(_translate("cadastro_cli", "Cancelar"))
        self.cadastroCli_button.setText(_translate("cadastro_cli", "Cadastro"))
        self.cadastroCli_button.clicked.connect(self.cadastrarUsuario)
        self.cancelar_button.clicked.connect(lambda: self.sairTela(cadastro_cli))

    def cadastrarUsuario(self):
        nameInsert = self.search_name.text()
        cpfInsert = self.search_cpf.text()
        emailInsert = self.search_Email.text()
        telefoneInsert = self.search_telefone.text()
        connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)
        mycursor = connection.cursor()
        consultaSql = "SELECT ADD_CLIENTE('"+nameInsert +"','"+telefoneInsert+"','"+emailInsert+"','"+ cpfInsert+ "');"
        try:
            mycursor.execute(consultaSql)
            connection.commit()
        except:
            print ("erro")
        self.search_name.setText("")
        self.search_cpf.setText("")
        self.search_Email.setText("")
        self.search_telefone.setText("")
        mycursor.close()
        
    def sairTela(self, cadsatro_cli):
        cadsatro_cli.close()

from Imagens import imageCadastro
from Imagens import imageDelete

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cadastro_cli = QtWidgets.QWidget()
    ui = Ui_cadastro_cli()
    ui.setupUi(cadastro_cli)
    cadastro_cli.show()
    sys.exit(app.exec_())
