from PyQt5 import QtCore, QtGui, QtWidgets

from cliente_page import Ui_Form
from funcionario_page import Ui_funcionarioPage
from fornecedor_page import Ui_fornecedorPage
from produto_page import Ui_produto_page

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(608, 381)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.sobre_grouptext = QtWidgets.QTextBrowser(self.centralwidget)
        self.sobre_grouptext.setGeometry(QtCore.QRect(140, 130, 331, 211))
        self.sobre_grouptext.setStyleSheet("image: url(:/logoempresa/icons/fornecedor.png)")
        self.sobre_grouptext.setObjectName("sobre_grouptext")

        self.cliente_button = QtWidgets.QPushButton(self.centralwidget)
        self.cliente_button.setGeometry(QtCore.QRect(0, 0, 91, 71))
        self.cliente_button.setStyleSheet("image: url(:/logo_cliente/cliente.png)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo_cliente/cliente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cliente_button.setIcon(icon)
        self.cliente_button.setObjectName("cliente_button")

        self.produto_button = QtWidgets.QPushButton(self.centralwidget)
        self.produto_button.setGeometry(QtCore.QRect(520, 0, 91, 71))
        self.produto_button.setStyleSheet("image:url(:/logo_produto/produtos.png)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logo_produto/produtos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.produto_button.setIcon(icon1)
        self.produto_button.setObjectName("produto_button")

        self.fornecedor_button = QtWidgets.QPushButton(self.centralwidget)
        self.fornecedor_button.setGeometry(QtCore.QRect(350, 0, 91, 71))
        self.fornecedor_button.setStyleSheet("image: url(:/logo_fornecedor/fornecedor.png)")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/logo_fornecedor/fornecedor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fornecedor_button.setIcon(icon2)
        self.fornecedor_button.setObjectName("fornecedor_button")

        self.funcionario_button = QtWidgets.QPushButton(self.centralwidget)
        self.funcionario_button.setGeometry(QtCore.QRect(170, 0, 91, 71))
        self.funcionario_button.setStyleSheet("image: url(:/logo_func/funcionario.png)")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/alterar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.funcionario_button.setIcon(icon3)
        self.funcionario_button.setObjectName("funcionario_button")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 608, 21))
        self.menubar.setObjectName("menubar")
        self.menuCadastro = QtWidgets.QMenu(self.menubar)
        self.menuCadastro.setObjectName("menuCadastro")
        self.menuOperacoes = QtWidgets.QMenu(self.menubar)
        self.menuOperacoes.setObjectName("menuOperacoes")
        self.menuProdutos_na_cesta = QtWidgets.QMenu(self.menuOperacoes)
        self.menuProdutos_na_cesta.setObjectName("menuProdutos_na_cesta")
        self.menuExclusao = QtWidgets.QMenu(self.menuOperacoes)
        self.menuExclusao.setObjectName("menuExclusao")
        self.menuFornecedor_2 = QtWidgets.QMenu(self.menuOperacoes)
        self.menuFornecedor_2.setObjectName("menuFornecedor_2")
        self.menuProduto_2 = QtWidgets.QMenu(self.menuOperacoes)
        self.menuProduto_2.setObjectName("menuProduto_2")
        self.menuVizualiza_o_do_banco = QtWidgets.QMenu(self.menubar)
        self.menuVizualiza_o_do_banco.setObjectName("menuVizualiza_o_do_banco")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p><img src=\":/logo_cliente/cliente.png\"/></p></body></html>"))
        self.sobre_grouptext.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Grupo 7 - Projeto de Banco de Dados<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Componentes:<br />Guilherme Dallmann Lima</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">João Paulo Brito de Almeida</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Juathan Coelho Duarte</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Padaria</span></p></body></html>"))

        self.cliente_button.clicked.connect(self.tela_client)
        self.funcionario_button.clicked.connect(self.tela_funcionario)
        self.fornecedor_button.clicked.connect(self.tela_fornecedor)
        self.produto_button.clicked.connect(self.tela_produto)

    def tela_client(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def tela_funcionario(self):
        self.funcionarioPage = QtWidgets.QWidget()
        self.ui = Ui_funcionarioPage()
        self.ui.setupUi(self.funcionarioPage)
        self.funcionarioPage.show()

    def tela_fornecedor(self):
        self.fornecedorPage = QtWidgets.QWidget()
        self.ui = Ui_fornecedorPage()
        self.ui.setupUi(self.fornecedorPage)
        self.fornecedorPage.show()

    def tela_produto(self):
        self.produto_page = QtWidgets.QWidget()
        self.ui = Ui_produto_page()
        self.ui.setupUi(self.produto_page)
        self.produto_page.show()

from Imagens import imageClient
from Imagens import imageFornecedor
from Imagens import imageFuncionario
from Imagens import imageProduto

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
