# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from scoreFile import Ui_Form as score

import sqlite3
connectionObject = sqlite3.connect('cricketgame.db')
cursorObject = connectionObject.cursor()

class Ui_Form(object):
    def __init__(self):
        self.scoreDialog = QtWidgets.QMainWindow()
        self.score_screen = score()
        self.score_screen.setupUi(self.scoreDialog)
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 400)
        self.elabel = QtWidgets.QLabel(Form)
        self.elabel.setGeometry(QtCore.QRect(120, 20, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.elabel.setFont(font)
        self.elabel.setObjectName("elabel")
        self.selectteam_cb = QtWidgets.QComboBox(Form)
        self.selectteam_cb.setGeometry(QtCore.QRect(120, 80, 150, 22))
        self.selectteam_cb.setObjectName("selectteam_cb")
        self.selectmatch_cb = QtWidgets.QComboBox(Form)
        self.selectmatch_cb.setGeometry(QtCore.QRect(340, 80, 150, 22))
        self.selectmatch_cb.setObjectName("selectmatch_cb")
        self.players_lw = QtWidgets.QListWidget(Form)
        self.players_lw.setGeometry(QtCore.QRect(40, 160, 256, 192))
        self.players_lw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.players_lw.setObjectName("players_lw")
        self.scores_lw = QtWidgets.QListWidget(Form)
        self.scores_lw.setGeometry(QtCore.QRect(330, 160, 256, 192))
        self.scores_lw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scores_lw.setObjectName("scores_lw")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 120, 581, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.calcscore_btn = QtWidgets.QPushButton(Form)
        self.calcscore_btn.setGeometry(QtCore.QRect(240, 360, 151, 28))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.calcscore_btn.setFont(font)
        self.calcscore_btn.setObjectName("calcscore_btn")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(330, 140, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.totalpoints = QtWidgets.QLabel(Form)
        self.totalpoints.setGeometry(QtCore.QRect(400, 140, 55, 16))
        self.totalpoints.setObjectName("totalpoints")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.calcscore_btn.clicked.connect(self.final_score)
        selected_team = self.selectteam_cb.currentText()
        #print(selected_team)
        self.changedname(selected_team)

        self.selectteam_cb.currentTextChanged.connect(self.fetch_name)
        #self.changedname('CSK')
        #self.final_score()

    def fetch_name(self):
        selected = self.selectteam_cb.currentText()
        self.changedname(selected)

    def changedname(self,t):
        self.players_lw.clear()
        self.scores_lw.clear()
        #print(t)
        y = cursorObject.execute("SELECT Players from Teams WHERE Name = '" + t + "';")
        player = y.fetchall()
        #print('player',player)
        for j in player:
            self.players_lw.addItem(j[0])
        z = cursorObject.execute("SELECT Value from Teams WHERE Name = '" + t +"';")
        value = z.fetchall()

        #print(value)
        for k in value:
            self.scores_lw.addItem(str(k[0]))
        self.team_score = 0
        for i in value:
            self.team_score += i[0]


    def final_score(self):
        total_score = 0
        '''t = self.selectmatch_cb.currentText()
        print(t)
        z = cursorObject.execute("SELECT Value from Teams WHERE Name = '" + t + "';")
        value = z.fetchall()
        print('value',value)
        value = 
        for k in value:
            total_score += k[0]'''
        self.totalpoints.setText(str(self.team_score))
        self.score_screen.score_total.setText(str(self.team_score))
        self.scoreDialog.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.elabel.setText(_translate("Form", "Evaluate the performance of your fantasy"))
        self.calcscore_btn.setText(_translate("Form", "Calculate Score"))
        self.label_2.setText(_translate("Form", "Players"))
        self.label_3.setText(_translate("Form", "Points"))
        self.totalpoints.setText(_translate("Form", ""))
        for i in range(1,7):
            self.selectmatch_cb.addItem('Match %d'%(i))

        x = cursorObject.execute("SELECT DISTINCT Name from Teams;")
        team = x.fetchall()
        for i in team:
            self.selectteam_cb.addItem(i[0])       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
