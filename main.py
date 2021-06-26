# -*- coding: utf-8 -*-

from os import times
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import random
import time
import sys
import datetime
from verb import verb

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(433, 360)
                MainWindow.setMinimumSize(QtCore.QSize(433, 360))
                MainWindow.setMaximumSize(QtCore.QSize(433, 360))
                MainWindow.setStyleSheet("color:white;\n"
        "background-color: rgb(61, 56, 70);")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
                self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 411, 301))
                self.layoutWidget.setObjectName("layoutWidget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout.setObjectName("verticalLayout")
                self.gridLayout = QtWidgets.QGridLayout()
                self.gridLayout.setObjectName("gridLayout")
                self.ru_verb = QtWidgets.QLabel(self.layoutWidget)
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.ru_verb.setFont(font)
                self.ru_verb.setStyleSheet("margin:10px;\n"
        "background-color: rgb(153, 193, 241);\n"
        "border-radius: 10px;")
                self.ru_verb.setText("")
                self.ru_verb.setAlignment(QtCore.Qt.AlignCenter)
                self.ru_verb.setObjectName("ru_verb")
                self.gridLayout.addWidget(self.ru_verb, 0, 0, 1, 1)
                self.verticalLayout.addLayout(self.gridLayout)
                self.ru_verb_complete = QtWidgets.QLabel(self.layoutWidget)
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.ru_verb_complete.setFont(font)
                self.ru_verb_complete.setStyleSheet("background-color: rgb(249, 240, 107);\n"
        "margin:10px;\n"
        "border-radius:10px;")
                self.ru_verb_complete.setText("")
                self.ru_verb_complete.setAlignment(QtCore.Qt.AlignCenter)
                self.ru_verb_complete.setObjectName("ru_verb_complete")
                self.verticalLayout.addWidget(self.ru_verb_complete)
                self.en_verb_complete = QtWidgets.QLabel(self.layoutWidget)
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.en_verb_complete.setFont(font)
                self.en_verb_complete.setStyleSheet("background-color: rgb(246, 97, 81);\n"
        "border-radius:10px;\n"
        "margin:10px;")
                self.en_verb_complete.setText("")
                self.en_verb_complete.setAlignment(QtCore.Qt.AlignCenter)
                self.en_verb_complete.setObjectName("en_verb_complete")
                self.verticalLayout.addWidget(self.en_verb_complete)
                self.skip = QtWidgets.QPushButton(self.centralwidget)
                self.skip.setGeometry(QtCore.QRect(400, 10, 21, 21))
                self.skip.setStyleSheet("border-radius:10px;\n"
        "font: 16pt \"Cantarell\";\n"
        "background-color: rgb(245, 194, 17);\n"
        "\n"
        "")
                self.skip.setObjectName("skip")
                self.submit = QtWidgets.QPushButton(self.centralwidget)
                self.submit.setGeometry(QtCore.QRect(370, 320, 41, 27))
                self.submit.setMaximumSize(QtCore.QSize(70, 100))
                self.submit.setStyleSheet("background-color: rgb(46, 194, 126);\n"
        "border-radius:10px;\n"
        "color:white;\n"
        "border-radius:10px;")
                self.submit.setObjectName("submit")
                self.answer = QtWidgets.QLineEdit(self.centralwidget)
                self.answer.setGeometry(QtCore.QRect(10, 320, 371, 27))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.answer.sizePolicy().hasHeightForWidth())
                self.answer.setSizePolicy(sizePolicy)
                self.answer.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.answer.setStyleSheet("background-color: rgb(154, 153, 150);\n"
        "border-radius:5px;\n"
        "margin-left:10px;")
                self.answer.setObjectName("answer")
                self.help = QtWidgets.QPushButton(self.centralwidget)
                self.help.setGeometry(QtCore.QRect(400, 210, 21, 21))
                self.help.setStyleSheet("border-radius:10px;\n"
        "font: 16pt \"Cantarell\";\n"
        "background-color: rgb(98, 160, 234);\n"
        "\n"
        "")
                self.help.setObjectName("help")
                self.submit.raise_()
                self.layoutWidget.raise_()
                self.skip.raise_()
                self.answer.raise_()
                self.help.raise_()
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "500 Comman Russian Verbs"))
                self.skip.setText(_translate("MainWindow", "x"))
                self.submit.setText(_translate("MainWindow", "  C"))
                self.help.setText(_translate("MainWindow", "?"))

                self.verb = None
                self.submit.clicked.connect(self.clear)
                self.skip.clicked.connect(self.skipclicked)
                self.help.clicked.connect(self.help_clicked)
                self.answer.returnPressed.connect(self.clicked_submit)
                self.init()

        def clear(self):
                self.answer.clear()

        def skipclicked(self):
                self.verb.point = int(self.verb.point)+100
                self.verb.last_date = str(datetime.datetime.now())[:10]
                self.verb.update()
                self.clear()
                self.init()
        def help_clicked(self):
                self.en_verb_complete.setText(" / ".join(self.verb.en_complete_verb.split("/")))

        def clicked_submit(self):
                answer = self.answer.text()
                if self.check(answer) and self.verb:
                        self.verb.point = int(self.verb.point)+10
                        self.verb.last_date = str(datetime.datetime.now())[:10]
                        self.verb.update()
                else:
                        self.en_verb_complete.setText("/".join(self.verb.en_complete_verb.lower().strip().split(",")))
                        time.sleep(3) 
                        self.verb.point = int(self.verb.point)-10
                        self.verb.last_date = str(datetime.datetime.now())[:10]
                        self.verb.update()   
                self.init()

        def check(self,answer):
                return answer in str(self.verb.en_complete_verb).split(",")

        def fill_controlls(self,ru:str="",ru_1:str="",en:str=""):
                self.ru_verb.setText(ru)
                self.ru_verb_complete.setText(ru_1)
                self.en_verb_complete.setText(en)

        def init(self): 
                self.clear()      
                self.verb = verb()
                ru_0=self.verb.ru_verb
                ru_1 = " / ".join(self.verb.ru_complete_verb.split(";"))
                en_0=" / ".join(self.verb.en_complete_verb.split("/"))
                try:
                        if int(self.verb.point)<10:
                                self.fill_controlls(ru_0,ru_1,en_0)
                        else:
                                self.fill_controlls(ru_0,ru_1,"")
                except:
                        self.fill_controlls(ru_0,ru_1,"")

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
