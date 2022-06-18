from PyQt5 import QtCore, QtGui, QtWidgets
from fornecedor_cadastro import Ui_cadastro_fornecedor
from fornecedor_excluir import Ui_exclusao_fornecedor
from fornecedor_procurarProdutoFornecido import Ui_procurador_produtofornecedor

from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem 

import psycopg2
import pandas as pd
import variaveisControle

host = variaveisControle.host
user = variaveisControle.user
password = variaveisControle.password
database = variaveisControle.database
port = variaveisControle.port

class Ui_fornecedorPage(object):
    def setupUi(self, fornecedorPage):
        fornecedorPage.setObjectName("fornecedorPage")
        fornecedorPage.resize(380, 306)

        self.cadastroCli_button = QtWidgets.QPushButton(fornecedorPage)
        self.cadastroCli_button.setGeometry(QtCore.QRect(30, 0, 101, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo_cadastro/cadastrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastroCli_button.setIcon(icon)
        self.cadastroCli_button.setObjectName("cadastroCli_button")

        self.excluirCli_button = QtWidgets.QPushButton(fornecedorPage)
        self.excluirCli_button.setGeometry(QtCore.QRect(130, 0, 101, 71))
        self.excluirCli_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logo_excluir/excluir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.excluirCli_button.setIcon(icon1)
        self.excluirCli_button.setObjectName("excluirCli_button")

        self.cestaCli_button = QtWidgets.QPushButton(fornecedorPage)
        self.cestaCli_button.setGeometry(QtCore.QRect(230, 0, 111, 71))
        self.cestaCli_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/logo_cesta/consultar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cestaCli_button.setIcon(icon2)
        self.cestaCli_button.setObjectName("cestaCli_button")

        self.retorno_bd = QtWidgets.QTableWidget(fornecedorPage)
        self.retorno_bd.setGeometry(QtCore.QRect(0, 110, 381, 191))
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

        self.NameClient = QtWidgets.QLabel(fornecedorPage)
        self.NameClient.setGeometry(QtCore.QRect(30, 80, 91, 20))
        self.NameClient.setObjectName("NameClient")

        self.search_button = QtWidgets.QPushButton(fornecedorPage)
        self.search_button.setGeometry(QtCore.QRect(280, 80, 51, 21))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pesquisar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon3)
        self.search_button.setObjectName("search_button")

        self.search_client = QtWidgets.QLineEdit(fornecedorPage)
        self.search_client.setGeometry(QtCore.QRect(120, 80, 151, 20))
        self.search_client.setObjectName("search_client")

        self.retranslateUi(fornecedorPage)
        QtCore.QMetaObject.connectSlotsByName(fornecedorPage)

    def retranslateUi(self, fornecedorPage):
        _translate = QtCore.QCoreApplication.translate
        fornecedorPage.setWindowTitle(_translate("fornecedorPage", "fornecedorPage"))
        self.cadastroCli_button.setText(_translate("fornecedorPage", "Cadastro"))
        self.excluirCli_button.setText(_translate("fornecedorPage", "Excluir"))
        self.cestaCli_button.setText(_translate("fornecedorPage", "Produto"))
        item = self.retorno_bd.horizontalHeaderItem(0)
        item.setText(_translate("fornecedorPage", "ID"))
        item = self.retorno_bd.horizontalHeaderItem(1)
        item.setText(_translate("fornecedorPage", "Nome"))
        item = self.retorno_bd.horizontalHeaderItem(2)
        item.setText(_translate("fornecedorPage", "CNPJ"))
        item = self.retorno_bd.horizontalHeaderItem(3)
        item.setText(_translate("fornecedorPage", "Telefone"))
        item = self.retorno_bd.horizontalHeaderItem(4)
        item.setText(_translate("fornecedorPage", "Email"))
        self.NameClient.setText(_translate("fornecedorPage", "Nome Fornecedor:"))
        self.search_button.setText(_translate("fornecedorPage", "BUSCAR"))
        
        self.cadastroCli_button.clicked.connect(self.abrirCadastro)
        self.excluirCli_button.clicked.connect(self.abrirExclusao)
        self.search_button.clicked.connect(self.listarFornecedor)
        self.cestaCli_button.clicked.connect(self.abrirtelaProduto)

    def abrirCadastro(self):
        self.cadastro_fornecedor = QtWidgets.QWidget()
        self.ui = Ui_cadastro_fornecedor()
        self.ui.setupUi(self.cadastro_fornecedor)
        self.cadastro_fornecedor.show()

    def abrirExclusao(self):
        self.exclusao_fornecedor = QtWidgets.QWidget()
        self.ui = Ui_exclusao_fornecedor()
        self.ui.setupUi(self.exclusao_fornecedor)
        self.exclusao_fornecedor.show()
    
    def listarFornecedor(self):
        connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)
        mycursor = connection.cursor()
        nomeConsulta = self.search_client.text  ()    
        consultaSql = "select idfornecedor, nome, cnpj, telefone, email from fornecedor where nome ilike '"+ nomeConsulta +"%';"
        mycursor.execute(consultaSql)
        myresult = mycursor.fetchall()
        df = pd.DataFrame(myresult, columns = ['ID', 'NOME', 'CNPJ', 'TELEFONE', 'EMAIL'])
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
    
    def abrirtelaProduto(self):
        self.procurador_produtofornecedor = QtWidgets.QWidget()
        self.ui = Ui_procurador_produtofornecedor()
        self.ui.setupUi(self.procurador_produtofornecedor)
        self.procurador_produtofornecedor.show()

from Imagens import imageAddCesta
from Imagens import imageCestaCliente
from Imagens import imageDeleteCesta

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fornecedorPage = QtWidgets.QWidget()
    ui = Ui_fornecedorPage()
    ui.setupUi(fornecedorPage)
    fornecedorPage.show()
    sys.exit(app.exec_())
