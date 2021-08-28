# This Python file uses the following encoding: utf-8
# from pathlib import Path
import sys
import resources
import io

from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from PySide2.QtCore import QFile
from PySide2 import QtCore
# from PySide2.QtUiTools import QUiLoader

from PyQt5 import uic, QtWidgets

import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from feedback import Feedback
from PyQt5.QtCore import QDate, QDateTime
import datetime
import calendar
import time

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)


global STUDENTS
STUDENTS = pd.DataFrame({
    'id': [
        '133', '143', '159', '160', '161', '163', '164', '165', '166',
        '167', '168', '169', '170', '171', '172', '173', '174', '175', '176',
        '177', '178', '179', '180', '181', '182', '183', '184', '185'],
    'randomname': [
        'Carissa Magby', 'Paris Burke', 'Syble Sinnott', 'Alda Hassinger',
        'Marilou Andreotti', 'Sharell Galyean', 'Breana Reisman',
        'Cherlyn Benites', 'Hosea Linker', 'Cheryle Layfield',
        'Ludivina Gautreaux', 'Tyree Lockett', 'Stephaine Dreiling',
        'Robert Sakai', 'Joella Darrell', 'Lynetta Lubin', 'Bo Mcfarren',
        'Garret Seidl', 'Jenine Delvalle', 'Elenore Lenahan', 'Keitha Mauk',
        'Rossana Ferrara', 'Robin Felipe', 'Ivy Landey', 'Emery Fellers',
        'Marinda Scheller', 'Jenell Moats', 'Luke Mckibben']})


class Login(QtWidgets.QWidget):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi('form2.ui', self)

        self.next = MoodleStart()
        self.pushButtonLogin.clicked.connect(self.openMoodle)
        #weekend = [1601424000,1602028800,1602633600,1603238400,1603843200,1604448000,1605052800,1605657600,1606262400,1607472000,1607904000]
        #users = [124, 133, 143, 159, 160, 161, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185]

        #for user in users:
         #   for date in weekend:
          #      print(user,date)
           #     Feedback().feedback_method(user,date)
    def openMoodle(self):
        sid = self.lineEditID.text()
        if sid not in STUDENTS.id.values:
            self.label_noid.setText("No valid ID")
        else:
            MoodleStart.currentid = sid
            MoodleStart.currentdate = self.calendarWidget.selectedDate()
            MoodleStart.currentname = STUDENTS.loc[(STUDENTS.index[STUDENTS['id'] == sid]), ('randomname')].values[0]
            self.next.showing()
            self.close()

