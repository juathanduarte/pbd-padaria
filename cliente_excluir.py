from this import s
from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2

import variaveisControle

host = variaveisControle.host
user = variaveisControle.user
password = variaveisControle.password
database = variaveisControle.database
port = variaveisControle.port

class Ui_exclusao_cliente(object):
    def setupUi(self, exclusao_cliente):
        exclusao_cliente.setObjectName("exclusao_cliente")
        exclusao_cliente.resize(400, 203)

        self.NameClient = QtWidgets.QLabel(exclusao_cliente)
        self.NameClient.setGeometry(QtCore.QRect(60, 40, 91, 20))
        self.NameClient.setObjectName("NameClient")

        self.search_client = QtWidgets.QLineEdit(exclusao_cliente)
        self.search_client.setGeometry(QtCore.QRect(150, 40, 151, 20))
        self.search_client.setObjectName("search_client")

        self.excluirCliente_button = QtWidgets.QPushButton(exclusao_cliente)
        self.excluirCliente_button.setGeometry(QtCore.QRect(230, 90, 101, 71))
        self.excluirCliente_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logo_excluir/excluir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.excluirCliente_button.setIcon(icon1)
        self.excluirCliente_button.setObjectName("excluirCliente_button")

        self.cancelar_button = QtWidgets.QPushButton(exclusao_cliente)
        self.cancelar_button.setGeometry(QtCore.QRect(110, 90, 101, 71))
        self.cancelar_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        self.cancelar_button.setIcon(icon1)
        self.cancelar_button.setObjectName("cancelar_button")

        self.retranslateUi(exclusao_cliente)
        QtCore.QMetaObject.connectSlotsByName(exclusao_cliente)

    def retranslateUi(self, exclusao_cliente):
        _translate = QtCore.QCoreApplication.translate
        exclusao_cliente.setWindowTitle(_translate("exclusao_cliente", "Form"))
        self.NameClient.setText(_translate("exclusao_cliente", "CPF do Cliente:"))
        self.excluirCliente_button.setText(_translate("exclusao_cliente", "Excluir Cliente"))
        self.cancelar_button.setText(_translate("exclusao_cliente", "Cancelar"))
        self.excluirCliente_button.clicked.connect(self.excluirCliente)
        self.cancelar_button.clicked.connect(lambda: self.sairTela(exclusao_cliente))

    def excluirCliente(self):
        cpfClient = self.search_client.text()
        connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)
        mycursor = connection.cursor()
        consultaSql = "SELECT DELET_CLI('"+ cpfClient + "');"
        try:
            mycursor.execute(consultaSql)
            connection.commit()
        except:
            print ("erro")
        self.search_client.setText("")
        mycursor.close()
    
    def sairTela(self, exclusao_cliente):
        exclusao_cliente.close()

from Imagens import imageDelete

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    exclusao_cliente = QtWidgets.QWidget()
    ui = Ui_exclusao_cliente()
    ui.setupUi(exclusao_cliente)
    exclusao_cliente.show()
    sys.exit(app.exec_())
