from this import s
from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2

import variaveisControle

host = variaveisControle.host
user = variaveisControle.user
password = variaveisControle.password
database = variaveisControle.database
port = variaveisControle.port

class Ui_excluir_cestacli(object):
    def setupUi(self, excluir_cestacli):
        excluir_cestacli.setObjectName("excluir_cestacli")
        excluir_cestacli.resize(323, 176)

        self.idCesta = QtWidgets.QLabel(excluir_cestacli)
        self.idCesta.setGeometry(QtCore.QRect(50, 40, 61, 20))
        self.idCesta.setObjectName("idCesta")

        self.search_id = QtWidgets.QLineEdit(excluir_cestacli)
        self.search_id.setGeometry(QtCore.QRect(100, 40, 151, 20))
        self.search_id.setText("")
        self.search_id.setObjectName("search_id")

        self.cancelar_button = QtWidgets.QPushButton(excluir_cestacli)
        self.cancelar_button.setGeometry(QtCore.QRect(50, 90, 101, 71))
        self.cancelar_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo_excluir/excluir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelar_button.setIcon(icon)
        self.cancelar_button.setObjectName("cancelar_button")

        self.excluircesta_button = QtWidgets.QPushButton(excluir_cestacli)
        self.excluircesta_button.setGeometry(QtCore.QRect(170, 90, 101, 71))
        self.excluircesta_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        self.excluircesta_button.setIcon(icon)
        self.excluircesta_button.setObjectName("excluircesta_button")

        self.retranslateUi(excluir_cestacli)
        QtCore.QMetaObject.connectSlotsByName(excluir_cestacli)

    def retranslateUi(self, excluir_cestacli):
        _translate = QtCore.QCoreApplication.translate
        excluir_cestacli.setWindowTitle(_translate("excluir_cestacli", "Form"))
        self.idCesta.setText(_translate("excluir_cestacli", "Id Cesta:"))
        self.cancelar_button.setText(_translate("excluir_cestacli", "Cancelar"))
        self.excluircesta_button.setText(_translate("excluir_cestacli", "Excluir da Cesta"))
        self.excluircesta_button.clicked.connect(self.excluircesta)
        self.cancelar_button.clicked.connect(lambda: self.sairTela(excluir_cestacli))

    def excluircesta(self):
        cesta = self.search_id.text()
        connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)
        mycursor = connection.cursor()
        consultaSql = "SELECT DELET_CESTA('"+ cesta + "');"
        try:
            mycursor.execute(consultaSql)
            connection.commit()
        except:
            print ("erro")
        self.search_id.setText("")
        mycursor.close()
    
    def sairTela(self, exclusao_cesta):
        exclusao_cesta.close()

from Imagens import imageDelete

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    excluir_cestacli = QtWidgets.QWidget()
    ui = Ui_excluir_cestacli()
    ui.setupUi(excluir_cestacli)
    excluir_cestacli.show()
    sys.exit(app.exec_())
