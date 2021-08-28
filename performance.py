# -*- coding: utf-8 -*-

try:
    from PySide import QtWidgets
except:
    from PyQt5 import QtWidgets

import pandas as pd

class Performance:
    def __init__(self):
        lkasjdflkasjdf = 45

    #Woche anhand des Datum berechnen
    def weekcalculation(self,date, weekend):
        for i in range(len(weekend)-1,-1,-1):
            if date < 1601424000:
                return 0
            if date == weekend[i]:
                return i
            if date > weekend[i]:
                return i+1

    #Quiz Note

    def grade_q(self, uid, date, quizg_df, quiza_df, quizweeks, quizids, weekend):
        week = self.weekcalculation(date, weekend)
        #Quiz Id heraufinden
        weekindex = quizweeks.index(week+1)
        quizid = quizids[weekindex]


        temp = quizg_df[(quizg_df["quiz"] == quizid) & (quizg_df["userid"] == uid)]
        x = temp.empty

        quizNotFinished = False
        quizNotFinishedIT = False
        if not x:
            temp2 = quiza_df[(quiza_df["quiz"] == quizid) & (quiza_df["userid"] == uid)].iloc[0]
            quizNotFinished = (temp2["timefinish"] == 0)

            #quiz finished in time
            quizNotFinishedIT = (temp2["timefinish"] > weekend[week])

        #Falls das Quiz nicht gemacht oder nicht rechtzeitig beendet wurde => Note = 0
        if x | quizNotFinished | quizNotFinishedIT :
            return 0

        usergrade = temp.iloc[0]["grade"]
        return usergrade


    #Quiz Notendurchschnitt

    def grade_qa(self, date, quizg_df, quiza_df, quizweeks, quizids, weekend):
        week = self.weekcalculation(date, weekend)
        #Quiz Id heraufinden
        weekindex = quizweeks.index(week+1)
        quizid = quizids[weekindex]

        ids = quiza_df[(date > quiza_df["timefinish"]) & (quiza_df["state"] == "finished") & (quiza_df["quiz"] == quizid)]
        uids = ids.userid.tolist()
        #Durchschnitt berechnen
        grades = []
        for uid in uids:
            temp = quizg_df[(quizg_df["quiz"] == quizid) & (quizg_df["userid"] == uid)]
            #Manche User haben keine Note obwohl sie Das Quiz beendet haben
            x = temp.empty
            if x:
                continue
            grades += [temp.iloc[0]["grade"]]

        if len(grades) == 0:
            average = 0
            return average
        average = sum(grades)/len(grades)

        return average


    #Assignment Note

    def grade_a(self, uid, date, assignmentg_df, assignmentweeks, assignmentids, weekend):
        week = self.weekcalculation(date, weekend)
        #Assignment Id heraufinden
        weekindex = assignmentweeks.index(week+1)
        assignmentid = assignmentids[weekindex]

        temp = assignmentg_df[(assignmentg_df["assignment"] == assignmentid)  & (assignmentg_df["userid"] == uid)]
        if temp.empty:
            return 0

        usergrade = temp.iloc[0]["grade"]

        #Dieser If-Zweig wird nicht erreicht, letzte abgabe irrelevant da unbenotet
        if (assignmentid == 31) & (usergrade == -1):
            return("Assignment" ,31, "100 Punkte", "Usergrade", usergrade)

        #Fall das Assignment nicht abgeben wurde, gib False aus
        if (usergrade == -1) | (pd.isnull(usergrade)):
            return 0
        return usergrade


    #Assignment Notendurchschnitt

    def grade_aa(self, date, assignmentg_df, assignmentweeks, assignmentids, weekend):
        week = self.weekcalculation(date, weekend)

        #Assignment Id heraufinden
        weekindex = assignmentweeks.index(week+1)
        assignmentid = assignmentids[weekindex]

        #Durchschnitt berechnen
        temp = assignmentg_df[(assignmentg_df["assignment"] == assignmentid)]
        grades = temp.grade.tolist()

        #entferne -1 und nan
        cgrades = []
        for grade in grades:
            if (grade == -1) | (pd.isnull(grade)):
                continue
            else:
                cgrades += [grade]

        average = sum(cgrades)/len(cgrades)

        return average


    #Level speichern

    def writeV(self, uid, week, value, cat):
        df = pd.read_csv("./CourseData/UserScores.csv")

        #Ersetze den Wert
        temp = df.iloc[uid][cat]
        temp = list(temp)
        temp[week] = str(value)
        temp = "".join(temp)

        df.loc[uid, cat] = temp
        df.to_csv("./CourseData/UserScores.csv", index = False)



    #Performance Level berechnen

    def performance_level(self, uid, date, assignmentg_df, quizg_df, quiza_df, assignmentweeks, assignmentids, quizweeks, quizids, weekend):
        performance = 999
        #Bestimme die Beste zu erreichende Note für die Quiz
        quizmaxg_df = pd.read_csv("./CourseData/cleanrow_quiz.csv")
        quizmaxg = quizmaxg_df.grade.tolist()
        #Entferne Klausur Quizgrade
        quizmaxg.pop(-1)

        week = self.weekcalculation(date, weekend)

        #Lies die Werte der letzten Woche ein
        #[UID,Performance, TP, LOBK, Engagement]
        lastWeekScores_df = pd.read_csv("./CourseData/UserScores.csv")


        #PerformanceLevelLastWeek
        temp = lastWeekScores_df.iloc[uid]["Performance"]
        temp = list(temp)
        pllw = 999
        if week > 0:
            pllw = int(temp[week-1])

        #Für Woche 3,5 gibt es kein Quiz/Assignment, daher der Performance Score der vorwoche
        assignmentweeks = [4,6,11,12]
        if (week+1 == 3) | (week+1 == 5):
            self.writeV(uid, week, pllw, "Performance")
            return (pllw, "unchangedNoQA")