class MoodleStart(QtWidgets.QWidget):
    currentid = '0'
    currentname = 'empty'
    currentdate = ''
    language = 'german'
    feedback_viewed = False
    feedback_text = ""
    showperformance = True
    showtimeplanning = True
    showbackgroundknowledge = True
    showengagement = True
    showavgperformance = False
    showavgtimeplanning = False
    showavgbackgroundknowledge = False
    showavgengagement = False
    weekend = [1601424000,1602028800,1602633600,1603238400,1603843200,1604448000,1605052800,1605657600,1606262400,1607472000,1607904000]
    dates = []


    def __init__(self):
        super(MoodleStart, self).__init__()
        uic.loadUi('form.ui', self)

        # hide gui parts
        self.graphicsView_calendar.hide()
        self.graphicsView_kitten.hide()
        self.graphicsView_doggo.hide()
        self.label_files.hide()
        self.label_myellow.hide()  # Feedback warning for yellow feedback
        self.label_morange.hide()  # Feedback warning for orange feedback
        self.label_mred.hide()  # Feedback warning for red feedback
        self.frame_feedback.hide()
        self.pushButton_requestFeedback.hide()
        self.textBrowser_courses.hide()
        self.textBrowser_courseDescription.hide()
        self.textBrowser_courseDescription_2.hide()
        self.textBrowser_courseDescription_3.hide()
        self.MplWidget.hide()
        self.textBrowser_performance.hide()
        self.textBrowser_timePlanning.hide()
        self.textBrowser_backgroundKnowledge.hide()
        self.textBrowser_engagement.hide()
        self.frame_options.hide()
        self.textBrowser_timeContingency.hide()

        # Exactly one button checked at all times
        self.pushButton_dash.clicked.connect(self.uncheckall)
        self.pushButton_dash.clicked.connect(self.checkdash)
        self.pushButton_home.clicked.connect(self.uncheckall)
        self.pushButton_home.clicked.connect(self.checkhome)
        self.pushButton_calendar.clicked.connect(self.uncheckall)
        self.pushButton_calendar.clicked.connect(self.checkcalendar)
        self.pushButton_files.clicked.connect(self.uncheckall)
        self.pushButton_files.clicked.connect(self.checkfiles)
        self.pushButton_mycourses.clicked.connect(self.uncheckall)
        self.pushButton_mycourses.clicked.connect(self.checkmycourses)
        self.pushButton_course1.clicked.connect(self.uncheckall)
        self.pushButton_course1.clicked.connect(self.checkcourse1)
        self.pushButton_course2.clicked.connect(self.uncheckall)
        self.pushButton_course2.clicked.connect(self.checkcourse2)
        self.pushButton_course3.clicked.connect(self.uncheckall)
        self.pushButton_course3.clicked.connect(self.checkcourse3)

        # feedback gui
        self.pushButton_x.clicked.connect(self.closefeedback)
        self.pushButton_requestFeedback.clicked.connect(self.requestfeedback)
        self.pushButton_fullFeedback.clicked.connect(self.requestfeedback)

        # Change language (only german and english)
        self.pushButton_language.clicked.connect(self.translate)

        # Hide menu
        self.pushButton_menu.clicked.connect(self.hidemenu)

        for date in self.weekend:
            self.dates += [time.strftime("%a, %d %b", time.localtime(date))]


    def showing(self):
        pydate = str(MoodleStart.currentdate.toPyDate())
        date = calendar.timegm(time.strptime(pydate, "%Y-%m-%d"))


        self.feedback_text = Feedback().feedback_method(int(self.currentid), date, False)[0]
        self.colour = Feedback().feedback_method(int(self.currentid), date, False)[1]

        self.textBrowser_feedback.setText(self.feedback_text)
        if self.colour == 2:
            self.label_myellow.show()
            self.frame_feedback.setStyleSheet("border:2px solid yellow")
        if self.colour == 3:
            self.label_morange.show()
            self.frame_feedback.setStyleSheet("border:2px solid orange")
        if self.colour == 4:
            self.label_mred.show()
            self.frame_feedback.setStyleSheet("border:2px solid red")

        self.label_nameLarge.setText(self.currentname)
        self.label_nameTiny.setText(self.currentname)

        dt = QDateTime.fromString(self.currentdate.toString() + " 15:00:00");
        timestamp = dt.toTime_t();
        self.prepareGraph(int(self.currentid), timestamp)

        self.show()

    def uncheckall(self):
        self.pushButton_dash.setChecked(False)
        self.pushButton_home.setChecked(False)
        self.pushButton_calendar.setChecked(False)
        self.pushButton_files.setChecked(False)
        self.pushButton_mycourses.setChecked(False)
        self.pushButton_course1.setChecked(False)
        self.pushButton_course2.setChecked(False)
        self.pushButton_course3.setChecked(False)

    def backtonormal(self):
        self.graphicsView_doggo.hide()
        self.graphicsView_kitten.hide()
        self.graphicsView_calendar.hide()
        self.label_files.hide()
        self.frame_middle.setGeometry(220, 210, 721, 421)
        self.frame_video.show()
        self.frame_downRight.show()
        self.textBrowser_video.show()
        self.textBrowser_videodescription.show()
        self.graphicsView_video.show()
        self.pushButton_profileLarge.show()
        self.label_nameLarge.setText(self.currentname)
        self.frame_nameandpic.setGeometry(220, 90, 901, 111)
        self.label_nameLarge.setGeometry(130, 20, 181, 31)
        self.frame_feedback.hide()
        self.pushButton_requestFeedback.hide()
        self.textBrowser_courses.hide()
        self.textBrowser_courseDescription.hide()
        self.textBrowser_courseDescription_2.hide()
        self.textBrowser_courseDescription_3.hide()
        self.MplWidget.hide()
        self.textBrowser_performance.hide()
        self.textBrowser_timePlanning.hide()
        self.textBrowser_backgroundKnowledge.hide()
        self.textBrowser_engagement.hide()
        self.frame_options.hide()
        self.textBrowser_timeContingency.hide()

    def checkdash(self):
        self.backtonormal()
        self.pushButton_dash.setChecked(True)

    def checkhome(self):
        self.backtonormal()
        self.pushButton_home.setChecked(True)

    def checkcalendar(self):
        self.backtonormal()
        self.pushButton_calendar.setChecked(True)
        self.frame_middle.setGeometry(220, 210, 900, 421)
        self.frame_video.hide()
        self.frame_downRight.hide()
        self.graphicsView_calendar.show()

    def checkfiles(self):
        self.backtonormal()
        self.pushButton_files.setChecked(True)
        self.textBrowser_video.hide()
        self.textBrowser_videodescription.hide()
        self.graphicsView_video.hide()
        self.graphicsView_kitten.show()
        self.graphicsView_doggo.show()
        self.label_files.show()

    def checkmycourses(self):
        self.backtonormal()
        self.pushButton_mycourses.setChecked(True)
        self.textBrowser_courses.show()
    # THIS IS OUR COURSE! (Hier sollte das Feedback erscheinen, vielleicht eine kurze Kursbeschreibung, auf Knopfdruck die Visualisierung...)
    def checkcourse1(self):
        self.backtonormal()
        self.pushButton_course1.setChecked(True)
        self.frame_video.hide()
        self.frame_downRight.hide()
        self.pushButton_profileLarge.hide()
        self.pushButton_requestFeedback.show()
        self.label_nameLarge.setGeometry(30, 20, 300, 31)
        self.label_nameLarge.setText("HOW TO TRAIN YOUR DRAGON")
        self.frame_nameandpic.setGeometry(220, 90, 901, 71)
        self.frame_middle.setGeometry(220, 170, 901, 461)
        if self.colour > 0 and not self.feedback_viewed:
            self.textBrowser_feedback.show()
            self.frame_feedback.show()
            self.textBrowser_courseDescription.setGeometry(230, 350, 881, 271)
        self.textBrowser_courseDescription.show()
        if self.feedback_viewed:
            self.frame_feedback.hide()
    def checkcourse2(self):
        self.backtonormal()
        self.pushButton_course2.setChecked(True)
        self.textBrowser_courseDescription_2.show()
    def checkcourse3(self):
        self.backtonormal()
        self.pushButton_course3.setChecked(True)
        self.textBrowser_courseDescription_3.show()

    def translate(self):
        if self.language == 'german':
            self.language = 'english'
            self.pushButton_language.setText("English (en)")
            self.pushButton_home.setText(" Home")
            self.pushButton_calendar.setText(" Calendar")
            self.pushButton_files.setText(" Files")
            self.pushButton_mycourses.setText(" My Courses")
            self.pushButton_course1.setText(" Course 1")
            self.pushButton_course2.setText(" Course 2")
            self.pushButton_course3.setText(" Course 3")
        else:
            self.language = 'german'
            self.pushButton_language.setText("Deutsch (de)")
            self.pushButton_home.setText(" Startseite")
            self.pushButton_calendar.setText(" Kalender")
            self.pushButton_files.setText(" Dokumente")
            self.pushButton_mycourses.setText(" Meine Kurse")
            self.pushButton_course1.setText(" Kurs 1")
            self.pushButton_course2.setText(" Kurs 2")
            self.pushButton_course3.setText(" Kurs 3")

    def hidemenu(self):
        midwidth = self.frame_middle.width()
        midheight = self.frame_middle.height()
        midy = self.frame_middle.y()
        nameandpicheight = self.frame_nameandpic.height()
        if self.pushButton_menu.isChecked():
            self.frame_buttons.hide()
            self.frame_nameandpic.setGeometry(20, 90, 1101, nameandpicheight)
            self.frame_middle.setGeometry(20, midy, midwidth+200, midheight)
        else:
            self.frame_buttons.show()
            self.frame_nameandpic.setGeometry(220, 90, 901, nameandpicheight)
            self.frame_middle.setGeometry(220, midy, midwidth-200, midheight)

    def closefeedback(self):
        self.frame_feedback.hide()
        self.feedback_viewed = True;
        self.label_myellow.hide()  # Feedback warning for yellow feedback: Hide feedback warning when course is clicked
        self.label_morange.hide()  # Feedback warning for orange feedback: Hide feedback warning when course is clicked
        self.label_mred.hide()  # Feedback warning for red feedback: Hide feedback warning when course is clicked
        self.textBrowser_courseDescription.setGeometry(230, 180, 881, 441)

    def requestfeedback(self):
        # Hide and show relevant GUI parts
        self.MplWidget.show()
        self.frame_feedback.hide()
        self.textBrowser_courseDescription.hide()
        self.textBrowser_performance.show()
        self.textBrowser_timePlanning.show()
        self.textBrowser_backgroundKnowledge.show()
        self.textBrowser_engagement.show()
        self.frame_options.show()
        self.textBrowser_timeContingency.show()

        self.checkBox_performance.stateChanged.connect(self.checkperformance)
        self.checkBox_avgPerformance.stateChanged.connect(self.checkavgperformance)
        self.checkBox_timePlanning.stateChanged.connect(self.checktimeplanning)
        self.checkBox_avgTimePlanning.stateChanged.connect(self.checkavgtimeplanning)
        self.checkBox_backgroundKnowledge.stateChanged.connect(self.checkbackgroundknowledge)
        self.checkBox_avgBackgroundKnowledge.stateChanged.connect(self.checkavgbackgroundknowledge)
        self.checkBox_engagement.stateChanged.connect(self.checkengagement)
        self.checkBox_avgEngagement.stateChanged.connect(self.checkavgengagement)

        # Graph zeichnen
        self.drawGraph(self.showperformance, self.showavgperformance, self.showtimeplanning, self.showavgtimeplanning, self.showbackgroundknowledge, self.showavgbackgroundknowledge, self.showengagement, self.showavgengagement)

        # Feedback bestimmen und ausgeben
        pydate = str(self.currentdate.toPyDate())
        date = calendar.timegm(time.strptime(pydate, "%Y-%m-%d"))
        fullfeedback = Feedback().feedback_method(int(self.currentid), date, True)[0]
        #print(fullfeedback)
        Full = fullfeedback.split("---",3)
        TimeContingency = Full[1] + "\n" +Full[2]
        Rest = Full[3]
        self.textBrowser_timeContingency.setText(TimeContingency)
        Performance = Rest.split("---",2)[0] + "\n" + Rest.split("---",2)[1]
        Rest = Rest.split("---", 2)[2]
        self.textBrowser_performance.setText(Performance)
        TimePlanning = Rest.split("---",2)[0] + "\n" + Rest.split("---",2)[1]
        Rest = Rest.split("---", 2)[2]
        self.textBrowser_timePlanning.setText(TimePlanning)
        BackgroundKnowledge = Rest.split("---",2)[0] + "\n" + Rest.split("---",2)[1]
        Rest = Rest.split("---", 2)[2]
        self.textBrowser_backgroundKnowledge.setText(BackgroundKnowledge)
        Engagement = Rest.split("---",1)[0] + "\n" + Rest.split("---",1)[1]
        self.textBrowser_engagement.setText(Engagement)


        if Feedback.pcolour < 2:
            self.textBrowser_performance.setStyleSheet("border: 1px solid green")
        elif Feedback.pcolour == 2:
            self.textBrowser_performance.setStyleSheet("border: 1px solid yellow")
        elif Feedback.pcolour == 3:
            self.textBrowser_performance.setStyleSheet("border: 1px solid orange")
        elif Feedback.pcolour == 4:
            self.textBrowser_performance.setStyleSheet("border: 1px solid red")

        if Feedback.tpcolour < 2:
            self.textBrowser_timePlanning.setStyleSheet("border: 1px solid green")
        elif Feedback.tpcolour == 2:
            self.textBrowser_timePlanning.setStyleSheet("border: 1px solid yellow")
        elif Feedback.tpcolour == 3:
            self.textBrowser_timePlanning.setStyleSheet("border: 1px solid orange")
        elif Feedback.tpcolour == 4:
            self.textBrowser_timePlanning.setStyleSheet("border: 1px solid red")

        if Feedback.lobkcolour < 2:
            self.textBrowser_backgroundKnowledge.setStyleSheet("border: 1px solid green")
        elif Feedback.lobkcolour == 2:
            self.textBrowser_backgroundKnowledge.setStyleSheet("border: 1px solid yellow")
        elif Feedback.lobkcolour == 3:
            self.textBrowser_backgroundKnowledge.setStyleSheet("border: 1px solid orange")
        elif Feedback.lobkcolour == 4:
            self.textBrowser_backgroundKnowledge.setStyleSheet("border: 1px solid red")

        if Feedback.ecolour < 2:
            self.textBrowser_engagement.setStyleSheet("border: 1px solid green")
        elif Feedback.ecolour == 2:
            self.textBrowser_engagement.setStyleSheet("border: 1px solid yellow")
        elif Feedback.ecolour == 3:
            self.textBrowser_engagement.setStyleSheet("border: 1px solid orange")
        elif Feedback.ecolour == 4:
            self.textBrowser_engagement.setStyleSheet("border: 1px solid red")




    def checkperformance(self):
        self.showperformance = not self.showperformance
        self.drawGraph(self.showperformance, self.showavgperformance, self.showtimeplanning, self.showavgtimeplanning, self.showbackgroundknowledge, self.showavgbackgroundknowledge, self.showengagement, self.showavgengagement)

    def checkavgperformance(self):
        self.showavgperformance = not self.showavgperformance
        self.drawGraph(self.showperformance, self.showavgperformance, self.showtimeplanning, self.showavgtimeplanning, self.showbackgroundknowledge, self.showavgbackgroundknowledge, self.showengagement, self.showavgengagement)

    def checktimeplanning(self):
         self.showtimeplanning = not self.showtimeplanning
         self.drawGraph(self.showperformance, self.showavgperformance, self.showtimeplanning, self.showavgtimeplanning, self.showbackgroundknowledge, self.showavgbackgroundknowledge, self.showengagement, self.showavgengagement)

    def checkavgtimeplanning(self):
         self.showavgtimeplanning = not self.showavgtimeplanning
         self.drawGraph(self.showperformance, self.showavgperformance, self.showtimeplanning, self.showavgtimeplanning, self.showbackgroundknowledge, self.showavgbackgroundknowledge, self.showengagement, self.showavgengagement)

    def checkbackgroundknowledge(self):
        self.showbackgroundknowledge = not self.showbackgroundknowledge
        self.drawGraph(self.showperformance, self.showavgperformance, self.showtimeplanning, self.showavgtimeplanning, self.showbackgroundknowledge, self.showavgbackgroundknowledge, self.showengagement, self.showavgengagement)

    def checkavgbackgroundknowledge(self):
        self.showavgbackgroundknowledge = not self.showavgbackgroundknowledge
        self.drawGraph(self.showperformance, self.showavgperformance, self.showtimeplanning, self.showavgtimeplanning, self.showbackgroundknowledge, self.showavgbackgroundknowledge, self.showengagement, self.showavgengagement)

    def checkengagement(self):
        self.showengagement = not self.showengagement
        self.drawGraph(self.showperformance, self.showavgperformance, self.showtimeplanning, self.showavgtimeplanning, self.showbackgroundknowledge, self.showavgbackgroundknowledge, self.showengagement, self.showavgengagement)

    def checkavgengagement(self):
        self.showavgengagement = not self.showavgengagement
        self.drawGraph(self.showperformance, self.showavgperformance, self.showtimeplanning, self.showavgtimeplanning, self.showbackgroundknowledge, self.showavgbackgroundknowledge, self.showengagement, self.showavgengagement)

    def weekcalculation(self, date, weekend):
        for i in range(len(weekend)-1,-1,-1):
            if date < 1601424000:
                return 0
            if date == weekend[i]:
                return i
            if date > weekend[i]:
                return i+1

    def create_list(self, length):
        arra = np.array(list(range(0,length)))
        for i in range(len(arra)):
            arra[i] = 0
        return arra

    def prepareGraph(self, uid, date):
        weekend = [1601424000, 1602028800, 1602633600, 1603238400, 1603843200, 1604448000, 1605052800, 1605657600, 1606262400, 1607472000, 1607904000]
        userids = users = [124, 133, 143, 159, 160, 161, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185]
        week = self.weekcalculation(date, weekend)

        file = QtCore.QFile(":/tables/UserScores.csv")
        if file.open(QtCore.QIODevice.ReadOnly):
            f = io.BytesIO(file.readAll().data())
            df = pd.read_csv(f)

        if date in weekend:
            week = week+1

        #Berechen die Durchschnittswerte für P,TP,LOBK,E
        self.p_average = self.create_list(week)
        self.tp_average = self.create_list(week)
        self.lobk_average = self.create_list(week)
        self.e_average = self.create_list(week)

        for userid in userids:
            h_array = list(df.iloc[userid]["Performance"])[:week]
            h_array = np.array(list(map(int, h_array)))
            self.p_average += h_array

            h_array = list(df.iloc[userid]["TP"])[:week]
            h_array = np.array(list(map(int, h_array)))
            self.tp_average += h_array


            h_array = list(df.iloc[userid]["LOBK"])[:week]
            h_array = np.array(list(map(int, h_array)))
            self.lobk_average += h_array

            h_array = list(df.iloc[userid]["Engagement"])[:week]
            h_array = np.array(list(map(int, h_array)))
            self.e_average += h_array


        self.p_average = self.p_average/len(users)
        self.tp_average = self.tp_average/len(users)
        self.lobk_average = self.lobk_average/len(users)
        self.e_average = self.e_average/len(users)

        #print(p_average, tp_average,lobk_average,e_average)

        #Berechen die P,TP,LOBK,E Werte für den Nutzer
        self.performance = list(df.iloc[uid]["Performance"])[:week]
        self.performance = np.array(list(map(int, self.performance)))

        self.tp = list(df.iloc[uid]["TP"])[:week]
        self.tp = list(map(int, self.tp))

        self.lobk = list(df.iloc[uid]["LOBK"])[:week]
        if week == 11:
            self.lobk[10] = np.nan
            self.lobk_average[10] = np.nan
        self.lobk = list(map(float, self.lobk))
        self.lobk_average = list(map(float, self.lobk_average))

        self.engagement = list(df.iloc[uid]["Engagement"])[:week]
        self.engagement = list(map(int, self.engagement))

        dates = ['Wed, 30 Sep', 'Wed, 07 Oct', 'Wed, 14 Oct', 'Wed, 21 Oct', 'Wed, 28 Oct', 'Wed, 04 Nov', 'Wed, 11 Nov', 'Wed, 18 Nov', 'Wed, 25 Nov', 'Wed, 09 Dec', 'Mon, 14 Dec']
        # Creates DataFrame. weekend[0:week] , "TP":tp, "LOBK":lobk, "Engagement":engagement})

        self.graphtime = pd.DataFrame({"Time": dates[:week]})
        #df = df.set_index("Time")


    def drawGraph(self, pf_b, pfa_b, tp_b, tpa_b, lobk_b, lobka_b, e_b, ea_b):
        #Falls nichts angezeigt werden soll => return
        if not (pf_b | tp_b | lobk_b | e_b | pfa_b | tpa_b | lobka_b | ea_b):
            return

        graphdata = self.graphtime
        # Was soll im Graphen gezeigt werden?
        if pf_b:
            graphdata["Performance"] = self.performance
        if pfa_b:
            graphdata["Performance_A"] = self.p_average
        if tp_b:
            graphdata["TP"] = self.tp
        if tpa_b:
            graphdata["TP_A"] = self.tp_average
        if lobk_b:
            graphdata["LOBK"] = self.lobk
        if lobka_b:
            graphdata["LOBK_A"] = self.lobk_average
        if e_b:
            graphdata["Engagement"] = self.engagement
        if ea_b:
            graphdata["Engagement_A"] = self.e_average


        #Figsize --- Größe des Plots ändern (width, height)
        #graph = df.plot(xticks = df.index, yticks = [0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0], figsize = (10,6))
        #graph = graph.set_xticklabels(df.Time, rotation = 90)

        matplotlib.rc('xtick', labelsize=6)
        matplotlib.rc('ytick', labelsize=6)
        matplotlib.rc('legend', fontsize=6)
        self.MplWidget.canvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.MplWidget.setFocus()
        self.MplWidget.canvas.axes.clear()

        graphdata.plot(ax=self.MplWidget.canvas.axes, xticks=graphdata.index, yticks=[0.0,1.0,2.0,3.0,4.0], xlabel='date', ylabel='score', title='Feedback score development')
        self.MplWidget.canvas.axes.set_xticklabels(graphdata.Time, rotation = 45, ha='right',rotation_mode='anchor')
        self.MplWidget.canvas.figure.tight_layout()
        self.MplWidget.canvas.updateGeometry()
        self.MplWidget.adjustSize()
        self.MplWidget.canvas.draw()

        graphdata.drop(graphdata.columns.difference(['Time']), 1, inplace=True)
        return




def main():
    app = QApplication([])
    widget = Login()
    widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
