from this import s
from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2

import variaveisControle

host = variaveisControle.host
user = variaveisControle.user
password = variaveisControle.password
database = variaveisControle.database
port = variaveisControle.port

class Ui_exclusao_funcionario(object):
    def setupUi(self, exclusao_funcionario):
        exclusao_funcionario.setObjectName("exclusao_funcionario")
        exclusao_funcionario.resize(254, 90)

        self.nomeFuncionario = QtWidgets.QLabel(exclusao_funcionario)
        self.nomeFuncionario.setGeometry(QtCore.QRect(10, 10, 71, 20))
        self.nomeFuncionario.setObjectName("nomeFuncionario")

        self.search_excluir_Funcionario = QtWidgets.QLineEdit(exclusao_funcionario)
        self.search_excluir_Funcionario.setGeometry(QtCore.QRect(80, 10, 151, 20))
        self.search_excluir_Funcionario.setObjectName("search_excluir_Funcionario")

        self.excluirFuncionario_button = QtWidgets.QPushButton(exclusao_funcionario)
        self.excluirFuncionario_button.setGeometry(QtCore.QRect(140, 40, 91, 31))
        self.excluirFuncionario_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo_excluir/excluir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.excluirFuncionario_button.setIcon(icon)
        self.excluirFuncionario_button.setObjectName("excluirFuncionario_button")

        self.cancelarFuncionario_button = QtWidgets.QPushButton(exclusao_funcionario)
        self.cancelarFuncionario_button.setGeometry(QtCore.QRect(20, 40, 91, 31))
        self.cancelarFuncionario_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        self.cancelarFuncionario_button.setIcon(icon)
        self.cancelarFuncionario_button.setObjectName("cancelarFuncionario_button")

        self.retranslateUi(exclusao_funcionario)
        QtCore.QMetaObject.connectSlotsByName(exclusao_funcionario)

    def retranslateUi(self, exclusao_funcionario):
        _translate = QtCore.QCoreApplication.translate
        exclusao_funcionario.setWindowTitle(_translate("exclusao_funcionario", "Form"))
        self.nomeFuncionario.setText(_translate("exclusao_funcionario", "CPF do Funcionário:"))
        self.excluirFuncionario_button.setText(_translate("exclusao_funcionario", "Excluir da Funcionario"))
        self.cancelarFuncionario_button.setText(_translate("exclusao_funcionario", "Cancelar"))

        self.excluirFuncionario_button.clicked.connect(self.excluirFuncionario)
        self.cancelarFuncionario_button.clicked.connect(lambda: self.sairTela(exclusao_funcionario))

    def excluirFuncionario(self):
        cpfFun = self.search_excluir_Funcionario.text()
        connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)
        mycursor = connection.cursor()
        consultaSql = "SELECT DELET_FUN('"+ cpfFun + "');"
        try:
            mycursor.execute(consultaSql)
            connection.commit()
        except:
            print ("erro")

        self.search_excluir_Funcionario.setText("")
        mycursor.close()
    
    def sairTela(self, exclusao_funcionario):
        exclusao_funcionario.close()

from Imagens import imageDelete

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    exclusao_funcionario = QtWidgets.QWidget()
    ui = Ui_exclusao_funcionario()
    ui.setupUi(exclusao_funcionario)
    exclusao_funcionario.show()
    sys.exit(app.exec_())
