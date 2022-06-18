from this import s
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

class Ui_cesta_cli(object):
    def setupUi(self, cesta_cli):
        cesta_cli.setObjectName("cesta_cli")
        cesta_cli.resize(371, 301)
        cesta_cli.setStyleSheet("")

        self.NameClient = QtWidgets.QLabel(cesta_cli)
        self.NameClient.setGeometry(QtCore.QRect(20, 70, 91, 20))
        self.NameClient.setObjectName("NameClient")

        self.search_client = QtWidgets.QLineEdit(cesta_cli)
        self.search_client.setGeometry(QtCore.QRect(110, 70, 151, 20))
        self.search_client.setObjectName("search_client")

        self.retorno_bd = QtWidgets.QTableWidget(cesta_cli)
        self.retorno_bd.setGeometry(QtCore.QRect(90, 110, 211, 171))
        self.retorno_bd.setObjectName("retorno_bd")
        self.retorno_bd.setColumnCount(2)
        self.retorno_bd.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.retorno_bd.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.retorno_bd.setHorizontalHeaderItem(1, item)

        self.search_button = QtWidgets.QPushButton(cesta_cli)
        self.search_button.setGeometry(QtCore.QRect(270, 70, 61, 21))
        self.search_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pesquisar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon)
        self.search_button.setObjectName("search_button")

        self.retranslateUi(cesta_cli)
        QtCore.QMetaObject.connectSlotsByName(cesta_cli)

    def retranslateUi(self, cesta_cli):
        _translate = QtCore.QCoreApplication.translate
        cesta_cli.setWindowTitle(_translate("cesta_cli", "Form"))
        self.NameClient.setText(_translate("cesta_cli", "CPF do Cliente:"))
        item = self.retorno_bd.horizontalHeaderItem(0)
        item.setText(_translate("cesta_cli", "Nome Produto"))
        item = self.retorno_bd.horizontalHeaderItem(1)
        item.setText(_translate("cesta_cli", "Qnt_item"))
        self.search_button.clicked.connect(self.pesquisaCesta)
        self.search_button.setText(_translate("cesta_cli", "Procurar"))

    def pesquisaCesta(self):
        connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)
        mycursor = connection.cursor()
        nomeConsulta = self.search_client.text()    
        consultaSql = "SELECT P.NOME, C.QNT_ITEM FROM PRODUTO AS P INNER JOIN CESTA AS C ON P.IDPRODUTO = C.ID_PRODUTO WHERE C.ID_CLIENTE = (SELECT CES.IDCLIENTE FROM CLIENTE AS CES INNER JOIN PESSOA AS PES ON PES.IDPESSOA = CES.ID_PESSOA WHERE CPF ='" +  nomeConsulta +"');"
        mycursor.execute(consultaSql)
        myresult = mycursor.fetchall()
        df = pd.DataFrame(myresult, columns = ['Nome', 'Quantidade'])
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
    cesta_cli = QtWidgets.QWidget()
    ui = Ui_cesta_cli()
    ui.setupUi(cesta_cli)
    cesta_cli.show()
    sys.exit(app.exec_())
