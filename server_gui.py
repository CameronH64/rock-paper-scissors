from PyQt5 import QtCore, QtGui, QtWidgets
from rock_paper_scissors_server import Server



class Ui_Dialog(object):

    def __init__(self):
        self.server_address_textfield = None
        self.port_number_textfield = None
        self.server_address_label = None
        self.port_number_label = None
        self.information_display_label = None
        self.server_log_label = None
        self.server_log_textarea = None
        self.close_server_button = None
        self.start_server_button = None

        self.rps_server = Server()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(405, 385)

        self.start_server_button = QtWidgets.QPushButton(Dialog)
        self.start_server_button.setGeometry(QtCore.QRect(100, 340, 91, 23))
        self.start_server_button.setObjectName("start_server_button")
        self.start_server_button.clicked.connect(self.rps_server.start_server)

        self.close_server_button = QtWidgets.QPushButton(Dialog)
        self.close_server_button.setGeometry(QtCore.QRect(210, 340, 91, 23))
        self.close_server_button.setObjectName("close_server_button")

        self.server_log_textarea = QtWidgets.QTextBrowser(Dialog)
        self.server_log_textarea.setGeometry(QtCore.QRect(30, 40, 341, 151))
        self.server_log_textarea.setObjectName("server_log_textarea")

        self.server_log_label = QtWidgets.QLabel(Dialog)
        self.server_log_label.setGeometry(QtCore.QRect(30, 10, 101, 16))
        self.server_log_label.setObjectName("server_log_label")

        self.information_display_label = QtWidgets.QLabel(Dialog)
        self.information_display_label.setGeometry(QtCore.QRect(40, 200, 141, 16))
        self.information_display_label.setObjectName("information_display_label")

        self.port_number_label = QtWidgets.QLabel(Dialog)
        self.port_number_label.setGeometry(QtCore.QRect(90, 240, 101, 16))
        self.port_number_label.setObjectName("port_number_label")

        self.server_address_label = QtWidgets.QLabel(Dialog)
        self.server_address_label.setGeometry(QtCore.QRect(90, 270, 101, 16))
        self.server_address_label.setObjectName("server_address_label")

        self.port_number_textfield = QtWidgets.QLineEdit(Dialog)
        self.port_number_textfield.setGeometry(QtCore.QRect(200, 240, 113, 20))
        self.port_number_textfield.setObjectName("port_number_textfield")

        self.server_address_textfield = QtWidgets.QLineEdit(Dialog)
        self.server_address_textfield.setGeometry(QtCore.QRect(200, 270, 113, 20))
        self.server_address_textfield.setText("")
        self.server_address_textfield.setObjectName("server_address_textfield")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.start_server_button.setText(_translate("Dialog", "Start Server"))
        self.close_server_button.setText(_translate("Dialog", "Close Server"))
        self.server_log_textarea.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.server_log_label.setText(_translate("Dialog", "Server Log"))
        self.information_display_label.setText(_translate("Dialog", "Information Display:"))
        self.port_number_label.setText(_translate("Dialog", "Port Number: "))
        self.server_address_label.setText(_translate("Dialog", "Server Address: "))


if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
