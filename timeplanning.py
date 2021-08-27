# -*- coding: utf-8 -*-
import pandas as pd

try:
    from PySide import QtWidgets
except:
    from PyQt5 import QtWidgets


class TimePlanning:
    def __init__(self):
        sldkfjasldkfj = 0

    def weekcalculation(self, date, weekend):
        for i in range(len(weekend)-1,-1,-1):
            if date < 1601424000:
                return 0
            if date == weekend[i]:
                return i
            if date > weekend[i]:
                return i+1


    #Wurde das Quiz in der richtigen Woche begonnen?

    def quiz_start(self, uid, date, quizattempts_df, weekend, quizids, quizweeks):
    #finde heraus zu welcher Woche das date gehört -- es sollte vorher gefiltert werden das nur Dates aus
    #dem Kurszeitraum erlaubt sind
        week = self.weekcalculation(date, weekend)

    #überprüfe ob es für die Woche ein Quiz gibt
    #falls es ein quiz gibt gib die quiz id aus
        if week+1 in quizweeks:
            weekindex = quizweeks.index(week+1)
            quizid = quizids[weekindex]
        else:
            #print("Es wurde kein Quiz für Woche ", week+1, "gefunden.")
            return
    #Zeitpunkt einlesen wann das Quiz gestartet wurde, falls es keine Zeitpunkte gibt => False
        temp = quizattempts_df[(quizattempts_df["userid"] == uid)  & (quizattempts_df["quiz"] == quizid)]
        if temp.empty:
            return False
        temp = quizattempts_df[(quizattempts_df["userid"] == uid)  & (quizattempts_df["quiz"] == quizid)].iloc[0]


    #in der richtigen woche quiz begonnen?
        timestart = temp["timestart"]
        if date >= timestart:
            return True
        else:
            return False


    #Wurde das Quiz in der richtigen Woche beendet?

    def quiz_finished(self, uid, date, quizattempts_df, weekend, quizweeks, quizids):
    #finde heraus zu welcher Woche das date gehört -- es sollte vorher gefiltert werden das nur Dates aus
    #dem Kurszeitraum erlaubt sind
        week = self.weekcalculation(date, weekend)

    #überprüfe ob es für die Woche ein Quiz gibt
    #falls es ein quiz gibt gib die quiz id aus
        if week+1 in quizweeks:
            weekindex = quizweeks.index(week+1)
            quizid = quizids[weekindex]

    #Zeitpunkte einlesen wann das Quiz beendet wurde, falls es keine Zeitpunkte gibt => False
        temp = quizattempts_df[(quizattempts_df["userid"] == uid)  & (quizattempts_df["quiz"] == quizid)]
        if temp.empty:
            return False
        temp = quizattempts_df[(quizattempts_df["userid"] == uid)  & (quizattempts_df["quiz"] == quizid)].iloc[0]


    #checke ob Quiz beendet wurde
        if temp["state"] == "inprogress":
            return False

    #überprüfe ob das Quiz in der richtigen Woche beendet wurde
        timefinished = temp["timefinish"]
        if date >= timefinished:
            return True
        else:
            return False


    #Berechnet ob der User das Quiz später oder früher als der Durchschnitt angefangen hat

    def qtimeuntild(self, uid, date, quizattempts_df, weekend, quizweeks, quizids):
    #Diese Feature wird nur für vergangene Wochen berechnet, testen ob Woche vorbei ist
    #und nur ausgeführt falls der user das quiz gemacht hat
        if date in weekend:
            None
        else:
            #print("Time until deadline wird nicht für eine laufende Wochen berechnet!")
            return

    #finde heraus zu welcher Woche das date gehört -- es sollte vorher gefiltert werden das nur Dates aus
    #dem Kurszeitraum erlaubt sind
        week = self.weekcalculation(date, weekend)

        weekindex = quizweeks.index(week+1)
        quizid = quizids[weekindex]
    #Berechne die Durchscnittliche Startzeit
        temp = quizattempts_df[(quizattempts_df["quiz"] == quizid)  & (quizattempts_df["state"] == "finished") & (date >= quizattempts_df["timefinish"])]
        timestart = temp.timestart.tolist()
        averagestarttime = sum(timestart)/ len(timestart)

        temp = quizattempts_df[(quizattempts_df["quiz"] == quizid)  & (quizattempts_df["state"] == "finished") & (date >= quizattempts_df["timefinish"]) & (quizattempts_df["userid"] == uid)]
        usertimestart = temp.iloc[0]["timestart"]
        if usertimestart > averagestarttime:
            return True
        else:
            return False


    #Berechnet ob der User das Assignment früher oder später als der Durchschnitt angefangen hat

    def atimeuntild(self, uid, date, a_df, weekend, assignmentweeks, assignmentids):
    #Diese Feature wird nur für vergangene Wochen berechnet, testen ob Woche vorbei ist
    #und nur ausgeführt falls der user das Assignment gemacht hat
        if date in weekend:
            None
        else:
            #print("Time until deadline wird nicht für eine laufende Wochen berechnet!")
            return

    #finde heraus zu welcher Woche das date gehört -- es sollte vorher gefiltert werden das nur Dates aus
    #dem Kurszeitraum erlaubt sind
        week = 0
        for i in range(len(weekend)-1,-1,-1):
            if date == weekend[i]:
                week = i
                break
            elif date > weekend[i]:
                week = i+1
                break

        weekindex = assignmentweeks.index(week+1)
        assignmentid = assignmentids[weekindex]

    #Berechne die Durchschnittliche Startzeit
        temp = a_df[(a_df["assignment"] == assignmentid)  & (a_df["status"] == "submitted")]
        timestart = temp.timecreated.tolist()
        averagestarttime = sum(timestart)/ len(timestart)

        temp = a_df[(a_df["assignment"] == assignmentid)  & (a_df["status"] == "submitted") & (a_df["userid"] == uid)]
        x = temp.empty
        if x:
            return "notSubmitted"

        temp = a_df[(a_df["assignment"] == assignmentid)  & (a_df["status"] == "submitted") & (a_df["userid"] == uid)].iloc[0]

        usertimestart = temp["timecreated"]
        if usertimestart > averagestarttime:
            return True
        else:
            return False


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


    #TimePlanning Level

    def tp_level(self, uid, date, a_df, quizattempts_df, weekend, assignmentweeks, assignmentids, quizweeks, quizids):
    #finde heraus zu welcher Woche das date gehört -- es sollte vorher gefiltert werden das nur Dates aus
    #dem Kurszeitraum erlaubt sind
        week = self.weekcalculation(date, weekend)

        scores_df = pd.read_csv("./CourseData/UserScores.csv")

    #PerformanceLevel
        temp = scores_df.iloc[uid]["Performance"]
        temp = list(temp)
        performance_level = int(temp[week])

    #TimePlanning Score der letzten Woche
        tp_level_LW = 999
        if week > 0:
            tp_level_LW = scores_df.iloc[uid]["TP"]
            tp_level_LW = list(temp)
            tp_level_LW = int(tp_level_LW[week-1])


        tp_level = 999
        tp_levelq = 999
        tp_levela = 999


    #Wochen in denen es kein Quiz und kein Assignment gibt => gib das Level der letzten Woche aus + Hinweis
        if (week+1 == 4) | (week+1 ==  6) | (week+1 ==  11):
            self.writeV(uid, week, tp_level_LW, "TP")
            return (tp_level_LW,"unchangedNoQA")


    #überprüfe ob es ein Quiz/Assignment für diese week gibt
        qweek = week+1 in quizweeks
        aweek = week+1 in assignmentweeks
    #Es gibt ein Quiz
        if qweek:
            quiz_started = self.quiz_start(uid, date, quizattempts_df, weekend, quizids, quizweeks)
            if quiz_started:
                quizf = self.quiz_finished(uid, date, quizattempts_df, weekend, quizweeks, quizids)
            #Quiz beendet
                if quizf:
                    if performance_level >= 2:
                        qtime_ga = self.qtimeuntild(uid, date, quizattempts_df, weekend, quizweeks, quizids)
                    #Quiz später als der Kursdurchschnitt angefangen
                        if qtime_ga:
                            tp_levelq = 2
                        else:
                            tp_levelq = 0
                #falls das Performance Level < 2 ist
                    else:
                        tp_levelq = 0
            #Quiz nicht rechtzeitig beendet
                else:
                    tp_levelq = 3
        #quiz nicht angefangen
            else:
                tp_levelq = 3
                if (tp_level_LW == tp_levelq) | (tp_level_LW == 4):
                        tp_levelq = 4

    #Es gibt ein Assigment --- siehe Feedback  Score Tp


        if aweek:
            atime_ga = self.atimeuntild(uid, date, a_df, weekend, assignmentweeks, assignmentids)
            if (performance_level >= 2) & (str(atime_ga) != "notSubmitted"):
            #Assignment später als der Kursdurchschnitt angefangen

                if atime_ga:
                    tp_levela = 2
                else:
                    tp_levela = 0

            elif (performance_level >= 2) & (atime_ga != "notSubmitted"):
                tp_levela = 3
            elif (performance_level >= 2) & (atime_ga != "notSubmitted") & (tp_level_LW == 4):
                tp_levela = 4
        #Performance_Level < 2
            else:
                tp_levela = 0

    #haben wir eine Woche mit Quiz & Assignment...
        if aweek:
            tp_level = round (tp_levela)

        if qweek:
            tp_level = round (tp_levelq)

        if aweek & qweek:
            tp_level = round ((tp_levelq + tp_levela*2)/3)

    #Speicher neue Performance in der Datei
        self.writeV(uid, week, tp_level, "TP")

    #lastWeekScores_df.loc[uid, "Performance"] = performance
    #lastWeekScores_df.to_csv("UserScores.csv")

        if week > 0:
            if tp_level < tp_level_LW:
                return (tp_level, "improved")
            elif tp_level == tp_level_LW:
                return (tp_level, "unchanged")
            elif tp_level > tp_level_LW:
                return (tp_level, "worsened")

        else:
            return (tp_level, "WeekOne")
