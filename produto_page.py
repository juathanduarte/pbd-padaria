from PyQt5 import QtCore, QtGui, QtWidgets
from produto_cadastro import Ui_cadastro_produto
from produto_excluir import Ui_exclusao_produto
from produto_atualizapreco import Ui_AtualizarProduto
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem 

import psycopg2
import pandas as pd
import variaveisControle

host = variaveisControle.host
user = variaveisControle.user
password = variaveisControle.password
database = variaveisControle.database
port = variaveisControle.port

class Ui_produto_page(object):
    def setupUi(self, produto_page):
        produto_page.setObjectName("produto_page")
        produto_page.resize(469, 299)

        self.cadastroProd_button = QtWidgets.QPushButton(produto_page)
        self.cadastroProd_button.setGeometry(QtCore.QRect(80, 0, 101, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo_cadastro/cadastrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastroProd_button.setIcon(icon)
        self.cadastroProd_button.setObjectName("cadastroProd_button")

        self.excluirProd_button = QtWidgets.QPushButton(produto_page)
        self.excluirProd_button.setGeometry(QtCore.QRect(180, 0, 101, 71))
        self.excluirProd_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logo_excluir/excluir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.excluirProd_button.setIcon(icon1)
        self.excluirProd_button.setObjectName("excluirProd_button")

        self.cestaCli_button = QtWidgets.QPushButton(produto_page)
        self.cestaCli_button.setGeometry(QtCore.QRect(280, 0, 111, 71))
        self.cestaCli_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/logo_cesta/consultar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cestaCli_button.setIcon(icon2)
        self.cestaCli_button.setObjectName("cestaCli_button")

        self.retorno_bd = QtWidgets.QTableWidget(produto_page)
        self.retorno_bd.setGeometry(QtCore.QRect(0, 110, 471, 191))
        self.retorno_bd.setObjectName("retorno_bd")
        self.retorno_bd.setColumnCount(6)
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
        item = QtWidgets.QTableWidgetItem()
        self.retorno_bd.setHorizontalHeaderItem(5, item)

        self.NameClient = QtWidgets.QLabel(produto_page)
        self.NameClient.setGeometry(QtCore.QRect(50, 80, 91, 20))
        self.NameClient.setObjectName("NameClient")

        self.search_client = QtWidgets.QLineEdit(produto_page)
        self.search_client.setGeometry(QtCore.QRect(130, 80, 151, 20))
        self.search_client.setObjectName("search_client")

        self.search_button_2 = QtWidgets.QPushButton(produto_page)
        self.search_button_2.setGeometry(QtCore.QRect(290, 80, 51, 21))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pesquisar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button_2.setIcon(icon3)
        self.search_button_2.setObjectName("search_button_2")

        self.search_button_3 = QtWidgets.QPushButton(produto_page)
        self.search_button_3.setGeometry(QtCore.QRect(340, 80, 101, 21))
        self.search_button_3.setIcon(icon3)
        self.search_button_3.setObjectName("search_button_3")

        self.retranslateUi(produto_page)
        QtCore.QMetaObject.connectSlotsByName(produto_page)

    def retranslateUi(self, produto_page):
        _translate = QtCore.QCoreApplication.translate
        produto_page.setWindowTitle(_translate("produto_page", "produto_page"))
        self.cadastroProd_button.setText(_translate("produto_page", "Cadastrar Produdo"))
        self.excluirProd_button.setText(_translate("produto_page", "Excluir Produto"))
        self.cestaCli_button.setText(_translate("produto_page", "Atualizar Preço"))
        item = self.retorno_bd.horizontalHeaderItem(0)
        item.setText(_translate("produto_page", "Nome"))
        item = self.retorno_bd.horizontalHeaderItem(1)
        item.setText(_translate("produto_page", "Valor"))
        item = self.retorno_bd.horizontalHeaderItem(2)
        item.setText(_translate("produto_page", "Validade"))
        item = self.retorno_bd.horizontalHeaderItem(3)
        item.setText(_translate("produto_page", "Tipo"))
        item = self.retorno_bd.horizontalHeaderItem(4)
        item.setText(_translate("produto_page", "ID"))
        item = self.retorno_bd.horizontalHeaderItem(5)
        item.setText(_translate("produto_page", "Quantidade"))
        self.NameClient.setText(_translate("produto_page", "Nome Produto:"))
        self.search_button_2.setText(_translate("produto_page", "BUSCAR"))
        self.search_button_3.setText(_translate("produto_page", "MOSTRAR TODOS"))
        self.search_button_3.clicked.connect(self.imprimirTodos)
        self.search_button_2.clicked.connect(self.imprimirSelecionado)
        self.cadastroProd_button.clicked.connect(self.cadastroProduto)
        self.excluirProd_button.clicked.connect(self.excluirProduto)
        self.cestaCli_button.clicked.connect(self.atualizarPreco)
    def imprimirTodos(self):
        connection = psycopg2.connect(user=user,
                            password=password,
                            host=host,
                            port=port,
                            database=database)
        mycursor = connection.cursor()
        nomeConsulta = self.search_client.text()    
        consultaSql = "select nome, valor, validade, tipo, idproduto, quantidade from produto;"
        mycursor.execute(consultaSql)
        myresult = mycursor.fetchall()
        df = pd.DataFrame(myresult, columns = ['Nome', 'Valor', 'Validade', 'Tipo', 'ID', 'Quantidade'])
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

    def imprimirSelecionado(self):
        connection = psycopg2.connect(user=user,
                            password=password,
                            host=host,
                            port=port,
                            database=database)
        mycursor = connection.cursor()
        nomeConsulta = self.search_client.text()
        consultaSql = "select nome, valor, validade, tipo, idproduto, quantidade from produto where nome ilike '%" + nomeConsulta + "%';"
        mycursor.execute(consultaSql)
        myresult = mycursor.fetchall()
        df = pd.DataFrame(myresult, columns = ['Nome', 'Valor', 'Validade', 'Tipo', 'ID', 'Quantidade'])
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
        ##Abrir cadastro do produto
    def cadastroProduto(self):
        self.cadastro_produto = QtWidgets.QWidget()
        self.ui = Ui_cadastro_produto()
        self.ui.setupUi(self.cadastro_produto)
        self.cadastro_produto.show()
        ##Abrir exclusão do produto
    def excluirProduto(self):
        self.exclusao_produto = QtWidgets.QWidget()
        self.ui = Ui_exclusao_produto()
        self.ui.setupUi(self.exclusao_produto)
        self.exclusao_produto.show()
        ##Abrir atuliazação de preco
    def atualizarPreco(self):
        self.AtualizarProduto = QtWidgets.QMainWindow()
        self.ui = Ui_AtualizarProduto()
        self.ui.setupUi(self.AtualizarProduto)
        self.AtualizarProduto.show()
from Imagens import imageCestaCliente
from Imagens import imageDelete

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    produto_page = QtWidgets.QWidget()
    ui = Ui_produto_page()
    ui.setupUi(produto_page)
    produto_page.show()
    sys.exit(app.exec_())
