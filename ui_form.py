# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources

class Ui_bla(object):
    def setupUi(self, bla):
        if not bla.objectName():
            bla.setObjectName(u"bla")
        bla.resize(1153, 647)
        bla.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(bla)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setGeometry(QRect(0, 10, 1151, 631))
        self.verticalScrollBar = QScrollBar(self.centralwidget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(1130, 30, 21, 601))
        self.verticalScrollBar.setAutoFillBackground(False)
        self.verticalScrollBar.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setEnabled(True)
        self.line.setGeometry(QRect(0, 70, 1131, 16))
        self.line.setAutoFillBackground(False)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setFrameShape(QFrame.HLine)
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(10, 330, 190, 41))
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"text-align: left;\n"
"border: 1px solid;\n"
"border-color: rgb(215, 215, 215);\n"
"icon: url(:/icons/icons/course.png);\n"
"icon-size: 20px;\n"
"padding-left: 30px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(13, 9, 145);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-color: rgb(13, 9, 145);\n"
"text-align: left;\n"
"font-weight: bold;\n"
"icon: url(:/icons/icons/course_white.png);\n"
"icon-size: 20px;\n"
"padding-left: 30px;\n"
"}\n"
"")
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setFlat(True)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(220, 90, 901, 111))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.textBrowser_2 = QTextBrowser(self.frame_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(130, 20, 256, 51))
        self.textBrowser_2.setFrameShape(QFrame.NoFrame)
        self.pushButton_11 = QPushButton(self.frame_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(20, 10, 91, 91))
        self.pushButton_11.setStyleSheet(u"icon: url(:/icons/icons/profilepic.png);\n"
"qproperty-iconSize: 90px;")
        self.pushButton_11.setFlat(True)
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(950, 480, 171, 151))
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(220, 210, 721, 421))
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(10, 290, 190, 41))
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"text-align: left;\n"
"border: 1px solid;\n"
"border-color: rgb(215, 215, 215);\n"
"icon: url(:/icons/icons/course.png);\n"
"icon-size: 20px;\n"
"padding-left: 30px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(13, 9, 145);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-color: rgb(13, 9, 145);\n"
"text-align: left;\n"
"font-weight: bold;\n"
"icon: url(:/icons/icons/course_white.png);\n"
"icon-size: 20px;\n"
"padding-left: 30px;\n"
"}\n"
"")
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setChecked(False)
        self.pushButton_8.setFlat(True)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 30, 41, 31))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"selection-background-color: rgb(156, 156, 156);\n"
