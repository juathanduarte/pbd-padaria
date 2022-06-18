from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_popup_aviso(object):
    def setupUi(self, popup_aviso):
        popup_aviso.setObjectName("popup_aviso")
        popup_aviso.resize(437, 83)

        self.error_text = QtWidgets.QLineEdit(popup_aviso)
        self.error_text.setGeometry(QtCore.QRect(120, 20, 181, 20))
        self.error_text.setObjectName("error_text")

        self.sair_button = QtWidgets.QPushButton(popup_aviso)
        self.sair_button.setGeometry(QtCore.QRect(170, 50, 75, 23))
        self.sair_button.setObjectName("sair_button")

        self.retranslateUi(popup_aviso)
        QtCore.QMetaObject.connectSlotsByName(popup_aviso)

    def retranslateUi(self, popup_aviso):
        _translate = QtCore.QCoreApplication.translate
        popup_aviso.setWindowTitle(_translate("popup_aviso", "Form"))
        self.error_text.setText(_translate("popup_aviso", "Ocorreu um erro, tente novamente!"))
        self.sair_button.setText(_translate("popup_aviso", "Sair"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    popup_aviso = QtWidgets.QWidget()
    ui = Ui_popup_aviso()
    ui.setupUi(popup_aviso)
    popup_aviso.show()
    sys.exit(app.exec_())
