# -*- coding: utf-8 -*-
import pandas as pd
import calendar, time;

try:
    from PySide import QtWidgets
except:
    from PyQt5 import QtWidgets


class Lackofbackgroundknowledge:
    def __init__(self):
        lkasdjflaskdjf = 45

    suggorder_weeks = [[606, 608, 609, 610, 611], [613, 614, 615, 616], [618, 619, 620, 621, 623], [634, 635, 636, 637, 638], [644, 641, 642, 643, 640], [642, 646, 647, 649], [663, 664, 666, 667], [668, 669, 671, 672, 673], [678, 679, 681, 680], [688, 689, 690, 697, 698]]


    def weekcalculation(self, date, weekend):
        for i in range(len(weekend)-1,-1,-1):
            if date < 1601424000:
                return 0
            if date == weekend[i]:
                return i
            if date > weekend[i]:
                return i+1

    #Material angesehen? Ja/Nein  Nein -> Welches Material nicht
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


    #Wurde die suggested order eingehalten?
    def sugg_ord(self, uid, date, logs_df, suggorder_weeks, weekend):
        #finde heraus zu welcher Woche das date gehört -- es sollte vorher gefiltert werden das nur Dates aus
        #dem Kurszeitraum erlaubt sind bzw. dates die für suggorder erlaubt sind, da nur bis woche 10 relevant
        week = self.weekcalculation(date, weekend) #week ist der Index nicht die Woche

        dates = []
        user = ("anonfirstname"+str(uid-112)+" anonlastname"+str(uid-112))
        #lies die Zeitpunkte an denen die Materialien das erste mal angeklickt wurde in "dates" ein
        for idw in suggorder_weeks[week]:
            firstocc = logs_df[(logs_df["User full name"] == user) & logs_df["Description"].str.contains(str(idw))].iloc[-1]
            firstocctime = firstocc["Time"]
            times = calendar.timegm(time.strptime(firstocctime, "%d/%m/%y, %H:%M"))
            dates += [times]
        #sind die Dates in der Liste aufsteigend? -> ja => dann wurde die suggested order eingehalten
        for i in range(len(dates)):
            if i == len(dates)-1: break
            a = dates[i]
            n = dates[i+1]
            if a > n:
                return(False)

        return(True)


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


    #LOBK Level
    def lobk_level(self, uid, date, logs_df, suggorder_weeks, weekend):
        quizweeks = [1,2,7,8,9,10]
        assignmentweeks = [3,5,10,11]
        lobk_level = 999

        scores_df = pd.read_csv("./CourseData/UserScores.csv")
        week = self.weekcalculation(date, weekend)
        #aktuelles Performance Level
        #Performance Level
        temp = scores_df.iloc[uid]["Performance"]
        temp = list(temp)
        performance_level = int(temp[week])


        #LOBK Score der letzten Woche
        if week > 0:
            temp = scores_df.iloc[uid]["LOBK"]
            temp = list(temp)
            lobk_level_LW = int(temp[week-1])

        #MaterilViewedValue Bool oder (Bool, Liste)
        mvv = self.material_viewed(uid, date, logs_df, suggorder_weeks, weekend)
        #SuggestedOrderValue Bool
        if mvv[0]:
            sov = self.sugg_ord(uid, date, logs_df, suggorder_weeks, weekend)

        #siehe Feedback Score Diagramm zu LOBK
        #Performance >=2
        if (performance_level >= 2):
            #alle Materialien angesehen?
            if mvv[0] == False:
                lobk_level = 4
            #suggested order eingehalten?
            elif sov: #WAS PASSIERT BEI EINER WIEDERHOLUNG?? # if lobk_level_LW == 2 & performancelastweek >= 2...
                lobk_level = "2a"
            else:
                lobk_level = 3
        #Performance < 2
        else:
            #alle Materialien angesehen?
            if mvv[0] == False:
                lobk_level = "2b"
            elif sov:
                lobk_level = 0
            else:
                lobk_level = 1

        x = lobk_level
        if lobk_level == "2a":
            x = 21
        elif lobk_level =="2b":
            x = 22

        #Speicher neue Performance in der Datei
        if (lobk_level == "2b") | (lobk_level == "2a"):
            self.writeV(uid, week, 2, "LOBK")
            lobk_level = 2

            #Sonderfall 2a 2b und nicht Woche 1
            if week > 0:
                if lobk_level < lobk_level_LW:
                    return (x, "improved", mvv[1])
                elif lobk_level == lobk_level_LW:
                    return (x, "unchanged", mvv[1])
                elif lobk_level > lobk_level_LW:
                    return (x, "worsened", mvv[1])
        else:
            self.writeV(uid, week, lobk_level, "LOBK")


        if week > 0:
            if lobk_level < lobk_level_LW:
                return (lobk_level, "improved", mvv[1])
            elif lobk_level == lobk_level_LW:
                return (lobk_level, "unchanged", mvv[1])
            elif lobk_level > lobk_level_LW:
                return (lobk_level, "worsened", mvv[1])

        else:
            return (x, "WeekOne", mvv[1])
