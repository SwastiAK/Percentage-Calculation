# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 12:50:53 2022

@author: Swasti
"""

from tkinter import *
root = Tk()

root.title("% Calculation")
root.geometry("600x600")

pa_grade_1_label = Label(root)
pa_grade_5_label = Label(root)
pa_grade_7_label = Label(root)

class grade_1():
    
    def __init__(self, lang_arts, maths):
        self.lang_arts = lang_arts
        self.maths = maths
        
    def percentage(self):
        total_marks = self.lang_arts + self.maths
        tm_with_100 = total_marks * 100
        grade_1_pa = tm_with_100 / 200
        pa_grade_1_label["text"] = grade_1_pa
        
class grade_5():
    
    def __init__(self, lang_arts, maths, sst):
        self.lang_arts = lang_arts
        self.maths = maths
        self.sst = sst
        
    def percentage(self):
        total_marks = self.lang_arts + self.maths + self.sst
        tm_with_100 = total_marks * 100
        grade_5_pa = tm_with_100 / 300
        pa_grade_5_label["text"] = grade_5_pa
        
class grade_7():
    
    def __init__(self, lang_arts, maths, sst, foreign_lang):
        self.lang_arts = lang_arts
        self.maths = maths
        self.sst = sst
        self.foreign_lang = foreign_lang
        
    def percentage(self):
        total_marks = self.lang_arts + self.maths + self.sst + self.foreign_lang
        tm_with_100 = total_marks * 100
        grade_7_pa = tm_with_100 / 400
        pa_grade_7_label["text"] = grade_7_pa
        
obj_grade_1 = grade_1(40, 50)
grade_1_btn = Button(root, text = "Grade - 1", command = obj_grade_1.percentage)
grade_1_btn.pack(padx = 20, pady = 20)
pa_grade_1_label.pack(padx = 20, pady = 20)

obj_grade_5 = grade_5(40, 50, 70)
grade_5_btn = Button(root, text = "Grade - 5", command = obj_grade_5.percentage)
grade_5_btn.pack(padx = 20, pady = 20)
pa_grade_5_label.pack(padx = 20, pady = 20)

obj_grade_7 = grade_7(40, 50, 70, 90)
grade_7_btn = Button(root, text = "Grade - 7", command = obj_grade_7.percentage)
grade_7_btn.pack(padx = 20, pady = 20)
pa_grade_7_label.pack(padx = 20, pady = 20)

root.mainloop()