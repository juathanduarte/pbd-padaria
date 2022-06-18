#import s
from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2

import variaveisControle

host = variaveisControle.host
user = variaveisControle.user
password = variaveisControle.password
database = variaveisControle.database
port = variaveisControle.port

class Ui_exclusao_fornecedor(object):
    def setupUi(self, exclusao_fornecedor):
        exclusao_fornecedor.setObjectName("exclusao_fornecedor")
        exclusao_fornecedor.resize(339, 80)

        self.cnpj_fornecedor = QtWidgets.QLabel(exclusao_fornecedor)
        self.cnpj_fornecedor.setGeometry(QtCore.QRect(10, 10, 111, 20))
        self.cnpj_fornecedor.setObjectName("cnpj_fornecedor")

        self.search_fornecedor = QtWidgets.QLineEdit(exclusao_fornecedor)
        self.search_fornecedor.setGeometry(QtCore.QRect(120, 10, 201, 20))
        self.search_fornecedor.setObjectName("search_fornecedor")

        self.excluirFornecedor_button = QtWidgets.QPushButton(exclusao_fornecedor)
        self.excluirFornecedor_button.setGeometry(QtCore.QRect(170, 40, 121, 31))
        self.excluirFornecedor_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo_excluir/excluir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.excluirFornecedor_button.setIcon(icon)
        self.excluirFornecedor_button.setObjectName("excluirFornecedor_button")

        self.cancelarFornecedor_button = QtWidgets.QPushButton(exclusao_fornecedor)
        self.cancelarFornecedor_button.setGeometry(QtCore.QRect(50, 40, 121, 31))
        self.cancelarFornecedor_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        self.cancelarFornecedor_button.setIcon(icon)
        self.cancelarFornecedor_button.setObjectName("cancelarFornecedor_button")

        self.retranslateUi(exclusao_fornecedor)
        QtCore.QMetaObject.connectSlotsByName(exclusao_fornecedor)

    def retranslateUi(self, exclusao_fornecedor):
        _translate = QtCore.QCoreApplication.translate
        exclusao_fornecedor.setWindowTitle(_translate("exclusao_fornecedor", "Form"))
        self.cnpj_fornecedor.setText(_translate("exclusao_fornecedor", "CNPJ do Fornecedor:"))
        self.excluirFornecedor_button.setText(_translate("exclusao_fornecedor", "Excluir da Fornecedor"))
        self.cancelarFornecedor_button.setText(_translate("exclusao_fornecedor", "Cancelar"))

        self.excluirFornecedor_button.clicked.connect(self.excluirFornecedor)
        self.cancelarFornecedor_button.clicked.connect(lambda: self.sairTela(exclusao_fornecedor))

    def excluirFornecedor(self):
        cnpjFornecedor = self.search_fornecedor.text()
        connection = psycopg2.connect(user=user,
                                password=password,
                                host=host,
                                port=port,
                                database=database)
        mycursor = connection.cursor()
        consultaSql = "SELECT DELET_FORNECEDOR('"+cnpjFornecedor+"');"
        try:
            mycursor.execute(consultaSql)
            connection.commit()
        except:
            print ("erro")
        self.search_fornecedor.setText("")
        mycursor.close()
                
    def sairTela(self, exclusao_fornecedor):
            exclusao_fornecedor.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    exclusao_fornecedor = QtWidgets.QWidget()
    ui = Ui_exclusao_fornecedor()
    ui.setupUi(exclusao_fornecedor)
    exclusao_fornecedor.show()
    sys.exit(app.exec_())
