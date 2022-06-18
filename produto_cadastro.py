from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2

import variaveisControle

host = variaveisControle.host
user = variaveisControle.user
password = variaveisControle.password
database = variaveisControle.database
port = variaveisControle.port

class Ui_cadastro_produto(object):
    def setupUi(self, cadastro_produto):
        cadastro_produto.setObjectName("cadastro_produto")
        cadastro_produto.resize(351, 235)

        self.Nome_Fornecedor = QtWidgets.QLabel(cadastro_produto)
        self.Nome_Fornecedor.setGeometry(QtCore.QRect(40, 40, 91, 20))
        self.Nome_Fornecedor.setObjectName("Nome_Fornecedor")

        self.search_name = QtWidgets.QLineEdit(cadastro_produto)
        self.search_name.setGeometry(QtCore.QRect(130, 40, 181, 20))
        self.search_name.setObjectName("search_name")

        self.Telefone_Fornecedor = QtWidgets.QLabel(cadastro_produto)
        self.Telefone_Fornecedor.setGeometry(QtCore.QRect(40, 70, 101, 20))
        self.Telefone_Fornecedor.setObjectName("Telefone_Fornecedor")

        self.search_telefone = QtWidgets.QLineEdit(cadastro_produto)
        self.search_telefone.setGeometry(QtCore.QRect(130, 70, 181, 20))
        self.search_telefone.setObjectName("search_telefone")

        self.Email_Fornecedor = QtWidgets.QLabel(cadastro_produto)
        self.Email_Fornecedor.setGeometry(QtCore.QRect(40, 100, 91, 20))
        self.Email_Fornecedor.setObjectName("Email_Fornecedor")

        self.search_Email = QtWidgets.QLineEdit(cadastro_produto)
        self.search_Email.setGeometry(QtCore.QRect(130, 100, 181, 20))
        self.search_Email.setObjectName("search_Email")

        self.CNPJ_Fornecedor = QtWidgets.QLabel(cadastro_produto)
        self.CNPJ_Fornecedor.setGeometry(QtCore.QRect(40, 130, 91, 20))
        self.CNPJ_Fornecedor.setObjectName("CNPJ_Fornecedor")

        self.search_cpf = QtWidgets.QLineEdit(cadastro_produto)
        self.search_cpf.setGeometry(QtCore.QRect(130, 130, 181, 20))
        self.search_cpf.setObjectName("search_cpf")

        self.cancelar_button = QtWidgets.QPushButton(cadastro_produto)
        self.cancelar_button.setGeometry(QtCore.QRect(40, 170, 81, 51))
        self.cancelar_button.setStyleSheet("image: url(:cliente/logo_cliente/cliente.png)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo_excluir/excluir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelar_button.setIcon(icon)
        self.cancelar_button.setObjectName("cancelar_button")

        self.cadastroCli_button = QtWidgets.QPushButton(cadastro_produto)
        self.cadastroCli_button.setGeometry(QtCore.QRect(230, 170, 81, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logo_cadastro/cadastrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastroCli_button.setIcon(icon1)
        self.cadastroCli_button.setObjectName("cadastroCli_button")

        self.ID_Fornecedor = QtWidgets.QLabel(cadastro_produto)
        self.ID_Fornecedor.setGeometry(QtCore.QRect(40, 10, 91, 20))
        self.ID_Fornecedor.setObjectName("ID_Fornecedor")

        self.search_name_2 = QtWidgets.QLineEdit(cadastro_produto)
        self.search_name_2.setGeometry(QtCore.QRect(130, 10, 181, 20))
        self.search_name_2.setObjectName("search_name_2")

        self.retranslateUi(cadastro_produto)
        QtCore.QMetaObject.connectSlotsByName(cadastro_produto)

    def retranslateUi(self, cadastro_produto):
        _translate = QtCore.QCoreApplication.translate
        cadastro_produto.setWindowTitle(_translate("cadastro_produto", "Form"))
        self.Nome_Fornecedor.setText(_translate("cadastro_produto", "Valor"))
        self.Telefone_Fornecedor.setText(_translate("cadastro_produto", "Validade"))
        self.Email_Fornecedor.setText(_translate("cadastro_produto", "Tipo"))
        self.CNPJ_Fornecedor.setText(_translate("cadastro_produto", "Quantidade"))
        self.cancelar_button.setText(_translate("cadastro_produto", "Cancelar"))
        self.cadastroCli_button.setText(_translate("cadastro_produto", "Cadastro"))
        self.ID_Fornecedor.setText(_translate("cadastro_produto", "Nome "))

        ##Botoes sistema
        self.cadastroCli_button.clicked.connect(self.cadastrar)
        self.cancelar_button.clicked.connect(lambda: self.sairTela(cadastro_produto))
    def sairTela(self, cadastro_produto):
        cadastro_produto.close()

    def cadastrar(self):
        nome = self.search_name_2.text()
        valor = self.search_name.text()
        validade = self.search_telefone.text()
        tipo = self.search_Email.text()
        quantidade = self.search_cpf.text()
        connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)
        mycursor = connection.cursor()
        consultaSQL = "SELECT ADD_PRODUCT('"+nome+"',"+valor+",'"+validade+"','"+tipo+"',"+quantidade+");"
        print(consultaSQL)
        try:
            mycursor.execute(consultaSQL)
            connection.commit()
        except:
            print("error")
        mycursor.close()
        self.search_name.setText("")
        self.search_name_2.setText("")
        self.search_telefone.setText("")
        self.search_Email.setText("")
        self.search_cpf.setText("") 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cadastro_produto = QtWidgets.QWidget()
    ui = Ui_cadastro_produto()
    ui.setupUi(cadastro_produto)
    cadastro_produto.show()
    sys.exit(app.exec_())
