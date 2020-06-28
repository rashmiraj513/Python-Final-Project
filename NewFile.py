# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 200)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 40, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.teamname_line = QtWidgets.QLineEdit(Form)
        self.teamname_line.setGeometry(QtCore.QRect(40, 90, 211, 31))
        self.teamname_line.setObjectName("teamname_line")
        self.save_btn = QtWidgets.QPushButton(Form)
        self.save_btn.setGeometry(QtCore.QRect(100, 150, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.save_btn.setFont(font)
        self.save_btn.setObjectName("save_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Enter Team Name:"))
        self.teamname_line.setPlaceholderText(_translate("Form", "Enter Team Title"))
        self.save_btn.setText(_translate("Form", "Save"))
        self.save_btn.setShortcut(_translate("Form", "Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
