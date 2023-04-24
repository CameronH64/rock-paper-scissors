from PyQt5 import QtCore, QtGui, QtWidgets
from rock_paper_scissors_client import Client


class Ui_Dialog(object):

    def __init__(self):
        self.status_label = None
        self.connection_status_label = None
        # self.enter_button = None
        self.new_game_button = None
        self.client_log_textarea = None
        self.server_address_label = None
        self.server_address_textfield = None
        self.connect_to_server_button = None
        self.scissors_label = None
        self.paper_label = None
        self.rock_label = None
        self.rock_radio_button = None
        self.paper_radio_button = None
        self.scissors_radio_button = None
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

        self.scissors_radio_button = QtWidgets.QRadioButton(Dialog)
        self.scissors_radio_button.setGeometry(QtCore.QRect(90, 420, 131, 17))
        self.scissors_radio_button.setObjectName("scissors_radio_button")

        self.paper_radio_button = QtWidgets.QRadioButton(Dialog)
        self.paper_radio_button.setGeometry(QtCore.QRect(310, 420, 131, 17))
        self.paper_radio_button.setObjectName("paper_radio_button")

        self.rock_radio_button = QtWidgets.QRadioButton(Dialog)
        self.rock_radio_button.setGeometry(QtCore.QRect(550, 420, 131, 17))
        self.rock_radio_button.setObjectName("rock_radio_button")

        self.rock_label = QtWidgets.QLabel(Dialog)
        self.rock_label.setGeometry(QtCore.QRect(70, 290, 131, 121))
        self.rock_label.setText("")
        self.rock_label.setPixmap(QtGui.QPixmap("assets/rock.jpg"))
        self.rock_label.setScaledContents(True)
        self.rock_label.setObjectName("rock_label")

        self.paper_label = QtWidgets.QLabel(Dialog)
        self.paper_label.setGeometry(QtCore.QRect(300, 260, 171, 161))
        self.paper_label.setText("")
        self.paper_label.setPixmap(QtGui.QPixmap("assets/paper.jpg"))
        self.paper_label.setScaledContents(True)
        self.paper_label.setObjectName("paper_label")

        self.scissors_label = QtWidgets.QLabel(Dialog)
        self.scissors_label.setGeometry(QtCore.QRect(520, 260, 161, 161))
        self.scissors_label.setText("")
        self.scissors_label.setPixmap(QtGui.QPixmap("assets/scissors.png"))
        self.scissors_label.setScaledContents(True)
        self.scissors_label.setObjectName("scissors_label")

        self.connect_to_server_button = QtWidgets.QPushButton(Dialog)
        self.connect_to_server_button.setGeometry(QtCore.QRect(240, 220, 111, 23))
        self.connect_to_server_button.setObjectName("connect_to_server_button")
        self.connect_to_server_button.clicked.connect(lambda: self.rps_client.setup_client(self.server_address_textfield.text()))
        self.connect_to_server_button.clicked.connect(lambda: self.status_label.setStyleSheet("QLabel { color: green }"))
        self.connect_to_server_button.clicked.connect(lambda: self.status_label.setText("Connected"))

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

        # self.enter_button = QtWidgets.QPushButton(Dialog)
        # self.enter_button.setGeometry(QtCore.QRect(420, 40, 111, 23))
        # self.enter_button.setObjectName("enter_button")

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
        self.scissors_radio_button.setText(_translate("Dialog", "Rock"))
        self.paper_radio_button.setText(_translate("Dialog", "Paper"))
        self.rock_radio_button.setText(_translate("Dialog", "Scissors"))
        self.connect_to_server_button.setText(_translate("Dialog", "Connect to Server"))
        self.server_address_label.setText(_translate("Dialog", "Server Address: "))
        self.new_game_button.setText(_translate("Dialog", "New Game"))
        # self.enter_button.setText(_translate("Dialog", "Enter"))
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
