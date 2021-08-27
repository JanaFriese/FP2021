# -*- coding: utf-8 -*-
import pandas as pd

from lackofbackgroundknowledge import Lackofbackgroundknowledge
from performance import Performance
from timeplanning import TimePlanning
from engagement import Engagement
from timecontingency import Timecontingency

try:
    from PySide import QtWidgets
except:
    from PyQt5 import QtWidgets


class Feedback:

    ecolour = 0
    pcolour = 0
    tpcolour = 0
    lobkcolour = 0

    def __init__(self):
        xqwelkrjw = 0
        self.colour = 0 ## hier wird das Level für die Farbe gespeichert


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

    def weekcalculation(self, date, weekend):
        for i in range(len(weekend)-1,-1,-1):
            if date < 1601424000:
                return 0
            if date == weekend[i]:
                return i
            if date > weekend[i]:
                return i+1


    def feedback_method(self, uid, date, button_pressed):
        performance = Performance()
        engagement = Engagement()
        lackofbk = Lackofbackgroundknowledge()
        timeplanning = TimePlanning()
        self.colour = 0

        #PerformanceLevel (performance, x)  x = "improved"|"unchanged"|"worsened"
        quizweeks = [1,2,7,8,9,10]
        quizids = [37,38,39,40,41,42]
        assignmentweeks = [3,5,10,11]
        assignmentids = [27,28,30,31]
        suggorder_weeks = [[606, 608, 609, 610, 611], [613, 614, 615, 616], [618, 619, 620, 621, 623], [634, 635, 636, 637, 638], [644, 641, 642, 643, 640], [642, 646, 647, 649], [663, 664, 666, 667], [668, 669, 671, 672, 673], [678, 679, 681, 680], [688, 689, 690, 697, 698]]
        weekend = [1601424000,1602028800,1602633600,1603238400,1603843200,1604448000,1605052800,1605657600,1606262400,1607472000,1607904000]
        quiza_df = pd.read_csv("./CourseData/cleanrow_quiz_attempts_s3.csv")
        assignmentg_df= pd.read_csv("./CourseData/cleanrow_assign_grades_s3.csv")
        quizg_df = pd.read_csv("./CourseData/cleanrow_quiz_grades.csv")
        pl = performance.performance_level(uid, date, assignmentg_df, quizg_df, quiza_df, assignmentweeks, assignmentids, quizweeks, quizids, weekend)

        week = self.weekcalculation(date, weekend)

        #return value StringFeedback
        sf = ""
        sf += "Week: " + str(week+1)
        
        
        logs_df = pd.read_csv("./CourseData/cleanrow_logs.csv")
        quizattempts_df = pd.read_csv("./CourseData/cleanrow_quiz_attempts_s3.csv")
        assignSub_df = pd.read_csv("./CourseData/cleanrow_assign_submission.csv")

        timecon = Timecontingency()
        #print((timecon.timeContingency(uid, date, logs_df, quizattempts_df, assignSub_df, assignmentids , assignmentweeks, quizweeks, quizids, suggorder_weeks, weekend) + "\n"))

        timecontingency_fb = timecon.timeContingency(uid, date, logs_df, quizattempts_df, assignSub_df, assignmentids , assignmentweeks, quizweeks, quizids, suggorder_weeks, weekend)
        if (timecontingency_fb != "Nothing"):
            sf += (timecontingency_fb + "\n")
        else:
            sf += "\n\n---Reminders---\n"
        
        

        
        sf += "\n---Performance---\n"    

        
        #Kein automatisches Feedback falls Performance < 2 und kein Knopf gedrückt
        if (button_pressed == False) & (pl[0] < 2):
            pl = (999,"keinAutomatischesFeedback")
            

        if pl[1] == "unchangedNoQA":
            sf += "There is no updated feedback this week as there was no quiz or assignment to complete. Feedback based on last week's results:\n"
            pl = (pl[0], "unchanged")
            
        #Woche 1
        #Level 0
        if (pl[0] == 0) & (pl[1] == "WeekOne"):
            sf += "You are starting with an excellent performance this week! Good job!"
        #Level 1
        elif (pl[0] == 1) & (pl[1] == "WeekOne"):
            sf += "You performed very well this week, that’s amazing! Keep it up!"
        #Level 2
        elif (pl[0] == 2) & (pl[1] == "WeekOne"):
            if self.colour < 2:
                self.colour = 2
            Feedback.pcolour = 2
            sf += "You performed well this week. Just make sure to start on time and study the material more concentrated next week. You can do this!"
        #Level 3
        elif (pl[0] == 3) & (pl[1] == "WeekOne"):
            if self.colour < 3:
                self.colour = 3
            Feedback.pcolour = 3
            sf += "You seem to have problems by understanding the material. Now, we are at the beginning so try to ask the teacher or post your questions in the forum so that your difficulties can be clarified."

        #Woche > 1
        #Level 0 - improved
        elif (pl[0] == 0) & (pl[1] == "improved"):
            sf += "Your performance is excellent! Bravo!"
        #Level 0 - unchanged
        elif (pl[0] == 0) & (pl[1] == "unchanged"):
            sf += "You’re keeping up your outstanding performance. Stupendous!"

        #Level 1 - improved
        elif (pl[0] == 1) & (pl[1] == "improved"):
            sf += "You performed very well this week, that’s amazing! Keep it up!"
        #Level 1 - worsened
        elif (pl[0] == 1) & (pl[1] == "worsened"):
            sf += "You performed very well this week, that’s amazing! Keep it up!"
        #Level 1 - unchanged
        elif (pl[0] == 1) & (pl[1] == "unchanged"):
            sf += "Your performance is still on a very good level. Keep going!"

        #Level 2 - improved
        elif (pl[0] == 2) & (pl[1] == "improved"):
            if self.colour < 2:
                self.colour = 2
            Feedback.pcolour = 2
            sf += "You improved your performance – very good! There is still room for improvement, so it is recommended to study the material more concentrated next time. But you are on the right path, keep it up!"
        #Level 2 - worsened
        elif (pl[0] == 2) & (pl[1] == "worsened"):
            if self.colour < 2:
                self.colour = 2
            Feedback.pcolour = 2
            sf += "Your performance this week was not as good as it has been before. Don’t worry, it’s not bad! Just make sure to start on time and study the material more concentrated next week. You can do this!"
        #Level 2 - unchanged
        elif (pl[0] == 2) & (pl[1] == "unchanged"):
            if self.colour < 2:
                self.colour = 2
            Feedback.pcolour = 2
            sf += "You kept up your performance. That’s good! However, your performance has room for improvement. Try to study the material more concentrated next time, then you will learn everything you need to know!"

        #Level 3 - improved
        elif (pl[0] == 3) & (pl[1] == "improved"):
            if self.colour < 3:
                self.colour = 3
            Feedback.pcolour = 3
            sf += "You improved your performance – good job! However, you still seem to struggle to understand all the contents. If you need help, don’t hesitate to ask the teacher or post your questions in the forum!"
        #Level 3 - worsened
        elif (pl[0] == 3) & (pl[1] == "worsened"):
            if self.colour < 3:
                self.colour = 3
            Feedback.pcolour = 3
            sf += "Your performance this week was not as good as it has been before. You seem to struggle to understand all the contents. If you need help, don’t hesitate to ask the teacher or post your questions in the forum!"
        #Level 3 - unchanged
        elif (pl[0] == 3) & (pl[1] == "unchanged"):
            if self.colour < 3:
                self.colour = 3
            Feedback.pcolour = 3
            sf += "Again you seem to struggle by understanding the material. Try to find help so you can improve your behaviour!"

        #Level 4 - worsened
        elif (pl[0] == 4) & (pl[1] == "worsened"):
            sf += "You did not perform well this week. It is important to learn during the semester so you don’t have to catch up everything shortly before the exam. If you study the material but have problems understanding it, please don’t hesitate to ask the teacher for help or reach out to your peers in the forum!"
            self.colour = 4
            Feedback.pcolour = 4
        #Level 4- unchanged
        elif (pl[0] == 4) & (pl[1] == "unchanged"):
            sf += "You did not perform well on the tasks again this week. It is important to learn during the semester so you don’t have to catch up everything shortly before the exam. If you study the material but have problems understanding it, please don’t hesitate to ask the teacher for help or reach out to your peers in the forum!"
            self.colour = 4
            Feedback.pcolour = 4

        #TimePlanning (performance, x)  x = "improved"|"unchanged"|"worsened"
        a_df = pd.read_csv("./CourseData/cleanrow_assign_submission.csv")
        quizattempts_df = pd.read_csv("./CourseData/cleanrow_quiz_attempts_s3.csv")
        weekend = [1601424000,1602028800,1602633600,1603238400,1603843200,1604448000,1605052800,1605657600,1606262400,1607472000,1607904000]
        #wochen in denen es Assignments gibt
        assignmentweeks = [3,5,10,11]
        assignmentids = [27,28,30,31]

        #wochen in denen es Quiz/Assignments gibt
        quizweeks = [1,2,7,8,9,10]
        quizids = [37,38,39,40,41,42]

        sf += "\n\n---Time Planning---\n"
        tp = timeplanning.tp_level(uid, date, a_df, quizattempts_df, weekend, assignmentweeks, assignmentids, quizweeks, quizids)
        
        #Kein automatisches Feedback falls TimePlanning < 2 und kein Knopf gedrückt
        if (button_pressed == False) & (tp[0] < 2):
            tp = (999,"keinAutomatischesFeedback")
        
        
        #Kein Feedback in Woche 4 & 6 da es kein Quiz und kein Assignment gibt & 11 da Assignment4(31) irrelevant ist - "unchangedNoQA"
        if (tp[1] == "unchangedNoQA"):
            tp = (tp[0], "unchanged")
            sf += "There is no updated feedback this week as there was no quiz or assignment to complete. Feedback based on last week's results:\n"
        
        #Woche 1
        #Level 0
        if (tp[0] == 0) & (tp[1] == "WeekOne"):
            sf += "You have finished all tasks on time this week. Great job!"
        #Level 2
        elif (tp[0] == 2) & (tp[1] == "WeekOne"):
            if self.colour < 2:
                self.colour = 2
            Feedback.tpcolour = 2
            sf += "You finished your tasks on time this week, that’s great! However, it seems like you could have needed more time for it. Planning out your week in advance, prioritizing your tasks, and keeping track of your accomplishments in a to-do-list will help you to avoid time pressure and improve your performance next time. You can do this!"
        #Level 3
        elif (tp[0] == 3) & (tp[1] == "WeekOne"):
            if self.colour < 3:
                self.colour = 3
            Feedback.tpcolour = 3
            sf += "You have not finished your tasks this week. In the beginning, it can be difficult to plan your time right but try to make a schedule for the upcoming weeks. It will help you finishing your tasks on time."
            

        #Woche > 1
        #Level 0 - improved
        elif (tp[0] == 0) & (tp[1] == "improved"):
            sf += "You have finished all tasks on time this week. Great job!"
        #Level 0 - unchanged
        elif (tp[0] == 0) & (tp[1] == "unchanged"):
            sf += "You always finish your tasks on time. Your time-planning skills are stupendous! Keep it up!"

        #Level 1 - improved
        elif (tp[0] == 1) & (tp[1] == "improved"):
            sf += "You finished the important tasks on time this week, that's great! Keep going!"
        #Level 1 - worsened
        elif (tp[0] == 1) & (tp[1] == "worsened"):
            sf += "You finished all important tasks on time again, that's great! However, you have submitted later than last week. Just keep an eye on your time-planning. Great job!"
        #Level 1 - unchanged
        elif (tp[0] == 1) & (tp[1] == "unchanged"):
            sf += "You finished all important tasks on time again, that's great! Keep it up!"

        #Level 2 - improved
        elif (tp[0] == 2) & (tp[1] == "improved"):
            if self.colour < 2:
                self.colour = 2
            Feedback.tpcolour = 2
            sf += "You finished your tasks on time this week, that’s great! However, it seems like you could have needed more time for it. Planning out your week in advance, prioritizing your tasks, and keeping track of your accomplishments in a to-do-list will help you to avoid time pressure and improve your performance next time. You can do this!"
        #Level 2 - worsened
        elif (tp[0] == 2) & (tp[1] == "worsened"):
            if self.colour < 2:
                self.colour = 2
            Feedback.tpcolour = 2
            sf += "You finished your tasks late this week. But don’t worry, just pay more attention to the time next week: Plan out your week in advance, prioritize your tasks, and keep track of your accomplishments in a to-do-list. This will prevent time pressure and boost your performance!"
        #Level 2 - unchanged
        elif (tp[0] == 2) & (tp[1] == "unchanged"):
            if self.colour < 2:
                self.colour = 2
            Feedback.tpcolour = 2
            sf += "You finished all tasks again. That’s great, keep it up! However, you also finished late again. Organizing your time can help you to improve your performance. If you have problems planning your time, a time management tool can help you to prevent time pressure. Try it out!"

        #Level 3 - improved
        elif (tp[0] == 3) & (tp[1] == "improved"):
            if self.colour < 3:
                self.colour = 3
            Feedback.tpcolour = 3
            sf += "You finished your tasks late this week but you got better than last week, this is amazing. Keep going !"
        #Level 3 - worsened
        elif (tp[0] == 3) & (tp[1] == "worsened"):
            if self.colour < 3:
                self.colour = 3
            Feedback.tpcolour = 3
            sf += "Did you have a demanding week? You did not finish your tasks this week. To finish your tasks on time, try to plan out your week in advance. A to-do-list or a timer might help you to organize your tasks and prevent time pressure!"
        #Level 3 - unchanged
        elif (tp[0] == 3) & (tp[1] == "unchanged"):
            if self.colour < 3:
                self.colour = 3
            Feedback.tpcolour = 3
            sf += "You have not finished your tasks again. Maybe you should modify your learning routine to be able to finish your tasks in time next week. A to-do-list or a timer might help you to organize your tasks and prevent time pressure!"

        #Level 4 - improved
        elif (tp[0] == 4) & (tp[1] == "worsened"):
            self.colour = 4
            Feedback.tpcolour = 4
            sf += "You repeatedly did not take the quiz. Participation is not mandatory, but it is highly recommended as you can test your knowledge and understanding here. Didn’t you have enough time to take the quiz? It will help if you plan your time properly. Plan your days, prioritize tasks and try to remove distractions when you’re working. You can do this!"
        #Level 4- unchanged
        elif (tp[0] == 4) & (tp[1] == "unchanged"):
            self.colour = 4
            Feedback.tpcolour = 4
            sf += "You repeatedly missed a quiz. To make sure you don’t lose track of this course, you should take the quizzes. They can help you to identify your difficulties. You don’t seem to find the time to take the quizzes or maybe even study for them. A time management tool can help you to organize your tasks. Try it out!"


        #LOBK (performance, x, y)  x = "improved"|"unchanged"|"worsened" performance = 0|1|"2a"|"2b"|3|4    y = Liste zu bearbeitender Materialien
        suggorder_weeks = [[606, 608, 609, 610, 611], [613, 614, 615, 616], [618, 619, 620, 621, 623], [634, 635, 636, 637, 638], [644, 641, 642, 643, 640], [642, 646, 647, 649], [663, 664, 666, 667], [668, 669, 671, 672, 673], [678, 679, 681, 680], [688, 689, 690, 697, 698]]
        weekend = [1601424000,1602028800,1602633600,1603238400,1603843200,1604448000,1605052800,1605657600,1606262400,1607472000,1607904000]
        logs_df = pd.read_csv("./CourseData/cleanrow_logs.csv")

        if week < 10:
                
            sf += "\n\n---Lack of background knowledge---\n"
            lobk = lackofbk.lobk_level(uid, date, logs_df, suggorder_weeks, weekend)
            missingMaterial = lobk[2]
            
            #Kein automatisches Feedback falls LOBK < 2 und kein Knopf gedrückt
            if (button_pressed == False) & (lobk[0] < 2):
                lobk = (0,"keinAutomatischesFeedback")

            #Woche 1
            #Level 0
            if (lobk[0] == 0) & (lobk[1] == "WeekOne"):
                sf += "This week, you studied all the material. This is the best way to learn the content of this course. That’s awesome! Keep it up!"
            #Level 1
            elif (lobk[0] == 1) & (lobk[1] == "WeekOne"):
                sf += "You have looked at all the material, but not in the order suggested. In the next weeks, try to follow the order to get a better overview of the topics."
            #Level 3
            elif (lobk[0] == 3) & (lobk[1] == "WeekOne"):
                if self.colour < 3:
                    self.colour = 3
                Feedback.lobkcolour = 3
                sf += "You have looked at all the material but not in the suggested order. In the next weeks, try to follow the order to get a better overview of the topics."
            #Level 4
            elif (lobk[0] == 4) & (lobk[1] == "WeekOne"):
                if self.colour < 4:
                    self.colour = 4
                Feedback.lobkcolour = 4
                sf += "You have not studied the whole material this week. It is important to study the given material to understand the contents of this course. Now, we are at the beginning but time flies . You should study the missing material as soon as possible. If you need help with it, reach out to the teacher or your peers!"

            #Woche > 1
            #Level 0 - improved
            elif (lobk[0] == 0) & (lobk[1] == "improved"):
                sf += "You have studied all the given material, so you are well prepared for the next test. That’s amazing! Keep it up!"
            #Level 0 - unchanged
            elif (lobk[0] == 0) & (lobk[1] == "unchanged"):
                sf += "You keep studying the material carefully. This way you learn the contents of this course best. That’s awesome! Keep it up!"

            #Level 1 - improved
            elif (lobk[0] == 1) & (lobk[1] == "improved"):
                sf += "You have looked at all the material – that’s great, keep it up! Next time, also try to follow the suggested order. This can give you a better overview and understanding of the contents."
            #Level 1 - worsened
            elif (lobk[0] == 1) & (lobk[1] == "worsened"):
                sf += "You have looked at all the material – that’s great! However, following the suggested order might give you a better understanding of the contents. Try it out next time!"
            #Level 1 - unchanged
            elif (lobk[0] == 1) & (lobk[1] == "unchanged"):
                sf += "You keep studying all the material. That’s amazing! However, following the suggested order might give you a better understanding of the contents. Try it out next time!"

            #Level 2 - 2a
            elif (lobk[0] == 21):
                if self.colour < 2:
                    self.colour = 2
                Feedback.lobkcolour = 2
                sf += "You looked at all the material and followed the suggested order, that is great! Keep up the good work!"
            #Level 2 - 2b
            elif (lobk[0] == 22):
                if self.colour < 2:
                    self.colour = 2
                Feedback.lobkcolour = 2
                sf += "You have not looked at the whole material this week. For a deeper understanding, it may be beneficial to look at all the material. Try it out next week!"


            #Level 3 - improved
            elif (lobk[0] == 3) & (lobk[1] == "improved"):
                if self.colour < 3:
                    self.colour = 3
                Feedback.lobkcolour = 3
                sf += "You have studied all the material this week – that’s awesome! However, you still seem to have problems understanding it. But following the suggested order and reading/watching the material more carefully can help you to boost your performance – try it out!"
            #Level 3 - worsened
            elif (lobk[0] == 3) & (lobk[1] == "worsened"):
                if self.colour < 3:
                    self.colour = 3
                Feedback.lobkcolour = 3
                sf += "You have studied all the material, very good! But you seem to have problems understanding it. Following the suggested order might help you to understand the material better. However, if you need help, don’t hesitate to ask the teacher or post your questions in the forum!"
            #Level 3 - unchanged
            elif (lobk[0] == 3) & (lobk[1] == "unchanged"):
                if self.colour < 3:
                    self.colour = 3
                Feedback.lobkcolour = 3
                sf += "You have not followed the suggested order of the material again. Following the suggested order and reading/watching the material more carefully can help you to boost your performance – try it out!"

            #Level 4 - improved
            elif (lobk[0] == 4) & (lobk[1] == "worsened"):
                self.colour = 4
                Feedback.lobkcolour = 4
                sf += "You have not studied the material this week. It is important to study the given material to understand the contents of this course. You should study the missing material as soon as possible so you can catch up with the material in time before the exam. If you need help with it, reach out to the teacher or your peers!"
            #Level 4- unchanged
            elif (lobk[0] == 4) & (lobk[1] == "unchanged"):
                self.colour = 4
                Feedback.lobkcolour = 4
                sf += "You have repeatedly not studied all the material. It is important to study the given material to understand the contents of this course. You should study the missing material as soon as possible so you can catch up with the material in time before the exam. If you need help with it, reach out to the teacher or your peers!"

            #You missed the following Material --- nicht anzeigen falls autom. FB & LOBK < 2
            if (button_pressed == False) & (lobk[0] < 2):
                kljdfaksdjf = 0
            else:
                materials = self.material_m(missingMaterial)
                sf += ("\nMissing material: " + " ".join(materials))
        
        else:
            sf += "\n\n---Lack of background knowledge---\n"

        #Engagement (performance, x)  x = "improved"|"unchanged"|"worsened" performance = 0|1|"2a"|"2b"|3|4    (++ Informationen, was/wieivel man gemacht hat)
        df = pd.read_csv("./CourseData/clean_user.csv")
        users = df.id.tolist()
        weekend = [1601424000,1602028800,1602633600,1603238400,1603843200,1604448000,1605052800,1605657600,1606262400,1607472000,1607904000]
        forumread_df = pd.read_csv("./CourseData/cleanrow_forum_read.csv")
        quiz_df = pd.read_csv("./CourseData/cleanrow_quiz_attempts_s3.csv")

        sf += "\n\n---Engagement---\n"

        e = engagement.engagement_level(uid, date, logs_df, forumread_df, quiz_df, weekend)
        
        #Kein automatisches Feedback falls Engagement < 2 und kein Knopf gedrückt
        if (button_pressed == False) & (e[0] < 2):
            e = (0,"keinAutomatischesFeedback",[999,999,999])

        #[mvp, frp, qgp]
        plist = e[2]

        #Woche 1
        #Level 0
        if (e[0] == 0) & (e[1] == "WeekOne"):
            sf += "Your engagement in the first week was amazing, keep it up!"
        #Level 1
        elif (e[0] == 1) & (e[1] == "WeekOne"):
            sf += "You are engaged, almost perfect – Try to focus on it more next week so your engagement will be perfect."
        #Level 2
        elif (e[0] == 2) & (e[1] == "WeekOne"):
            sf += "You are engaged, but you can do better! Try to focus on it next week!"
            if self.colour < 2:
                self.colour = 2
            Feedback.ecolour = 2            
        #Level 3
        elif (e[0] == 3) & (e[1] == "WeekOne"):
            if self.colour < 3:
                self.colour = 3
            Feedback.ecolour = 3
            sf += "Yet, you do not engage a lot in this course. Maybe it is because you are in the first week? Try to improve your engagement so you do not get into trouble."
        #Level 4
        elif (e[0] == 4) & (e[1] == "WeekOne"):
            self.colour = 4
            Feedback.ecolour = 4
            sf += "Yet, you do not engage a lot in this course. Maybe it is because you are in the first week? Try to improve your engagement so you do not get into trouble."

        #Woche > 1
        #Level 0 - improved
        elif (e[0] == 0) & (e[1] == "improved"):
            sf += "You are engaging a lot in this course – that’s great! Keep it up!"
        #Level 0 - unchanged
        elif (e[0] == 0) & (e[1] == "unchanged"):
            sf += "You are engaging a lot in this course – that’s great! Keep it up!"

        #Level 1 - improved
        elif (e[0] == 1) & (e[1] == "improved"):
            sf += "You increased your engagement in this course, good job! Now it is almost perfect – there are only a few things you have not viewed yet. Go on and complete the last few tasks!"
        #Level 1 - worsened
        elif( e[0] == 1) & (e[1] == "worsened"):
            sf += "You are still very engaged in this course. Great! However, there are a few things you have not viewed yet. Go on and complete the last few tasks!"
        #Level 1 - unchanged
        elif (e[0] == 1) & (e[1] == "unchanged"):
            sf += "You are very engaged in this course. Almost perfect! There are only a few things you have not viewed yet. Go on and complete the last few tasks!"

        #Level 2 - improved
        elif (e[0] == 2) & (e[1] == "improved"):
            if self.colour < 2:
                self.colour = 2
            Feedback.ecolour = 2
            sf += "You are engaging more and more in this course. Very good! You are definitely on the right path. Keep it up and try to increase your engagement even more next week! This will help you to improve your performance and to learn more in the long run."
        #Level 2 - worsened
        elif (e[0] == 2) & (e[1] == "worsened"):
            if self.colour < 2:
                self.colour = 2
            Feedback.ecolour = 2
            sf += "Your engagement in this course has decreased. Do not worry, you did not miss a lot yet. Just keep an eye on this so you do not lose track!"
        #Level 2 - unchanged
        elif (e[0] == 2) & (e[1] == "unchanged"):
            if self.colour < 2:
                self.colour = 2
            Feedback.ecolour = 2
            sf += "You are quite engaged in this course. That is good! However, there are still some tasks pending. Try to catch up as soon as possible so the undone tasks do not pile up!"

        #Level 3 - improved
        elif (e[0] == 3) & (e[1] == "improved"):
            if self.colour < 3:
                self.colour = 3
            Feedback.ecolour = 3
            sf += "You increased your engagement in this course. That is awesome! However, there is still a lot to do, but you are on the right path. Keep it up!"
        #Level 3 - worsened
        elif (e[0] == 3) & (e[1] == "worsened"):
            if self.colour < 3:
                self.colour = 3
            Feedback.ecolour = 3
            sf += "Your engagement in this course has decreased. Increase your engagement again before you have missed too much!"
        #Level 3 - unchanged
        elif (e[0] == 3) & (e[1] == "unchanged"):
            if self.colour < 3:
                self.colour = 3
            Feedback.ecolour = 3
            sf += "You do not engage a lot in this course. This way you may end up missing a lot of information and will have trouble to study everything in time for the exam. Increasing your engagement during the semester will help you to ease your exam preparation and improve your performance!"

        #Level 4 - improved
        elif (e[0] == 4) & (e[1] == "worsened"):
            self.colour = 4
            Feedback.ecolour = 4
            sf += "You do not engage in this course anymore. Do you think about quitting? If you start studying the missing material now, it is not too late to finish this course successfully!"
        #Level 4- unchanged
        elif (e[0] == 4) & (e[1] == "unchanged"):
            self.colour = 4
            Feedback.ecolour = 4
            sf += "You are here to look at this feedback. Great! You have not engaged in this course for a while now. To finish the course successfully, you should catch up with the material, quizzes and posts in the forum as soon as possible. It is not too late, you can do this!"
        
        #Prozente nicht anzeigen wenn autom. FB & Engagement < 2
        if (button_pressed == False) & (e[0] < 2):
            kljdfsadf=0
        else:    
            sf += "\nMaterial viewed (Material, Assignment, Webinars...): " + str(plist[0]) + "%" + "\nForum read (overall): " + str(plist[1]) + "%" + "\nQuiz done (overall): " + str(plist[2]) + "%"
        
        return (sf, self.colour)
