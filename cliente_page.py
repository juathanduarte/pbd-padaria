from this import s
from PyQt5 import QtCore, QtGui, QtWidgets
from cliente_cadastro import Ui_cadastro_cli
from cliente_excluir import Ui_exclusao_cliente
from cliente_cesta import Ui_cesta_cli
from cliente_excluir_cesta import Ui_excluir_cestacli
from cliente_adicionarCesta import Ui_adicionar

from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem 

import psycopg2
import pandas as pd
import variaveisControle

host = variaveisControle.host
user = variaveisControle.user
password = variaveisControle.password
database = variaveisControle.database
port = variaveisControle.port

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(517, 369)

        self.cadastroCli_button = QtWidgets.QPushButton(Form)
        self.cadastroCli_button.setGeometry(QtCore.QRect(0, 0, 101, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo_cadastro/cadastrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastroCli_button.setIcon(icon)
        self.cadastroCli_button.setObjectName("cadastroCli_button")

        self.excluirCli_button = QtWidgets.QPushButton(Form)
        self.excluirCli_button.setGeometry(QtCore.QRect(100, 0, 101, 71))
        self.excluirCli_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logo_excluir/excluir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.excluirCli_button.setIcon(icon1)
        self.excluirCli_button.setObjectName("excluirCli_button")

        self.cestaCli_button = QtWidgets.QPushButton(Form)
        self.cestaCli_button.setGeometry(QtCore.QRect(200, 0, 111, 71))
        self.cestaCli_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/logo_cesta/consultar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cestaCli_button.setIcon(icon2)
        self.cestaCli_button.setObjectName("cestaCli_button")

        self.addcesta_button = QtWidgets.QPushButton(Form)
        self.addcesta_button.setGeometry(QtCore.QRect(310, 0, 111, 71))
        self.addcesta_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/logo_adicionar/adicionar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addcesta_button.setIcon(icon3)
        self.addcesta_button.setObjectName("addcesta_button")

        self.excluircesta_button = QtWidgets.QPushButton(Form)
        self.excluircesta_button.setGeometry(QtCore.QRect(420, 0, 101, 71))
        self.excluircesta_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        self.excluircesta_button.setIcon(icon1)
        self.excluircesta_button.setObjectName("excluircesta_button")

        self.retorno_bd = QtWidgets.QTableWidget(Form)
        self.retorno_bd.setGeometry(QtCore.QRect(10, 170, 501, 191))
        self.retorno_bd.setObjectName("retorno_bd")
        self.retorno_bd.setColumnCount(5)
        self.retorno_bd.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.retorno_bd.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.retorno_bd.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.retorno_bd.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.retorno_bd.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.retorno_bd.setHorizontalHeaderItem(4, item)

        self.NameClient = QtWidgets.QLabel(Form)
        self.NameClient.setGeometry(QtCore.QRect(80, 110, 91, 20))
        self.NameClient.setObjectName("NameClient")

        self.search_button = QtWidgets.QPushButton(Form)
        self.search_button.setGeometry(QtCore.QRect(330, 110, 61, 21))
        self.search_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("pesquisar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon4)
        self.search_button.setObjectName("search_button")
        
        self.search_client = QtWidgets.QLineEdit(Form)
        self.search_client.setGeometry(QtCore.QRect(170, 110, 151, 20))
        self.search_client.setObjectName("search_client")

        self.todos_button = QtWidgets.QPushButton(Form)
        self.todos_button.setGeometry(QtCore.QRect(395, 110, 80, 21))
        self.todos_button.setText("")
        self.todos_button.setIcon(icon4)
        self.todos_button.setObjectName("todos_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        self.cadastroCli_button.setText(_translate("Form", "Cadastro"))
        self.excluirCli_button.setText(_translate("Form", "Excluir"))
        self.cestaCli_button.setText(_translate("Form", "Cesta Cliente"))
        self.addcesta_button.setText(_translate("Form", "Adicionar a Cesta"))
        self.excluircesta_button.setText(_translate("Form", "Excluir da Cesta"))
        self.search_button.setText(_translate("Form", "Procurar"))
        self.todos_button.setText(_translate("Form", "Mostrar todos"))

        item = self.retorno_bd.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.retorno_bd.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nome"))
        item = self.retorno_bd.horizontalHeaderItem(2)
        item.setText(_translate("Form", "CPF"))
        item = self.retorno_bd.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Telefone"))
        item = self.retorno_bd.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Email"))
        
        self.NameClient.setText(_translate("Form", "CPF do Cliente:"))

        self.cadastroCli_button.clicked.connect(self.tela_cadastro)
        self.excluirCli_button.clicked.connect(self.tela_excluircliente)
        self.cestaCli_button.clicked.connect(self.tela_cestaCli)
        self.addcesta_button.clicked.connect(self.tela_adicionarCesta)
        self.excluircesta_button.clicked.connect(self.tela_excluircesta)
        self.todos_button.clicked.connect(self.search_bd)
        self.search_button.clicked.connect(self.pesquisar_cliente)

    def tela_cadastro(self):
        self.cadastro_cli = QtWidgets.QWidget()
        self.ui = Ui_cadastro_cli()
        self.ui.setupUi(self.cadastro_cli)
        self.cadastro_cli.show()

    def tela_excluircliente(self):
        self.exclusao_cliente = QtWidgets.QWidget()
        self.ui = Ui_exclusao_cliente()
        self.ui.setupUi(self.exclusao_cliente)
        self.exclusao_cliente.show()
        
    def tela_cestaCli(self):
        self.cesta_cli = QtWidgets.QWidget()
        self.ui = Ui_cesta_cli()
        self.ui.setupUi(self.cesta_cli)
        self.cesta_cli.show()

    def tela_adicionarCesta(self):
        self.adicionar = QtWidgets.QWidget()
        self.ui = Ui_adicionar()
        self.ui.setupUi(self.adicionar)
        self.adicionar.show()

    def tela_excluircesta(self):
        self.excluir_cestacli = QtWidgets.QWidget()
        self.ui = Ui_excluir_cestacli()
        self.ui.setupUi(self.excluir_cestacli)
        self.excluir_cestacli.show()

    def search_bd(self):
        connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)
        mycursor = connection.cursor()
        mycursor.execute("SELECT C.IDCLIENTE, P.NOME, P.CPF, P.TELEFONE, P.EMAIL FROM PESSOA AS P INNER JOIN CLIENTE AS C ON P.IDPESSOA = C.ID_PESSOA;")
        myresult = mycursor.fetchall()
        df = pd.DataFrame(myresult, columns = ['ID', 'NOME', 'CPF', 'TELEFONE', 'EMAIL'])
        self.all_data = df
        numRows = len(self.all_data.index)
        self.retorno_bd.setColumnCount(len(self.all_data.columns))
        self.retorno_bd.setRowCount(numRows)
        self.retorno_bd.setHorizontalHeaderLabels(self.all_data.columns)
        for i in range(numRows):
            for j in range(len(self.all_data.columns)):
                self.retorno_bd.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i,j])))
        self.retorno_bd.resizeColumnsToContents()
        self.retorno_bd.resizeRowsToContents()
        mycursor.close()

    def pesquisar_cliente(self):
        connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)
        mycursor = connection.cursor()
        nomeConsulta = self.search_client.text()    
        consultaSql = "SELECT C.IDCLIENTE, P.NOME, P.CPF, P.TELEFONE, P.EMAIL FROM PESSOA AS P INNER JOIN CLIENTE AS C ON P.IDPESSOA = C.ID_PESSOA WHERE P.CPF = '" + nomeConsulta + "';"
        mycursor.execute(consultaSql)
        myresult = mycursor.fetchall()
        df = pd.DataFrame(myresult, columns = ['ID', 'NOME', 'CPF', 'TELEFONE', 'EMAIL'])
        self.all_data = df
        numRows = len(self.all_data.index)
        self.retorno_bd.setColumnCount(len(self.all_data.columns))
        self.retorno_bd.setRowCount(numRows)
        self.retorno_bd.setHorizontalHeaderLabels(self.all_data.columns)
        for i in range(numRows):
            for j in range(len(self.all_data.columns)):
                self.retorno_bd.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i,j])))
        self.retorno_bd.resizeColumnsToContents()
        self.retorno_bd.resizeRowsToContents()
        mycursor.close()

from Imagens import imageCadastro
from Imagens import imageCestaCliente
from Imagens import imageDelete
from Imagens import imageDeleteCesta

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
