# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Open.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3
connectionObject = sqlite3.connect('CricketGame.db')
cursorObject = connectionObject.cursor()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 200)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 30, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.open_cb = QtWidgets.QComboBox(Form)
        self.open_cb.setGeometry(QtCore.QRect(90, 70, 121, 22))
        self.open_cb.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.open_cb.setDuplicatesEnabled(False)
        self.open_cb.setObjectName("open_cb")
        self.openbtn = QtWidgets.QPushButton(Form)
        self.openbtn.setGeometry(QtCore.QRect(120, 130, 61, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.openbtn.setFont(font)
        self.openbtn.setObjectName("openbtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Select Teams to Open"))
        self.openbtn.setText(_translate("Form", "Open"))

        x = cursorObject.execute("SELECT DISTINCT Name from Teams;")
        team = x.fetchall()
        for i in team:
            self.open_cb.addItem(i[0])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
