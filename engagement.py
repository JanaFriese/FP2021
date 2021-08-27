# -*- coding: utf-8 -*-
import pandas as pd
import calendar, time;

try:
    from PySide import QtWidgets
except:
    from PyQt5 import QtWidgets


class Engagement:
    def __init__(self):
        xiuqwer = 0


    def weekcalculation(self, date, weekend):
        for i in range(len(weekend)-1,-1,-1):
            if date < 1601424000:
                return 0
            if date == weekend[i]:
                return i
            if date > weekend[i]:
                return i+1


    #Quiz done until date
    def quizdone(self, uid, date, df, quiztimesbeginn):
        #anzahl bis date veröffentlichter quiz
        qp = sum(i <= date for i in quiztimesbeginn)
        qd = 0 #anzahl absolvierter quiz


        for quizid in range(37,43):
            dataf = df.loc[(df["userid"] == uid) & (df["quiz"] == quizid)]
            #falls user das quiz nicht gemacht hat
            try:
                timefinished = dataf["timefinish"].values[0]
            except:
                continue

            if (date >= timefinished) & (timefinished != 0):
                qd += 1
        return((qd/qp)*100)


    #Forum read until date
    def forumread(self, uid, date, df):
        #enthält die Zeitpunkte wann die Posts 256-306 gemacht wurden
        creationdates = []
        for i in range(256,307):
            forumr = df[df["postid"].isin([i])]
            firstreads = df["firstread"].tolist()
            creationdate = min(firstreads)
            creationdates += [creationdate]

        counter = 0 #index für creationdates
        pc = 0 #anzahl bis date veröffentlichter posts
        rc = 0 #anzahl gelesenser post
        for postid in range(256,307):
            dataf = df.loc[(df["userid"] == uid) & (df["postid"] == postid)]
            #falls user den Post gar nicht liest
            try:
                firstread = dataf["firstread"].values[0]
            except:
                if creationdates[counter] > date:
                    counter +=1
                    continue
                else:
                    pc +=1
                    counter +=1
                    continue
            if creationdates[counter] > date:
                counter +=1
                continue
            if date >= firstread :
                rc+=1

            pc +=1
            counter +=1
        return((rc/pc)*100)


    #Material viewed + Participation
    def materialviewed(self, uid, date, df, weekend):
        weeks = [[606, 608, 609, 610, 611], [612, 613, 614, 615, 616, 617], [618, 619, 620, 621, 622, 623], [634, 635, 636, 637, 638], [639, 640, 641, 642, 643, 644, 645], [646, 647, 648, 649, 659], [663, 664, 665, 666, 667], [668, 669, 670, 671, 672, 673], [678, 679, 680, 681], [688, 689, 690, 697, 698], [706, 707, 708]]
        logs = df
        #finde heraus zu welcher Woche das date gehört -- es sollte vorher gefiltert werden das nur Dates aus
        #dem Kurszeitraum erlaubt sind
        week = self.weekcalculation(date, weekend)
        #anzahl der angesehenen Materialien
        viewedc = 0

        #prüfe ob der user sich alle materialien für die jeweilige woche angesehen hat und vor date
        for i in range(len(weeks[week-1])):
            user = ("anonfirstname"+str(uid-112)+" anonlastname"+str(uid-112))
            temp = (logs["User full name"] == user) & logs["Description"].str.contains(str(weeks[week-1][i]))
            viewed = temp.any()
            if viewed == False:
                continue
            #liest Zeitpunkt an dem das Material das erste mal angeklickt wurde ein
            firstocc = logs[(logs["User full name"] == user) & logs["Description"].str.contains(str(weeks[week-1][i]))].iloc[-1]
            firstocctime = firstocc["Time"]
            times = calendar.timegm(time.strptime(firstocctime, "%d/%m/%y, %H:%M"))
            if viewed & (date >= times):
                viewedc += 1
        return((viewedc/len(weeks[week-1])*100))

    def writeV(self, uid, week, value, cat):
        df = pd.read_csv("./CourseData/UserScores.csv")

        #Ersetze den Wert
        temp = df.iloc[uid][cat]
        temp = list(temp)
        temp[week] = str(value)
        temp = "".join(temp)

        df.loc[uid, cat] = temp
        df.to_csv("./CourseData/UserScores.csv", index = False)

    #Engagement Level
    def engagement_level(self, uid, date, logs_df, forumread_df, quiz_df, weekend):
        #enthält die timestamp wann die wochen für die quiz 1-6 beginnen
        quiztimesbeginn = [1600819200,1601424000,1604448000,1605052800,1605657600,1606262400]
        #Engagement Level der letzten Woche
        scores_df = pd.read_csv("./CourseData/UserScores.csv")
        week = self.weekcalculation(date, weekend)
        if week > 0:
            temp = scores_df.iloc[uid]["Engagement"]
            temp = list(temp)
            engagement_level_LW = int(temp[week-1])

        #MaterialLevel
        mvl = 999
        #materialviewed(uid, date, df (logs), [[Material der Wochen 1-11]], [timestamps ende der wochen])
        #MaterialViewedPercentage
        mvp = self.materialviewed(uid, date, logs_df, weekend)
        if mvp > 80:
            mvl = 0
        elif mvp > 60:
            mvl = 1
        elif mvp > 40:
            mvl = 2
        elif mvp > 20:
            mvl = 3
        elif mvp >= 0:
            mvl = 4

        #ForumReadLevel
        frl = 999
        #forumread(uid, date, df (forum_read), [timestamps wann die einzelnen posts erstellt wurden])
        #ForumReadPercentage
        frp = self.forumread(uid, date, forumread_df)
        if frp > 80:
            frl = 0
        elif frp > 60:
            frl = 1
        elif frp > 40:
            frl = 2
        elif frp > 20:
            frl = 3
        elif frp >= 0:
            frl = 4

        #QuizDoneLevel
        qdl = 999
        #quizdone(uid, date, df (quiz_attempts), [timestamps wann die wochen der jeweiligen Quiz 1-6 beginnen])
        #QuizDonePercentage
        qdp = self.quizdone(uid, date, quiz_df, quiztimesbeginn)

        if qdp > 80:
            qdl = 0
        elif qdp > 60:
            qdl = 1
        elif qdp > 40:
            qdl = 2
        elif qdp > 20:
            qdl = 3
        elif qdp >= 0:
            qdl = 4

        engagement_level = round ((mvl + frl + qdl)/3)

        plist = [mvp, frp, qdp]

        #Speicher neue Performance in der Datei
        self.writeV(uid, week, engagement_level, "Engagement")

        #lastWeekScores_df.loc[uid, "Performance"] = performance
        #lastWeekScores_df.to_csv("UserScores.csv")

        if week > 0:
            if engagement_level < engagement_level_LW:
                return (engagement_level, "improved", plist)
            elif engagement_level == engagement_level_LW:
                return (engagement_level, "unchanged", plist)
            elif engagement_level > engagement_level_LW:
                return (engagement_level, "worsened", plist)

        else:
            return (engagement_level, "WeekOne", plist)

