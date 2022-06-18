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

class Ui_cadastro_funcionario(object):
    def setupUi(self, cadastro_cli):
        cadastro_cli.setObjectName("cadastro_cli")
        cadastro_cli.resize(351, 285)

        self.nome_funcionario = QtWidgets.QLabel(cadastro_cli)
        self.nome_funcionario.setGeometry(QtCore.QRect(30, 10, 111, 20))
        self.nome_funcionario.setObjectName("nome_funcionario")

        self.search_nome_funcionario = QtWidgets.QLineEdit(cadastro_cli)
        self.search_nome_funcionario.setGeometry(QtCore.QRect(140, 10, 181, 20))
        self.search_nome_funcionario.setObjectName("search_nome_funcionario")

        self.telefone_funcionario = QtWidgets.QLabel(cadastro_cli)
        self.telefone_funcionario.setGeometry(QtCore.QRect(20, 40, 121, 20))
        self.telefone_funcionario.setObjectName("telefone_funcionario")

        self.search_telefone_funcionario = QtWidgets.QLineEdit(cadastro_cli)
        self.search_telefone_funcionario.setGeometry(QtCore.QRect(140, 40, 181, 20))
        self.search_telefone_funcionario.setObjectName("search_telefone_funcionario")

        self.email_funcionario = QtWidgets.QLabel(cadastro_cli)
        self.email_funcionario.setGeometry(QtCore.QRect(30, 70, 111, 20))
        self.email_funcionario.setObjectName("email_funcionario")

        self.search_email_funcionario = QtWidgets.QLineEdit(cadastro_cli)
        self.search_email_funcionario.setGeometry(QtCore.QRect(140, 70, 181, 20))
        self.search_email_funcionario.setObjectName("search_email_funcionario")

        self.cpf_funcionario = QtWidgets.QLabel(cadastro_cli)
        self.cpf_funcionario.setGeometry(QtCore.QRect(40, 100, 101, 20))
        self.cpf_funcionario.setObjectName("cpf_funcionario")

        self.search_cpf_funcionario = QtWidgets.QLineEdit(cadastro_cli)
        self.search_cpf_funcionario.setGeometry(QtCore.QRect(140, 100, 181, 20))
        self.search_cpf_funcionario.setText("")
        self.search_cpf_funcionario.setObjectName("search_cpf_funcionario")

        self.cancelar_button_funcionario = QtWidgets.QPushButton(cadastro_cli)
        self.cancelar_button_funcionario.setGeometry(QtCore.QRect(170, 220, 61, 41))
        self.cancelar_button_funcionario.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo_excluir/excluir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelar_button_funcionario.setIcon(icon)
        self.cancelar_button_funcionario.setObjectName("cancelar_button_funcionario")

        self.cadastroFun_button = QtWidgets.QPushButton(cadastro_cli)
        self.cadastroFun_button.setGeometry(QtCore.QRect(240, 220, 61, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logo_cadastro/cadastrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastroFun_button.setIcon(icon1)
        self.cadastroFun_button.setObjectName("cadastroFun_button")

        self.cpf_funcionario_2 = QtWidgets.QLabel(cadastro_cli)
        self.cpf_funcionario_2.setGeometry(QtCore.QRect(30, 130, 111, 20))
        self.cpf_funcionario_2.setObjectName("cpf_funcionario_2")

        self.search_cargo_funcionario = QtWidgets.QLineEdit(cadastro_cli)
        self.search_cargo_funcionario.setGeometry(QtCore.QRect(140, 130, 181, 20))
        self.search_cargo_funcionario.setObjectName("search_cargo_funcionario")

        self.search_salario_funcionario = QtWidgets.QLineEdit(cadastro_cli)
        self.search_salario_funcionario.setGeometry(QtCore.QRect(140, 160, 181, 20))
        self.search_salario_funcionario.setText("")
        self.search_salario_funcionario.setObjectName("search_salario_funcionario")

        self.cpf_funcionario_3 = QtWidgets.QLabel(cadastro_cli)
        self.cpf_funcionario_3.setGeometry(QtCore.QRect(30, 160, 111, 20))
        self.cpf_funcionario_3.setObjectName("cpf_funcionario_3")

        self.cpf_funcionario_4 = QtWidgets.QLabel(cadastro_cli)
        self.cpf_funcionario_4.setGeometry(QtCore.QRect(30, 190, 111, 20))
        self.cpf_funcionario_4.setObjectName("cpf_funcionario_4")

        self.search_carteira_funcionario = QtWidgets.QLineEdit(cadastro_cli)
        self.search_carteira_funcionario.setGeometry(QtCore.QRect(140, 190, 181, 20))
        self.search_carteira_funcionario.setText("")
        self.search_carteira_funcionario.setObjectName("search_carteira_funcionario")

        self.retranslateUi(cadastro_cli)
        QtCore.QMetaObject.connectSlotsByName(cadastro_cli)

    def retranslateUi(self, cadastro_cli):
        _translate = QtCore.QCoreApplication.translate
        cadastro_cli.setWindowTitle(_translate("cadastro_cli", "Form"))
        self.nome_funcionario.setText(_translate("cadastro_cli", "Nome do Funcionário:"))
        self.telefone_funcionario.setText(_translate("cadastro_cli", "Telefone do Funcionário:"))
        self.email_funcionario.setText(_translate("cadastro_cli", "E-mail do Funcionário:"))
        self.cpf_funcionario.setText(_translate("cadastro_cli", "CPF do Funcionário:"))
        self.cancelar_button_funcionario.setText(_translate("cadastro_cli", "Cancelar"))
        self.cadastroFun_button.setText(_translate("cadastro_cli", "Cadastro"))
        self.cpf_funcionario_2.setText(_translate("cadastro_cli", "Cargo do Funcionário:"))
        self.cpf_funcionario_3.setText(_translate("cadastro_cli", "Salário do Funcionário:"))
        self.cpf_funcionario_4.setText(_translate("cadastro_cli", "Carteira de Trabalho:"))
        
        self.cadastroFun_button.clicked.connect(self.cadastrarFuncionario)
        self.cancelar_button_funcionario.clicked.connect(lambda: self.sairTela(cadastro_cli))

    def cadastrarFuncionario(self):
        nameInsert = self.search_nome_funcionario.text()
        telefoneInsert = self.search_telefone_funcionario.text()
        emailInsert = self.search_email_funcionario.text()
        cpfInsert = self.search_cpf_funcionario.text()
        cargoInsert = self.search_cargo_funcionario.text()
        salarioInsert = self.search_salario_funcionario.text()
        carteiraInsert = self.search_carteira_funcionario.text()
        
        connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)
        mycursor = connection.cursor()
        consultaSql = "SELECT ADD_FUNCIONARIO('"+nameInsert +"','"+telefoneInsert+"','"+emailInsert+"','"+ cpfInsert + "','" + cargoInsert + "','" + salarioInsert + "','" + carteiraInsert + "');"
        try:
            mycursor.execute(consultaSql)
            connection.commit()
        except:
            print ("erro")
        self.search_nome_funcionario.setText("")
        self.search_cpf_funcionario.setText("")
        self.search_email_funcionario.setText("")
        self.search_telefone_funcionario.setText("")
        self.search_cargo_funcionario.setText("")
        self.search_salario_funcionario.setText("")
        self.search_carteira_funcionario.setText("")
        mycursor.close()
        
    def sairTela(self, cadastro_fun):
        cadastro_fun.close()

from Imagens import imageCadastro
from Imagens import imageDelete

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cadastro_cli = QtWidgets.QWidget()
    ui = Ui_cadastro_funcionario()
    ui.setupUi(cadastro_cli)
    cadastro_cli.show()
    sys.exit(app.exec_())