"background-color: rgb(234, 234, 234);")
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(True)
        self.textBrowser_3 = QTextBrowser(self.centralwidget)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(950, 34, 141, 31))
        self.textBrowser_3.setFrameShape(QFrame.NoFrame)
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setGeometry(QRect(10, 250, 190, 41))
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"text-align: left;\n"
"border: 1px solid;\n"
"border-color: rgb(215, 215, 215);\n"
"icon: url(:/icons/icons/course.png);\n"
"icon-size: 20px;\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(13, 9, 145);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-color: rgb(13, 9, 145);\n"
"text-align: left;\n"
"font-weight: bold;\n"
"icon: url(:/icons/icons/course_white.png);\n"
"icon-size: 20px;\n"
"padding-left: 10px;\n"
"}\n"
"")
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setFlat(True)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 80, 211, 571))
        self.frame.setStyleSheet(u"background-color: rgb(238, 238, 238);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 10, 190, 41))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        font.setKerning(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"text-align: left;\n"
"border: 1px solid;\n"
"border-color: rgb(215, 215, 215);\n"
"icon: url(:/icons/icons/dash.png);\n"
"icon-size: 20px;\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(13, 9, 145);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"border: 1px solid;\n"
"border-color: rgb(13, 9, 145);\n"
"icon: url(:/icons/icons/dash_white.png);\n"
"icon-size: 20px;\n"
"padding-left: 10px;\n"
"}\n"
"")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(True)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setFlat(True)
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 50, 190, 41))
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"text-align: left;\n"
"border: 1px solid;\n"
"border-color: rgb(215, 215, 215);\n"
"icon: url(:/icons/icons/home.png);\n"
"icon-size: 20px;\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(13, 9, 145);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-color: rgb(13, 9, 145);\n"
"text-align: left;\n"
"font-weight: bold;\n"
"icon: url(:/icons/icons/home_white.png);\n"
"icon-size: 20px;\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setChecked(False)
        self.pushButton_4.setFlat(True)
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 90, 190, 41))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid;\n"
"border-color: rgb(215, 215, 215);\n"
"text-align: left;\n"
"icon: url(:/icons/icons/calender.png);\n"
"icon-size: 20px;\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(13, 9, 145);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-color: rgb(13, 9, 145);\n"
"text-align: left;\n"
"font-weight: bold;\n"
"icon: url(:/icons/icons/calender_white.png);\n"
"icon-size: 20px;\n"
"padding-left: 10px;\n"
"}\n"
"")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setFlat(True)
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(10, 130, 190, 41))
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"text-align: left;\n"
"border: 1px solid;\n"
"border-color: rgb(215, 215, 215);\n"
"icon: url(:/icons/icons/sheet.png);\n"
"icon-size: 20px;\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(13, 9, 145);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-color: rgb(13, 9, 145);\n"
"text-align: left;\n"
"font-weight: bold;\n"
"icon: url(:/icons/icons/sheet_white.png);\n"
"icon-size: 20px;\n"
"padding-left: 10px;\n"
"}\n"
"")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setFlat(False)
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(210, 100, 211, 571))
        self.frame_6.setStyleSheet(u"background-color: rgb(238, 238, 238);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.pushButton_12 = QPushButton(self.frame_6)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(10, 10, 190, 41))
        self.pushButton_12.setFont(font)
        self.pushButton_12.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_12.setAutoFillBackground(False)
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"text-align: left;\n"
"border: 1px solid;\n"
"border-color: rgb(215, 215, 215);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(13, 9, 145);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"font-weight: bold;\n"
"border: 1px solid;\n"
"border-color: rgb(13, 9, 145);\n"
"}\n"
"")
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setChecked(True)
        self.pushButton_12.setAutoDefault(False)
        self.pushButton_12.setFlat(True)
        self.pushButton_13 = QPushButton(self.frame_6)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(10, 50, 190, 41))
        self.pushButton_13.setAutoFillBackground(False)
        self.pushButton_13.setStyleSheet(u"QPushButton{\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"text-align: left;\n"
"border: 1px solid;\n"
"border-color: rgb(215, 215, 215);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(13, 9, 145);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-color: rgb(13, 9, 145);\n"
"text-align: left;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setChecked(False)
        self.pushButton_13.setFlat(True)
        self.pushButton_14 = QPushButton(self.frame_6)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(10, 90, 190, 41))
        self.pushButton_14.setFont(font)
        self.pushButton_14.setAutoFillBackground(False)
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid;\n"
"border-color: rgb(215, 215, 215);\n"
"text-align: left;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(13, 9, 145);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-color: rgb(13, 9, 145);\n"
"text-align: left;\n"
"font-weight: bold;\n"
"}\n"
"")
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setFlat(True)
        self.pushButton_15 = QPushButton(self.frame_6)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(10, 130, 190, 41))
        self.pushButton_15.setAutoFillBackground(False)
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"text-align: left;\n"
"border: 1px solid;\n"
"border-color: rgb(215, 215, 215);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(13, 9, 145);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-color: rgb(13, 9, 145);\n"
"text-align: left;\n"
"font-weight: bold;\n"
"}\n"
"")
        self.pushButton_15.setCheckable(True)
        self.pushButton_15.setAutoDefault(False)
        self.pushButton_15.setFlat(False)
        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(10, 370, 190, 41))
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"text-align: left;\n"
"border: 1px solid;\n"
"border-color: rgb(215, 215, 215);\n"
"icon: url(:/icons/icons/course.png);\n"
"icon-size: 20px;\n"
"padding-left: 30px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(13, 9, 145);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-color: rgb(13, 9, 145);\n"
"text-align: left;\n"
"font-weight: bold;\n"
"icon: url(:/icons/icons/course_white.png);\n"
"icon-size: 20px;\n"
"padding-left: 30px;\n"
"}\n"
"")
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setFlat(True)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(70, 34, 161, 31))
        self.textBrowser.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(220, 35, 93, 28))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(u"color: rgb(173, 173, 173);")
        self.pushButton_2.setFlat(True)
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(950, 210, 171, 261))
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.graphicsView = QGraphicsView(self.frame_4)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(10, 160, 151, 91))
        self.graphicsView.setStyleSheet(u"border-image: url(:/pictures/pictures/screens.png);")
        self.textBrowser_4 = QTextBrowser(self.frame_4)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(2, 20, 161, 51))
        self.textBrowser_4.setFrameShape(QFrame.NoFrame)
        self.textBrowser_5 = QTextBrowser(self.frame_4)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(10, 70, 151, 71))
        self.textBrowser_5.setFrameShape(QFrame.NoFrame)
        self.pushButton_16 = QPushButton(self.centralwidget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(830, 30, 31, 28))
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
"icon: url(:/icons/icons/bell.png);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"icon-size: 23px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"icon: url(:/icons/icons/bell_black.png);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"icon-size: 23px;\n"
"}")
        self.pushButton_16.setFlat(True)
        self.pushButton_17 = QPushButton(self.centralwidget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(880, 32, 31, 28))
        self.pushButton_17.setStyleSheet(u"QPushButton{\n"
"icon: url(:/icons/icons/bubble.png);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"icon-size: 23px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"icon: url(:/icons/icons/bubble_black.png);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"icon-size: 23px;\n"
"}")
        self.pushButton_17.setFlat(True)
        self.pushButton_18 = QPushButton(self.centralwidget)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(780, 30, 31, 28))
        self.pushButton_18.setStyleSheet(u"QPushButton{\n"
"icon: url(:/icons/icons/lupe.png);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"icon-size: 23px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"icon: url(:/icons/icons/lupe_black.png);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"icon-size: 23px;\n"
"}")
        self.pushButton_18.setFlat(True)
        self.pushButton_19 = QPushButton(self.centralwidget)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(1070, 20, 51, 51))
        self.pushButton_19.setStyleSheet(u"icon: url(:/icons/icons/profilepic.png);\n"
"qproperty-iconSize: 50px;")
        self.pushButton_19.setFlat(True)
        self.line.raise_()
        self.frame.raise_()
        self.verticalScrollBar.raise_()
        self.pushButton_9.raise_()
        self.frame_2.raise_()
        self.frame_5.raise_()
        self.frame_3.raise_()
        self.pushButton_8.raise_()
        self.pushButton.raise_()
        self.textBrowser_3.raise_()
        self.pushButton_7.raise_()
        self.pushButton_10.raise_()
        self.textBrowser.raise_()
        self.pushButton_2.raise_()
        self.frame_4.raise_()
        self.pushButton_16.raise_()
        self.pushButton_17.raise_()
        self.pushButton_18.raise_()
        self.pushButton_19.raise_()
        self.menubar = QMenuBar(bla)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1153, 26))
        self.statusbar = QStatusBar(bla)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setGeometry(QRect(0, 0, 3, 25))

        self.retranslateUi(bla)

        self.pushButton.setDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_5.setDefault(False)
        self.pushButton_12.setDefault(False)
        self.pushButton_14.setDefault(False)


        QMetaObject.connectSlotsByName(bla)
    # setupUi

    def retranslateUi(self, bla):
        bla.setWindowTitle(QCoreApplication.translate("bla", u"bla", None))
        self.pushButton_9.setText(QCoreApplication.translate("bla", u" Kurs 2", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("bla", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Student Name</span></p></body></html>", None))
        self.pushButton_11.setText("")
        self.pushButton_8.setText(QCoreApplication.translate("bla", u" Kurs 1", None))
        self.pushButton.setText(QCoreApplication.translate("bla", u"\u2261", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("bla", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#2901a1;\">Student Name</span></p></body></html>", None))
        self.pushButton_7.setText(QCoreApplication.translate("bla", u" Meine Kurse", None))
        self.pushButton_3.setText(QCoreApplication.translate("bla", u" Dashboard", None))
        self.pushButton_4.setText(QCoreApplication.translate("bla", u" Startseite", None))
        self.pushButton_5.setText(QCoreApplication.translate("bla", u" Kalender", None))
        self.pushButton_6.setText(QCoreApplication.translate("bla", u" Meine Dateien", None))
        self.pushButton_12.setText(QCoreApplication.translate("bla", u"     Dashboard", None))
        self.pushButton_13.setText(QCoreApplication.translate("bla", u"     Startseite", None))
        self.pushButton_14.setText(QCoreApplication.translate("bla", u"     Kalender", None))
        self.pushButton_15.setText(QCoreApplication.translate("bla", u"     Meine Dateien", None))
        self.pushButton_10.setText(QCoreApplication.translate("bla", u" Kurs 3", None))
        self.textBrowser.setHtml(QCoreApplication.translate("bla", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Moodle UDE</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("bla", u"Deutsch (de)", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("bla", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">Video-Anleitung: Moodle </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">f\u00fcr Studierende</span></p></body></html>", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("bla", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">Per Klick auf das nachfolgende Vorschaubild gelangen Sie zum Video.</span></p></body></html>", None))
        self.pushButton_16.setText("")
        self.pushButton_17.setText("")
        self.pushButton_18.setText("")
        self.pushButton_19.setText("")
    # retranslateUi

