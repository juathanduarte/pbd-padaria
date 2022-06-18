from this import s
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem 

from funcionario_excluir import Ui_exclusao_funcionario
from funcionario_cadastro import Ui_cadastro_funcionario

import psycopg2
import pandas as pd
import variaveisControle

host = variaveisControle.host
user = variaveisControle.user
password = variaveisControle.password
database = variaveisControle.database
port = variaveisControle.port

class Ui_funcionarioPage(object):
    def setupUi(self, funcionarioPage):
        funcionarioPage.setObjectName("funcionarioPage")
        funcionarioPage.resize(652, 363)

        self.cadastroFuncionario_button = QtWidgets.QPushButton(funcionarioPage)
        self.cadastroFuncionario_button.setGeometry(QtCore.QRect(220, 0, 101, 71))
        self.cadastroFuncionario_button.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo_cadastro/cadastrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastroFuncionario_button.setIcon(icon)
        self.cadastroFuncionario_button.setObjectName("cadastroFuncionario_button")

        self.excluirFuncionario_button = QtWidgets.QPushButton(funcionarioPage)
        self.excluirFuncionario_button.setGeometry(QtCore.QRect(320, 0, 101, 71))
        self.excluirFuncionario_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logo_excluir/excluir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.excluirFuncionario_button.setIcon(icon1)
        self.excluirFuncionario_button.setObjectName("excluirFuncionario_button")

        self.retorno_bd_Funcionario = QtWidgets.QTableWidget(funcionarioPage)
        self.retorno_bd_Funcionario.setGeometry(QtCore.QRect(10, 110, 631, 251))
        self.retorno_bd_Funcionario.setObjectName("retorno_bd_Funcionario")
        self.retorno_bd_Funcionario.setColumnCount(8)
        self.retorno_bd_Funcionario.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.retorno_bd_Funcionario.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.retorno_bd_Funcionario.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.retorno_bd_Funcionario.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.retorno_bd_Funcionario.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.retorno_bd_Funcionario.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.retorno_bd_Funcionario.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.retorno_bd_Funcionario.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.retorno_bd_Funcionario.setHorizontalHeaderItem(7, item)

        self.CPFClient_3 = QtWidgets.QLabel(funcionarioPage)
        self.CPFClient_3.setGeometry(QtCore.QRect(190, 80, 91, 20))
        self.CPFClient_3.setObjectName("CPFClient_3")

        self.search_cpf_Funcionario = QtWidgets.QLineEdit(funcionarioPage)
        self.search_cpf_Funcionario.setGeometry(QtCore.QRect(280, 80, 141, 20))
        self.search_cpf_Funcionario.setText("")
        self.search_cpf_Funcionario.setObjectName("search_cpf_Funcionario")

        self.procurarFuncionarioCPF_button = QtWidgets.QPushButton(funcionarioPage)
        self.procurarFuncionarioCPF_button.setGeometry(QtCore.QRect(430, 80, 61, 21))
        self.procurarFuncionarioCPF_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        self.procurarFuncionarioCPF_button.setObjectName("procurarFuncionarioCPF_button")

        self.mostrarFuncionarios_button = QtWidgets.QPushButton(funcionarioPage)
        self.mostrarFuncionarios_button.setGeometry(QtCore.QRect(490, 80, 81, 21))
        self.mostrarFuncionarios_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        self.mostrarFuncionarios_button.setObjectName("mostrarFuncionarios_button")

        self.cadastroFuncionario_button.raise_()
        self.excluirFuncionario_button.raise_()
        self.CPFClient_3.raise_()
        self.search_cpf_Funcionario.raise_()
        self.retorno_bd_Funcionario.raise_()
        self.procurarFuncionarioCPF_button.raise_()
        self.mostrarFuncionarios_button.raise_()

        self.retranslateUi(funcionarioPage)
        QtCore.QMetaObject.connectSlotsByName(funcionarioPage)

    def retranslateUi(self, funcionarioPage):
        _translate = QtCore.QCoreApplication.translate
        funcionarioPage.setWindowTitle(_translate("funcionarioPage", "Form"))
        self.cadastroFuncionario_button.setText(_translate("funcionarioPage", "Cadastro"))
        self.excluirFuncionario_button.setText(_translate("funcionarioPage", "Excluir"))
        item = self.retorno_bd_Funcionario.horizontalHeaderItem(0)
        item.setText(_translate("funcionarioPage", "ID"))
        item = self.retorno_bd_Funcionario.horizontalHeaderItem(1)
        item.setText(_translate("funcionarioPage", "Nome"))
        item = self.retorno_bd_Funcionario.horizontalHeaderItem(2)
        item.setText(_translate("funcionarioPage", "Telefone"))
        item = self.retorno_bd_Funcionario.horizontalHeaderItem(3)
        item.setText(_translate("funcionarioPage", "Email"))
        item = self.retorno_bd_Funcionario.horizontalHeaderItem(4)
        item.setText(_translate("funcionarioPage", "CPF"))
        item = self.retorno_bd_Funcionario.horizontalHeaderItem(5)
        item.setText(_translate("funcionarioPage", "Cargo"))
        item = self.retorno_bd_Funcionario.horizontalHeaderItem(6)
        item.setText(_translate("funcionarioPage", "Salário"))
        item = self.retorno_bd_Funcionario.horizontalHeaderItem(7)
        item.setText(_translate("funcionarioPage", "Carteira de Trabalho"))
        self.CPFClient_3.setText(_translate("funcionarioPage", "Procurar por CPF:"))
        self.procurarFuncionarioCPF_button.setText(_translate("funcionarioPage", "Procurar"))
        self.mostrarFuncionarios_button.setText(_translate("funcionarioPage", "Mostrar todos"))

        self.excluirFuncionario_button.clicked.connect(self.tela_funcionario_excluir)
        self.cadastroFuncionario_button.clicked.connect(self.tela_funcionario_cadastro)
        self.mostrarFuncionarios_button.clicked.connect(self.search_bd)
        self.procurarFuncionarioCPF_button.clicked.connect(self.pesquisar_funcionario)

    def tela_funcionario_excluir(self):
        self.exclusao_funcionario = QtWidgets.QWidget()
        self.ui = Ui_exclusao_funcionario()
        self.ui.setupUi(self.exclusao_funcionario)
        self.exclusao_funcionario.show()

    def tela_funcionario_cadastro(self):
        self.cadastro_cli = QtWidgets.QWidget()
        self.ui = Ui_cadastro_funcionario()
        self.ui.setupUi(self.cadastro_cli)
        self.cadastro_cli.show()

    def search_bd(self):
        connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)
        mycursor = connection.cursor()
        mycursor.execute("SELECT F.IDFUNCIONARIO, P.NOME, P.TELEFONE, P.EMAIL, P.CPF, F.CARGO, F.SALARIO, F.CARTEIRATRABALHO FROM PESSOA AS P INNER JOIN FUNCIONARIO AS F ON P.IDPESSOA = F.ID_PESSOA;")
        myresult = mycursor.fetchall()
        df = pd.DataFrame(myresult, columns = ['ID', 'NOME', 'TELEFONE', 'EMAIL', 'CPF', 'CARGO', 'SALARIO', 'CARTEIRATRABALHO'])
        self.all_data = df
        numRows = len(self.all_data.index)
        self.retorno_bd_Funcionario.setColumnCount(len(self.all_data.columns))
        self.retorno_bd_Funcionario.setRowCount(numRows)
        self.retorno_bd_Funcionario.setHorizontalHeaderLabels(self.all_data.columns)
        for i in range(numRows):
            for j in range(len(self.all_data.columns)):
                self.retorno_bd_Funcionario.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i,j])))
        
        self.retorno_bd_Funcionario.resizeColumnsToContents()
        self.retorno_bd_Funcionario.resizeRowsToContents()
        mycursor.close()

    def pesquisar_funcionario(self):
        connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)
        mycursor = connection.cursor()
        nomeConsulta = self.search_cpf_Funcionario.text()    
        consultaSql = "SELECT F.IDFUNCIONARIO, P.NOME, P.TELEFONE, P.EMAIL, P.CPF, F.CARGO, F.SALARIO, F.CARTEIRATRABALHO FROM PESSOA AS P INNER JOIN FUNCIONARIO AS F ON P.IDPESSOA = F.ID_PESSOA WHERE P.CPF = '" + nomeConsulta +"';"
        mycursor.execute(consultaSql)
        myresult = mycursor.fetchall()
        print(myresult)
        df = pd.DataFrame(myresult, columns = ['ID', 'NOME', 'TELEFONE', 'EMAIL', 'CPF', 'CARGO', 'SALARIO', 'CARTEIRATRABALHO'])
        self.all_data = df
        
        numRows = len(self.all_data.index)
        self.retorno_bd_Funcionario.setColumnCount(len(self.all_data.columns))
        self.retorno_bd_Funcionario.setRowCount(numRows)
        self.retorno_bd_Funcionario.setHorizontalHeaderLabels(self.all_data.columns)
        for i in range(numRows):
            for j in range(len(self.all_data.columns)):
                self.retorno_bd_Funcionario.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i,j])))
        
        self.retorno_bd_Funcionario.resizeColumnsToContents()
        self.retorno_bd_Funcionario.resizeRowsToContents()
        mycursor.close()

from Imagens import imageDeleteCesta
from Imagens import imageCadastro
from Imagens import imageCestaCliente
from Imagens import imageDelete
from Imagens import imageDeleteCesta

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    funcionarioPage = QtWidgets.QWidget()
    ui = Ui_funcionarioPage()
    ui.setupUi(funcionarioPage)
    funcionarioPage.show()
    sys.exit(app.exec_())
