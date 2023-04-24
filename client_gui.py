from PyQt5 import QtCore, QtGui, QtWidgets
from rock_paper_scissors_client import Client


class Ui_Dialog(object):

    def __init__(self):
        self.status_label = None
        self.connection_status_label = None
        self.enter_button = None
        self.new_game_button = None
        self.client_log_textarea = None
        self.server_address_label = None
        self.server_address_textfield = None
        self.connect_to_server_button = None
        self.squirtle_label = None
        self.charmander_label = None
        self.bulbasaur_label = None
        self.squirtle_radio_button = None
        self.charmander_radio_button = None
        self.bulbasaur_radio_button = None
        self.attack_button = None
        self.close_button = None

        self.rps_client = Client()

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(710, 482)

        self.close_button = QtWidgets.QPushButton(Dialog)
        self.close_button.setGeometry(QtCore.QRect(370, 220, 111, 23))
        self.close_button.setObjectName("close_button")

        self.attack_button = QtWidgets.QPushButton(Dialog)
        self.attack_button.setGeometry(QtCore.QRect(200, 450, 141, 23))
        self.attack_button.setObjectName("attack_button")

        self.bulbasaur_radio_button = QtWidgets.QRadioButton(Dialog)
        self.bulbasaur_radio_button.setGeometry(QtCore.QRect(90, 420, 131, 17))
        self.bulbasaur_radio_button.setObjectName("bulbasaur_radio_button")

        self.charmander_radio_button = QtWidgets.QRadioButton(Dialog)
        self.charmander_radio_button.setGeometry(QtCore.QRect(310, 420, 131, 17))
        self.charmander_radio_button.setObjectName("charmander_radio_button")

        self.squirtle_radio_button = QtWidgets.QRadioButton(Dialog)
        self.squirtle_radio_button.setGeometry(QtCore.QRect(550, 420, 131, 17))
        self.squirtle_radio_button.setObjectName("squirtle_radio_button")

        self.bulbasaur_label = QtWidgets.QLabel(Dialog)
        self.bulbasaur_label.setGeometry(QtCore.QRect(70, 290, 131, 121))
        self.bulbasaur_label.setText("")
        self.bulbasaur_label.setPixmap(QtGui.QPixmap("assets/bulbasaur.png"))
        self.bulbasaur_label.setScaledContents(True)
        self.bulbasaur_label.setObjectName("bulbasaur_label")

        self.charmander_label = QtWidgets.QLabel(Dialog)
        self.charmander_label.setGeometry(QtCore.QRect(300, 260, 171, 161))
        self.charmander_label.setText("")
        self.charmander_label.setPixmap(QtGui.QPixmap("assets/charmander.png"))
        self.charmander_label.setScaledContents(True)
        self.charmander_label.setObjectName("charmander_label")

        self.squirtle_label = QtWidgets.QLabel(Dialog)
        self.squirtle_label.setGeometry(QtCore.QRect(520, 260, 161, 161))
        self.squirtle_label.setText("")
        self.squirtle_label.setPixmap(QtGui.QPixmap("assets/squirtle.png"))
        self.squirtle_label.setScaledContents(True)
        self.squirtle_label.setObjectName("squirtle_label")

        self.connect_to_server_button = QtWidgets.QPushButton(Dialog)
        self.connect_to_server_button.setGeometry(QtCore.QRect(240, 220, 111, 23))
        self.connect_to_server_button.setObjectName("connect_to_server_button")
        self.connect_to_server_button.clicked.connect(lambda: self.rps_client.setup_client(self.server_address_textfield.text()))

        self.server_address_textfield = QtWidgets.QLineEdit(Dialog)
        self.server_address_textfield.setGeometry(QtCore.QRect(300, 40, 101, 20))
        self.server_address_textfield.setObjectName("server_address_textfield")

        self.server_address_label = QtWidgets.QLabel(Dialog)
        self.server_address_label.setGeometry(QtCore.QRect(190, 40, 81, 16))
        self.server_address_label.setObjectName("server_address_label")

        self.client_log_textarea = QtWidgets.QPlainTextEdit(Dialog)
        self.client_log_textarea.setGeometry(QtCore.QRect(190, 100, 341, 111))
        self.client_log_textarea.setObjectName("client_log_textarea")

        self.new_game_button = QtWidgets.QPushButton(Dialog)
        self.new_game_button.setEnabled(False)
        self.new_game_button.setGeometry(QtCore.QRect(370, 450, 141, 23))
        self.new_game_button.setObjectName("new_game_button")

        self.enter_button = QtWidgets.QPushButton(Dialog)
        self.enter_button.setGeometry(QtCore.QRect(420, 40, 111, 23))
        self.enter_button.setObjectName("enter_button")

        self.connection_status_label = QtWidgets.QLabel(Dialog)
        self.connection_status_label.setGeometry(QtCore.QRect(260, 70, 101, 16))
        self.connection_status_label.setObjectName("connection_status_label")

        self.status_label = QtWidgets.QLabel(Dialog)
        self.status_label.setGeometry(QtCore.QRect(370, 70, 101, 16))
        self.status_label.setStyleSheet("QLabel { color: red }")
        self.status_label.setObjectName("status_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.close_button.setText(_translate("Dialog", "Close"))
        self.attack_button.setText(_translate("Dialog", "Attack"))
        self.bulbasaur_radio_button.setText(_translate("Dialog", "Bulbasaur"))
        self.charmander_radio_button.setText(_translate("Dialog", "Charmander"))
        self.squirtle_radio_button.setText(_translate("Dialog", "Squirtle"))
        self.connect_to_server_button.setText(_translate("Dialog", "Connect to Server"))
        self.server_address_label.setText(_translate("Dialog", "Server Address: "))
        self.new_game_button.setText(_translate("Dialog", "New Game"))
        self.enter_button.setText(_translate("Dialog", "Enter"))
        self.connection_status_label.setText(_translate("Dialog", "Connection Status: "))
        self.status_label.setText(_translate("Dialog", "Disconnected"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
