# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cricket.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QMessageBox

from points_calculate import *
from newFile import Ui_Form as new
from scoreFile import Ui_Form as score
from openFile import Ui_Form as open
from evaluateFile import Ui_Form as eva

import sqlite3
connectionObject = sqlite3.connect('cricketgame.db')
cursorObject = connectionObject.cursor()

class Ui_MainWindow(object):
    def __init__(self):
        self.NewDialog = QtWidgets.QMainWindow()
        self.new_screen = new()
        self.new_screen.setupUi(self.NewDialog)

        self.EvaluateWindow = QtWidgets.QMainWindow()
        self.eval_screen = eva()
        self.eval_screen.setupUi(self.EvaluateWindow)

        self.openDialog = QtWidgets.QMainWindow()
        self.open_screen = open()
        self.open_screen.setupUi(self.openDialog)

    def setupUi(self, MainWindow):
        self.avail_points = 1000
        self.used_points = 0
        self.totalcount = 0
        self.batsmancount = 0
        self.bowlercount = 0
        self.allroundercount = 0
        self.wicketkeepercount = 0

        self.bat_list = []      # Batsman list.
        self.bowl_list = []     # Bowlers list.
        self.ar_list = []       # All Rounders list.
        self.wk_list = []       # Wicket Keepers list.
        self.sp_list = []       # Selected Players list.

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 587)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 15, 10, 15)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Batsman = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.Batsman.setFont(font)
        self.Batsman.setObjectName("Batsman")
        self.horizontalLayout.addWidget(self.Batsman)
        self.bat_count = QtWidgets.QLabel(self.centralwidget)
        self.bat_count.setObjectName("bat_count")
        self.horizontalLayout.addWidget(self.bat_count)
        self.WicketKeeper = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.WicketKeeper.setFont(font)
        self.WicketKeeper.setObjectName("WicketKeeper")
        self.horizontalLayout.addWidget(self.WicketKeeper)
        self.wk_count = QtWidgets.QLabel(self.centralwidget)
        self.wk_count.setObjectName("wk_count")
        self.horizontalLayout.addWidget(self.wk_count)
        self.AllRounder = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.AllRounder.setFont(font)
        self.AllRounder.setObjectName("AllRounder")
        self.horizontalLayout.addWidget(self.AllRounder)
        self.allrounder_count = QtWidgets.QLabel(self.centralwidget)
        self.allrounder_count.setObjectName("allrounder_count")
        self.horizontalLayout.addWidget(self.allrounder_count)
        self.Bowler = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.Bowler.setFont(font)
        self.Bowler.setObjectName("Bowler")
        self.horizontalLayout.addWidget(self.Bowler)
        self.bowler_count = QtWidgets.QLabel(self.centralwidget)
        self.bowler_count.setObjectName("bowler_count")
        self.horizontalLayout.addWidget(self.bowler_count)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(10, 15, 10, 15)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bat_rb = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.bat_rb.setFont(font)
        self.bat_rb.setObjectName("bat_rb")
        self.horizontalLayout_3.addWidget(self.bat_rb)
        self.wk_rb = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.wk_rb.setFont(font)
        self.wk_rb.setObjectName("wk_rb")
        self.horizontalLayout_3.addWidget(self.wk_rb)
        self.ar_rb = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.ar_rb.setFont(font)
        self.ar_rb.setObjectName("ar_rb")
        self.horizontalLayout_3.addWidget(self.ar_rb)
        self.bow_rb = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.bow_rb.setFont(font)
        self.bow_rb.setObjectName("bow_rb")
        self.horizontalLayout_3.addWidget(self.bow_rb)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.AvailablePoints = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.AvailablePoints.setFont(font)
        self.AvailablePoints.setObjectName("AvailablePoints")
        self.horizontalLayout_4.addWidget(self.AvailablePoints)
        self.points_available = QtWidgets.QLabel(self.centralwidget)
        self.points_available.setObjectName("points_available")
        self.horizontalLayout_4.addWidget(self.points_available)
        self.UsedPoints = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.UsedPoints.setFont(font)
        self.UsedPoints.setObjectName("UsedPoints")
        self.horizontalLayout_4.addWidget(self.UsedPoints)
        self.points_used = QtWidgets.QLabel(self.centralwidget)
        self.points_used.setObjectName("points_used")
        self.horizontalLayout_4.addWidget(self.points_used)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.AvailablePlayers = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.AvailablePlayers.setFont(font)
        self.AvailablePlayers.setObjectName("AvailablePlayers")
        self.horizontalLayout_5.addWidget(self.AvailablePlayers)
        self.SelectedPlayers = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.SelectedPlayers.setFont(font)
        self.SelectedPlayers.setObjectName("SelectedPlayers")
        self.horizontalLayout_5.addWidget(self.SelectedPlayers)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.availplayer_lw = QtWidgets.QListWidget(self.centralwidget)
        self.availplayer_lw.setObjectName("availplayer_lw")
        self.horizontalLayout_6.addWidget(self.availplayer_lw)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.selectedplayer_lw = QtWidgets.QListWidget(self.centralwidget)
        self.selectedplayer_lw.setObjectName("selectedplayer_lw")
        self.horizontalLayout_6.addWidget(self.selectedplayer_lw)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(10, 15, 10, 15)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout_8.addWidget(self.exit_button)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menuManage_Teams.addSeparator()
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        # New Team
        self.actionNEW_Team.triggered.connect(self.file_new)
        self.actionNEW_Team.setShortcutVisibleInContextMenu(True)

        # Open Team
        self.actionOPEN_Team.triggered.connect(self.file_open)
        self.actionOPEN_Team.setShortcutVisibleInContextMenu(True)

        # Save Team
        self.actionSAVE_Team.triggered.connect(self.file_save)
        self.actionSAVE_Team.setShortcutVisibleInContextMenu(True)

        # Evaluate Team
        self.actionEVALUATE_Team.triggered.connect(self.file_evaluate)
        self.actionEVALUATE_Team.setShortcutVisibleInContextMenu(True)

        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Disabling the Radio Buttons
        self.bat_rb.setEnabled(False)
        self.bow_rb.setEnabled(False)
        self.wk_rb.setEnabled(False)
        self.ar_rb.setEnabled(False)

        MainWindow.setWindowTitle('Cricket Fantasy League')
        
        # Exit Application
        self.exit_button.clicked.connect(self.quit)

        self.bat_rb.clicked.connect(self.load_players)
        self.bow_rb.clicked.connect(self.load_players)
        self.ar_rb.clicked.connect(self.load_players)
        self.wk_rb.clicked.connect(self.load_players)

        # Double Click Removing and Adding.
        self.availplayer_lw.itemDoubleClicked.connect(self.removelist1)
        self.selectedplayer_lw.itemDoubleClicked.connect(self.removelist2)

        self.new_screen.save_btn.clicked.connect(self.clickClose)
        self.stats = {}

    def clickClose(self):
        s = self.new_screen.teamname_line.text()
        self.NewDialog.close()
        self.label.setText(s)
        self.reset()

    def file_new(self):
        self.NewDialog.show()
        self.enabled()

    def file_open(self):
        self.open_screen.setupUi(self.openDialog)
        self.openDialog.show()
        self.open_screen.openbtn.clicked.connect(self.openteam)

    def file_evaluate(self):
        self.eval_screen.setupUi(self.EvaluateWindow)
        self.EvaluateWindow.show()
    
    def file_save(self):
        player_points = returnPoint()
        if not self.error():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText(" 😪Insufficient Players OR Points !!")
            msg.setWindowTitle("Fantasy Cricket")
            msg.exec_()
        elif self.error():
            try:
                cursorObject.execute("SELECT DISTINCT Name from Teams")
                x = cursorObject.fetchall()
                for i in x:
                    if self.label.text() == i[0]:
                        #print("Updated already there!!")
                        cursorObject.execute("DELETE FROM Teams WHERE Name = '" + self.label.text()  + "';")
            except:
                #print('error')
                pass

            for i in range(self.selectedplayer_lw.count()):
                '''print('-----adding-----')
                print('teamname:',self.label.text())
                print('playername:',self.sp_list[i])
                print('points:',player_points[self.sp_list[i]])'''
                try:
                    cursorObject.execute("INSERT INTO Teams (Name, Players, Value) VALUES (?,?,?)",
                                        (self.label.text(),self.sp_list[i],player_points[self.sp_list[i]]))
                    # self.file_evaluate()
                except:
                    #print('error')
                    pass
            connectionObject.commit()
        else:
            pass

        if self.error():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setInformativeText(" Team \nSaved Successfully !!")
            msg.setWindowTitle("Fantasy Cricket")
            msg.exec_()

    def quit(self):
        msg = QMessageBox()
        msg.setWindowTitle('Exit Window')
        msg.setText('Bye')
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
        sys.exit()

    def condition1(self,cat):
        self.avail_points -= self.stats[cat]
        self.used_points += self.stats[cat]
        if cat in self.bowl_list:
            self.bowlercount += 1
        elif cat in self.bat_list:
            self.batsmancount += 1
        elif cat in self.ar_list:
            self.allroundercount += 1
        elif cat in self.wk_list:
            self.wicketkeepercount += 1

        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.bat_count.setText(str(self.batsmancount))
        self.bowler_count.setText(str(self.bowlercount))
        self.allrounder_count.setText(str(self.allroundercount))
        self.wk_count.setText(str(self.wicketkeepercount))           

    def condition2(self,cat):
        self.avail_points += self.stats[cat]
        self.used_points -= self.stats[cat]
        if cat in self.bowl_list:
            self.bowlercount -= 1
        elif cat in self.bat_list:
            self.batsmancount -= 1
        elif cat in self.ar_list:
            self.allroundercount -= 1
        elif cat in self.wk_list:
            self.wicketkeepercount -= 1

        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.bat_count.setText(str(self.batsmancount))
        self.bowler_count.setText(str(self.bowlercount))
        self.allrounder_count.setText(str(self.allroundercount))
        self.wk_count.setText(str(self.wicketkeepercount))

    def removelist1(self,item):
        self.condition1(item.text())
        self.availplayer_lw.takeItem(self.availplayer_lw.row(item))
        self.selectedplayer_lw.addItem(item.text())
        self.totalcount = self.selectedplayer_lw.count()
        self.sp_list.append(item.text())
        self.error()

    def removelist2(self,item):
        self.selectedplayer_lw.takeItem(self.selectedplayer_lw.row(item))
        self.availplayer_lw.addItem(item.text())
        self.sp_list.remove(item.text())
        #self.error()
        self.totalcount = self.selectedplayer_lw.count()
        self.condition2(item.text())

    def nameChange(self):
        teamname = self.new_screen.teamname_line.text()
        cursorObject.execute("SELECT DISTINCT Name from Teams")
        n = cursorObject.fetchall()
        for i in n:
            if i[0] == teamname:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Team with same name already exists!! \nPlease choose another name!")
                msg.setWindowTitle("Invalid Team Name")
                msg.exec_()
                return 0
            if len(teamname) == 0:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You can't leave the field blank!!")
                msg.setWindowTitle("Invalid Name Title")
                msg.exec_()
                return 0
            elif teamname.isnumeric():
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Please enter a valid teamname\n(Name must contain atleast one character)!!")
                msg.setWindowTitle("Invalid Team Name")
                msg.exec_()
                return 0
            else:
                self.reset()
                self.tname = self.new_screen.teamname_line.text()
                self.label.setText('        ' + self.tname)
                self.newDialog.close()

    def openteam(self):
        self.reset()
        teamname = self.open_screen.open_cb.currentText()
        self.label.setText(teamname)
        self.enabled()
        cursorObject.execute("SELECT Players from Teams WHERE Name = '" + teamname + "';")
        x = cursorObject.fetchall()
        score = []
        for i in x:
            cursorObject.execute("SELECT Value from Stats WHERE Player = '" + i[0] + "';")
            y = cursorObject.fetchone()
            score.append(y[0])
        # print(score)
        sum = 0
        for i in score:
            sum += i
        self.selectedplayer_lw.clear()
        self.load_players()
        for i in x:
            self.selectedplayer_lw.addItem(i[0])
            self.sp_list.append(i[0])
            self.condition1(i[0])

        self.used_points = sum
        self.avail_points = 1000 - sum
        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.openDialog.close()

    def reset(self):
        self.enabled()
        self.load_players()
        self.used_points = 0
        self.avail_points = 1000
        self.allroundercount = 0
        self.batsmancount = 0
        self.bowlercount = 0
        self.wicketkeepercount = 0
        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.bat_count.setText(str(self.batsmancount))
        self.bowler_count.setText(str(self.bowlercount))
        self.allrounder_count.setText(str(self.allroundercount))
        self.wk_count.setText(str(self.wicketkeepercount))
        self.sp_list.clear()
        self.load_players()

        self.selectedplayer_lw.clear()

    def enabled(self):
        self.bat_rb.setEnabled(True)
        self.bow_rb.setEnabled(True)
        self.wk_rb.setEnabled(True)
        self.ar_rb.setEnabled(True)

    def error(self):
        msg = QMessageBox()
        if self.wicketkeepercount > 1:
            msg.setIcon(QMessageBox.Critical)
            #msg.setText("Error")
            msg.setInformativeText("Only 1 Wicket Keeper is allowed.")
            msg.setWindowTitle("Error")
            msg.exec_()
            return 0
        elif self.totalcount > 11:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText("No more than 11 players are allowed.")
            msg.setWindowTitle("Selection Error.")
            msg.exec_()
            return 0
        elif self.totalcount < 11:
            return 0
        elif self.wicketkeepercount < 1:
            return 0
        elif self.avail_points <= -1:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText("Not enough points!")
            msg.setWindowTitle('Selection Cricket')
            msg.exec_()
            return 0
        return 1

    def load_players(self):
        Batsman = 'BAT'
        Bowler = 'BWL'
        WicketKeeper = 'WK'
        AllRounder = 'AR'
        sql1 = "SELECT Player, Value from Stats WHERE Category = '" + Batsman + "';"
        sql2 = "SELECT Player, Value from Stats WHERE Category = '" + Bowler + "';"
        sql3 = "SELECT Player, Value from Stats WHERE Category = '" + WicketKeeper + "';"
        sql4 = "SELECT Player, Value from Stats WHERE Category = '" + AllRounder + "';"

        cursorObject.execute(sql1)
        x = cursorObject.fetchall()
        cursorObject.execute(sql2)
        y = cursorObject.fetchall()
        cursorObject.execute(sql3)
        z = cursorObject.fetchall()
        cursorObject.execute(sql4)
        w = cursorObject.fetchall()

        batsman = []
        bowler = []
        wicketkeeper = []
        allrounder = [] 

        for i in x:
            batsman.append(i[0])
            self.bat_list.append(i[0])
            self.stats[i[0]] = i[1]
        
        for i in w:
            allrounder.append(i[0])
            self.ar_list.append(i[0])
            self.stats[i[0]] = i[1]

        for i in y:
            bowler.append(i[0])
            self.bowl_list.append(i[0])
            self.stats[i[0]] = i[1]

        for i in z:
            wicketkeeper.append(i[0])
            self.wk_list.append(i[0])
            self.stats[i[0]] = i[1]
        
        for i in self.sp_list:
            if i in batsman:
                batsman.remove(i)
            elif i in allrounder:
                allrounder.remove(i)
            elif i in wicketkeeper:
                wicketkeeper.remove(i)
            elif i in bowler:
                bowler.remove(i)
        
        if self.bat_rb.isChecked() == True:
            self.availplayer_lw.clear()
            for i in range(len(batsman)):
                item = QtWidgets.QListWidgetItem(batsman[i])
                self.availplayer_lw.addItem(item)
        elif self.bow_rb.isChecked() == True:
            self.availplayer_lw.clear()
            for i in range(len(bowler)):
                item = QtWidgets.QListWidgetItem(bowler[i])
                self.availplayer_lw.addItem(item)
        elif self.ar_rb.isChecked() == True:
            self.availplayer_lw.clear()
            for i in range(len(allrounder)):
                item = QtWidgets.QListWidgetItem(allrounder[i])
                self.availplayer_lw.addItem(item)
        elif self.wk_rb.isChecked() == True:
            self.availplayer_lw.clear()
            for i in range(len(wicketkeeper)):
                item = QtWidgets.QListWidgetItem(wicketkeeper[i])
                self.availplayer_lw.addItem(item)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Team Name"))
        self.Batsman.setText(_translate("MainWindow", "Batsman(BAT)"))
        self.bat_count.setText(_translate("MainWindow", " ##"))
        self.WicketKeeper.setText(_translate("MainWindow", "WicketKeeper(WK)"))
        self.wk_count.setText(_translate("MainWindow", "  ##"))
        self.AllRounder.setText(_translate("MainWindow", "AllRounder(AR)"))
        self.allrounder_count.setText(_translate("MainWindow", "  ##"))
        self.Bowler.setText(_translate("MainWindow", "Bowler(BOW)"))
        self.bowler_count.setText(_translate("MainWindow", "  ##"))
        self.bat_rb.setText(_translate("MainWindow", "Batsman"))
        self.wk_rb.setText(_translate("MainWindow", "WicketKeeper"))
        self.ar_rb.setText(_translate("MainWindow", "AllRounder"))
        self.bow_rb.setText(_translate("MainWindow", "Bowler"))
        self.AvailablePoints.setText(_translate("MainWindow", "Available Points"))
        self.points_available.setText(_translate("MainWindow", "####"))
        self.UsedPoints.setText(_translate("MainWindow", "Used Points"))
        self.points_used.setText(_translate("MainWindow", "####"))
        self.AvailablePlayers.setText(_translate("MainWindow", "Available Players"))
        self.SelectedPlayers.setText(_translate("MainWindow", "   Selected Players"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionNEW_Team.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionOPEN_Team.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionSAVE_Team.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
        self.actionEVALUATE_Team.setShortcut(_translate("MainWindow", "Ctrl+E"))        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
input()