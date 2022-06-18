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

class Ui_procurador_produtofornecedor(object):
    def setupUi(self, procurador_produtofornecedor):
        procurador_produtofornecedor.setObjectName("procurador_produtofornecedor")
        procurador_produtofornecedor.resize(544, 300)

        self.cnpj_fornecedor = QtWidgets.QLabel(procurador_produtofornecedor)
        self.cnpj_fornecedor.setGeometry(QtCore.QRect(110, 70, 111, 20))
        self.cnpj_fornecedor.setObjectName("cnpj_fornecedor")

        self.retorno_bd = QtWidgets.QTableWidget(procurador_produtofornecedor)
        self.retorno_bd.setGeometry(QtCore.QRect(20, 110, 501, 191))
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

        self.procurarFornece_button = QtWidgets.QPushButton(procurador_produtofornecedor)
        self.procurarFornece_button.setGeometry(QtCore.QRect(380, 70, 61, 21))
        self.procurarFornece_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pesquisar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.procurarFornece_button.setIcon(icon)
        self.procurarFornece_button.setObjectName("procurarFornece_button")

        self.search_fornecedor = QtWidgets.QLineEdit(procurador_produtofornecedor)
        self.search_fornecedor.setGeometry(QtCore.QRect(220, 70, 151, 20))
        self.search_fornecedor.setText("")
        self.search_fornecedor.setObjectName("search_fornecedor")

        self.listartodos_button = QtWidgets.QPushButton(procurador_produtofornecedor)
        self.listartodos_button.setGeometry(QtCore.QRect(445, 70, 65, 21))
        self.listartodos_button.setText("")
        self.listartodos_button.setIcon(icon)
        self.listartodos_button.setObjectName("listartodos_button")

        self.retranslateUi(procurador_produtofornecedor)
        QtCore.QMetaObject.connectSlotsByName(procurador_produtofornecedor)

    def retranslateUi(self, procurador_produtofornecedor):
        _translate = QtCore.QCoreApplication.translate
        procurador_produtofornecedor.setWindowTitle(_translate("procurador_produtofornecedor", "Form"))
        self.cnpj_fornecedor.setText(_translate("procurador_produtofornecedor", "CNPJ do Fornecedor"))
        item = self.retorno_bd.horizontalHeaderItem(0)
        item.setText(_translate("procurador_produtofornecedor", "ID"))
        item = self.retorno_bd.horizontalHeaderItem(1)
        item.setText(_translate("procurador_produtofornecedor", "Nome"))
        item = self.retorno_bd.horizontalHeaderItem(2)
        item.setText(_translate("procurador_produtofornecedor", "Valor"))
        item = self.retorno_bd.horizontalHeaderItem(3)
        item.setText(_translate("procurador_produtofornecedor", "Validade"))
        item = self.retorno_bd.horizontalHeaderItem(4)
        item.setText(_translate("procurador_produtofornecedor", "Tipo"))
        item = self.retorno_bd.horizontalHeaderItem(5)
        item.setText(_translate("procurador_produtofornecedor", "Quantidade"))
        self.procurarFornece_button.setText(_translate("procurador_produtofornecedor", "Procurar"))
        self.listartodos_button.setText(_translate("procurador_produtofornecedor", "Mostrar todos"))
        self.listartodos_button.clicked.connect(self.listartodos)
        self.procurarFornece_button.clicked.connect(self.pesquisar)

    def pesquisar(self):
        connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)
        mycursor = connection.cursor()
        nomeConsulta = self.search_fornecedor.text()    
        consultaSql = "SELECT PRO.IDPRODUTO, PRO.NOME, PRO.VALOR, PRO.VALIDADE, PRO.TIPO, PRO.QUANTIDADE FROM PRODUTO AS PRO INNER JOIN FORNECE AS FORNE ON PRO.IDPRODUTO = FORNE.ID_PRODUTO WHERE FORNE.ID_FORNECEDOR = (SELECT IDFORNECEDOR FROM FORNECEDOR WHERE CNPJ = '"+nomeConsulta+"');"
        mycursor.execute(consultaSql)
        myresult = mycursor.fetchall()
        df = pd.DataFrame(myresult, columns = ['ID', 'NOME', 'VALOR', 'VALIDADE', 'TIPO', 'QUANTIDADE'])
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

    def listartodos(self):
        connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)
        mycursor = connection.cursor()
        nomeConsulta = self.search_fornecedor.text()    
        consultaSql = "SELECT PRO.IDPRODUTO, PRO.NOME, PRO.VALOR, PRO.VALIDADE, PRO.TIPO, PRO.QUANTIDADE FROM PRODUTO AS PRO INNER JOIN FORNECE AS FORNE ON PRO.IDPRODUTO = FORNE.ID_PRODUTO WHERE FORNE.ID_FORNECEDOR = (SELECT IDFORNECEDOR FROM FORNECEDOR WHERE FORNE.ID_FORNECEDOR = IDFORNECEDOR);"
        mycursor.execute(consultaSql)
        myresult = mycursor.fetchall()
        df = pd.DataFrame(myresult, columns = ['ID', 'NOME', 'VALOR', 'VALIDADE', 'TIPO', 'QUANTIDADE'])
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    procurador_produtofornecedor = QtWidgets.QWidget()
    ui = Ui_procurador_produtofornecedor()
    ui.setupUi(procurador_produtofornecedor)
    procurador_produtofornecedor.show()
    sys.exit(app.exec_())