#----------------------------------QuizPerformance---------------------------------------------------#
        performanceq = 999
        #Prüfe ob es für die Woche ein Quiz gibt -> falls ja berechne Score
        if week+1 in quizweeks:
            #Quiz Note
            quizg = self.grade_q(uid, date, quizg_df, quiza_df, quizweeks, quizids, weekend)
            #Quiz Notendurchschnitt
            quizga = self.grade_qa(date, quizg_df, quiza_df, quizweeks, quizids, weekend)

            #weise maxG die beste Note für Woche x zu
            weekindex = quizweeks.index(week+1)
            maxG = quizmaxg[weekindex]

            #intervall Level 0
            intervall = pd.arrays.IntervalArray([pd.Interval(maxG-(maxG-quizga)/2, maxG, closed="both")])
            #print(intervall)
            if intervall.contains(quizg):
                performanceq = 0

            #intervall Level 1
            intervall = pd.arrays.IntervalArray([pd.Interval(quizga, maxG-(maxG-quizga)/2, closed="left")])
            #print(intervall)
            if intervall.contains(quizg):
                performanceq = 1

            #intervall Level 2
            intervall = pd.arrays.IntervalArray([pd.Interval(quizga/2, quizga, closed="left")])
            #print(intervall)
            if intervall.contains(quizg):
                performanceq = 2

            #intervall Level 3
            intervall = pd.arrays.IntervalArray([pd.Interval(0, quizga/2, closed="left")])
            #print(intervall)
            if intervall.contains(quizg):
                performanceq = 3

            #Die Woche muss >= 1, da wir sonst keine Daten aus vergangenen Wochen haben
            if (week+1 >= 1) & (performanceq > 2):
                #Level 4
                if (pllw == 3) | (pllw == 4):
                    performanceq = 4



    #----------------------------------AssignmentPerformance---------------------------------------------------#
        performancea = 999

        #Bestimme die Beste zu erreichende Note für die Assignments
        assignmentsmaxg_df = pd.read_csv("./CourseData/cleanrow_assign.csv")
        assignmentmaxg = assignmentsmaxg_df.grade.tolist()
        #Entferne Wert für Assignment 29 - da es hier keine Note gibt -> irrelevant für Performance
        assignmentmaxg.pop(2)


        #die Performance soll nur für die ersten 3 Assignments berechnet werden
        assignmentid = 999
        if (week+1 in assignmentweeks):
            #Assignment Id heraufinden
            weekindex = assignmentweeks.index(week+1)
            assignmentid = assignmentids[weekindex]
        aperf = True
        if assignmentid == 31:
            aperf = False

        #Prüfe ob es für die Woche ein Assignment gibt -> falls ja berechne Score
        if (week+1 in assignmentweeks) & aperf:
            #Assignment Note
            assignmentg = self.grade_a(uid, date, assignmentg_df, assignmentweeks, assignmentids, weekend)
            #print("User:", uid, "Woche:",week+1, "Note Assignment:", assignmentg)
            #Assignment Notendurchschnitt
            assignmentga = self.grade_aa(date, assignmentg_df, assignmentweeks, assignmentids, weekend)

            #weise maxG die beste Note für Woche x zu
            weekindex = assignmentweeks.index(week+1)
            maxAG = assignmentmaxg[weekindex]

            #intervall Level 0
            intervall = pd.arrays.IntervalArray([pd.Interval(maxAG-(maxAG-assignmentga)/2, maxAG, closed="both")])
            #print(intervall)
            if intervall.contains(assignmentg):
                performancea = 0

            #intervall Level 1
            intervall = pd.arrays.IntervalArray([pd.Interval(assignmentga, maxAG-(maxAG-assignmentga)/2, closed="left")])
            #print(intervall)
            if intervall.contains(assignmentg):
                performancea = 1

            #intervall Level 2
            intervall = pd.arrays.IntervalArray([pd.Interval(assignmentga/2, assignmentga, closed="left")])
            #print(intervall)
            if intervall.contains(assignmentg):
                performancea = 2

            #intervall Level 3
            intervall = pd.arrays.IntervalArray([pd.Interval(0, assignmentga/2, closed="left")])
            #print(intervall)
            if intervall.contains(assignmentg):
                performancea = 3

            #Die Woche muss > 1, da wir sonst keine Daten aus vergangenen Wochen haben
            if (week+1 > 1) & (performancea > 2):
                #Level 4
                if (pllw == 3) | (pllw == 4):
                    performancea = 4



        if week+1 in quizweeks:
            performance = round(performanceq)

        if week+1 in assignmentweeks:
            performance = round(performancea)

        if (week+1 in quizweeks) & (week+1 in assignmentweeks):
            performance = round((performanceq + performancea*2)/3)

        performance = 4
        #Speicher neue Performance in der Datei
        self.writeV(uid, week, performance, "Performance")

        #lastWeekScores_df.loc[uid, "Performance"] = performance
        #lastWeekScores_df.to_csv("UserScores.csv")
        if week > 0:
            if performance < pllw:
                return (performance, "improved")
            elif performance == pllw:
                return (performance, "unchanged")
            elif performance > pllw:
                return (performance, "worsened")

        else:
            return (performance, "WeekOne")




