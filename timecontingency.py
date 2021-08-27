# -*- coding: utf-8 -*-
import pandas as pd
import calendar, time;

try:
    from PySide import QtWidgets
except:
    from PyQt5 import QtWidgets


class Timecontingency:
    def __init__(self):
        lksjdflkjasdlfkj = 0

    suggorder_weeks = [[606, 608, 609, 610, 611], [613, 614, 615, 616], [618, 619, 620, 621, 623], [634, 635, 636, 637, 638], [644, 641, 642, 643, 640], [642, 646, 647, 649], [663, 664, 666, 667], [668, 669, 671, 672, 673], [678, 679, 681, 680], [688, 689, 690, 697, 698]]

    def weekcalculation(self, date, weekend):
        for i in range(len(weekend)-1,-1,-1):
            if date < 1601424000:
                return 0
            if date == weekend[i]:
                return i
            if date > weekend[i]:
                return i+1

    def material_m(self, materialids):
        if len(materialids) == 0:
            return "None"
        df = pd.read_csv("./CourseData/cleanrow_course_modules.csv")
        material = []
        for mid in materialids:
            temp = df[df["id"] == mid]
            x = temp.iloc[0]["idnumber"]
            material += [x]
        return material

    def material_viewed(self, uid, date, logs_df, suggorder_weeks, weekend):
        #finde heraus zu welcher Woche das date gehört -- es sollte vorher gefiltert werden das nur Dates aus
        #dem Kurszeitraum erlaubt sind bzw. dates die hier erlaubt sind, da wochen nur bis 10 relevant
        week = self.weekcalculation(date, weekend)

        weeks = [[606, 608, 609, 610, 611], [613, 614, 615, 616], [618, 619, 620, 621, 623], [634, 635, 636, 637, 638], [644, 641, 642, 643, 640], [642, 646, 647, 649], [663, 664, 666, 667], [668, 669, 671, 672, 673], [678, 679, 681, 680], [688, 689, 690, 697, 698]]

        user = "anonfirstname"+str(uid-112)+" anonlastname"+str(uid-112)
        #enthält die ids aller nicht bearbeiteten Materialien
        notviewed = []
        viewedc = 0

        for i in range(len(weeks[week])):
            user = ("anonfirstname"+str(uid-112)+" anonlastname"+str(uid-112))
            temp = (logs_df["User full name"] == user)  & logs_df["Description"].str.contains(str(weeks[week][i]))
            viewed = temp.any()

            #liest Zeitpunkt an dem das Material das erste mal angeklickt wurde ein
            if viewed:
                firstocc = logs_df[(logs_df["User full name"] == user) & logs_df["Description"].str.contains(str(weeks[week][i]))].iloc[-1]
                firstocctime = firstocc["Time"]
                times = calendar.timegm(time.strptime(firstocctime, "%d/%m/%y, %H:%M"))
            else:
                notviewed += [suggorder_weeks[week][i]]
                continue

            if viewed & (date >= times):
                viewedc += 1
            else:
                notviewed += [suggorder_weeks[week][i]]

        if viewedc == len(weeks[week]):
            return(True, [])
        else:
            return(False, notviewed)


    def quiz_started(self, uid, date, quizattempts_df, quizweeks, quizids, weekend):
        #finde heraus zu welcher Woche das date gehört -- es sollte vorher gefiltert werden das nur Dates aus
        #dem Kurszeitraum erlaubt sind
        week = self.weekcalculation(date, weekend)

        #überprüfe ob es für die Woche ein Quiz gibt
        #falls es ein quiz gibt gib die quiz id aus
        if week+1 in quizweeks:
            weekindex = quizweeks.index(week+1)
            quizid = quizids[weekindex]
        else:
            print("Es wurde kein Quiz für Woche ", week+1, "gefunden.")
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

    def quiz_finished(self, uid, date, quizattempts_df, quizweeks, quizids, weekend):
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


    def assignmentSub(self, uid, date, assignSub_df, assignmentids , assignmentweeks, weekend):
        week = self.weekcalculation(date, weekend)

        #AssignmentID herausfinden
        weekindex = assignmentweeks.index(week+1)
        assignmentId = assignmentids[weekindex]

        temp = assignSub_df[(assignSub_df["assignment"] == assignmentId)  & (assignSub_df["userid"] == uid)]
        x = temp.empty
        if x:
            return False
        temp = temp.iloc[0]

        status = temp["status"]
        timeCreated = temp["timecreated"]

        #überprüfen ob abgegeben wurde
        if ((status == "submitted") | (status == "draft")) & (date > timeCreated):
            return True
        elif (status == "new") | timeCreated > date:
            return False


    #TimeContingency
    def timeContingency(self, uid, date, logs_df, quizattempts_df, assignSub_df, assignmentids , assignmentweeks, quizweeks, quizids, suggorder_weeks, weekend):
        week = self.weekcalculation(date, weekend)

        if week == 0:
            return "Nothing"

        #Lies die Werte der letzten Woche ein
        #[UID,Performance, TimePlanning, LOBK, Engagement]
        lastWeekScores_df = pd.read_csv("./CourseData/UserScores.csv")

        temp = lastWeekScores_df.iloc[uid]["LOBK"]
        lobkllw = list(temp)
        lobkllw = int(lobkllw[week-1])

        temp = lastWeekScores_df.iloc[uid]["TP"]
        tpllw = list(temp)
        tpllw = int(tpllw[week-1])

        rs = "\n\n---Reminders---\n"


        #LOBK >= 2
        if (lobkllw >= 2) & (week < 10):
            #MaterialViewed
            mv = self.material_viewed(uid, date, logs_df, suggorder_weeks, weekend)
            if mv[0]:
                lkjasdf = 0
            elif (mv[0] == False) & ((date + 172800) >= weekend[week]):
                rs += "The week ends in less than 2 days, please work through the materials: "
                rs += (" ".join(self.material_m(mv[1])))

            elif (mv[0] == False) & ((date + 345600) >= weekend[week]):
                rs += "The week ends in less than 4 days, please work through the materials: "
                rs += (" ".join(self.material_m(mv[1])))

        #TP >= 2
        if tpllw >= 2:
            if week+1 in quizweeks:
                #QuizStarted
                qs = self.quiz_started(uid, date, quizattempts_df, quizweeks, quizids, weekend)
                #QuizFinished
                qf = self.quiz_finished(uid, date, quizattempts_df, quizweeks, quizids, weekend)
                if qs & qf:
                    klasjdf = 0
                # Quiz nicht angefangen und nur noch 2 Tage Zeit
                elif (qs == False) & ((date + 172800) >= weekend[week]):
                    rs += "\nThe week ends in less than 2 days, please work on the quiz."
                # Quiz nicht angefangen und nur noch 4 Tage Zeit
                elif (qs == False) & ((date + 345600) >= weekend[week]):
                    rs += "\nThe week ends in less than 4 days, please work on the quiz."
                # Quiz nicht beendet und nur noch 2 Tage Zeit
                elif (qf == False) & ((date + 172800) >= weekend[week]):
                    rs += "\nThe week ends in less than 2 days, please finish the quiz."
                # Quiz nicht beendet und nur noch 4 Tage Zeit
                elif (qf == False) & ((date + 172800) >= weekend[week]):
                    rs += "\nThe week ends in less than 4 days, please finish the quiz."


            if week+1 in assignmentweeks:
                #AssignmentSubmitted
                asub = self.assignmentSub(uid, date, assignSub_df, assignmentids , assignmentweeks, weekend)
                if asub:
                    ölasdf = 0
                # Assignment nicht angefangen und nur noch 2 Tage Zeit
                elif (asub == False) & ((date + 172800) >= weekend[week]):
                    rs += "\nThe week ends in less than 2 days, please work on the assignment."
                # Assignment nicht angefangen und nur noch 4 Tage Zeit
                elif (asub == False) & ((date + 345600) >= weekend[week]):
                    rs += "\nThe week ends in less than 4 days, please work on the assignment."

        if (rs == "\n\n---Reminders---\n"):
            rs = "Nothing"
            return rs

        return rs
