from base64 import encode
import csv
import encodings
from tkinter import *
import re
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import filedialog
from tkinter import messagebox

class SampleData(object):
    def __init__(self, root):
        
        FilePath=Label(root, width=15)
        FilePath.config(text="Enter the file Path: ",fg="Aqua", bg="Black")
        FilePath.grid(row=2, column=1, padx=(5, 10), pady=(20, 0))
        
        year=Label(root, width=15)
        year.config(text="Year: ",fg="Aqua", bg="Black")
        year.grid(row=4, column=1, padx=(5, 10), pady=(20, 0))
        
        department=Label(root, width=15)
        department.config(text="Department: ",fg="Aqua", bg="Black")
        department.grid(row=4, column=3, padx=(5, 10), pady=(20, 0))
        
        warnings=Label(root, width=15)
        warnings.config(text="Warnings: ", fg="Aqua", bg="Black")
        warnings.grid(row=6, column=1, padx=(0, 0), pady=(50, 0), sticky=W)
        
        courses=Label(root, width=15)
        courses.config(text="Courses: ", fg="Aqua", bg="Black")
        courses.grid(row=6, column=4, padx=(0, 0), pady=(50, 0), sticky=W)

        self.pathEntry=Entry(root)
        self.pathEntry.grid(row=2, column=2, padx=(0, 0), pady=(20, 0), columnspan=2, sticky=W+E)
        
        self.departmentEntry=Entry(root)
        self.departmentEntry.grid(row=4, column=4, padx=(0, 0), pady=(20, 0), columnspan=2)
        
#A combobox is a combination of an Entry widget and a Listbox widget. A combobox widget allows you to select one value in a set of values.

        self.comboBox = Combobox(root)
        self.comboBox.bind('<<ComboboxSelected>>')
        self.comboBox.grid(row=4, column=2, padx=(5, 10), pady=(20, 0))
        self.comboBox['values']=(1, 2, 3, 4, 5)
        self.comboBox.current(0)

        btnDisplay=Button(root) 
        btnDisplay.config(text="Display", fg="Aqua", bg="Black", command=self.display)
        btnDisplay.grid(row=5, column=1, sticky=E, padx=(0, 10), pady=(50, 0))
        
        btnClear=Button(root)
        btnClear.config(text="Clear",fg="Aqua", bg="Black", command=self.clear)
        btnClear.grid(row=5, column=2, sticky=W+E, padx=(0, 10), pady=(50, 0))
    
        btnSave=Button(root)
        btnSave.config(text="Save", fg="Aqua", bg="Black", command=self.save)
        btnSave.grid(row=5, column=3, sticky=W+E, padx=(0, 10), pady=(50, 0))
        
#A Listbox widget displays a list of single-line text items. A Listbox allows you to browse through the items and select one or multiple items at once.

        self.warBox=Listbox(root, width=65)
        self.warBox.grid(row=7, column=1, columnspan=3, pady=(50,0), sticky=E+W)

        self.coursesBox=Listbox(root, width=65)
        self.coursesBox.bind("<Double-1>", self.click)
        self.coursesBox.grid(row=7, column=4, columnspan=3, padx=(10, 0), pady=(50,0), sticky=E+W)

        

#The rules for translating a Unicode string into a sequence of bytes are called a character encoding, or just an encoding.

    def display(self):
        csv_file=self.pathEntry.get()
        file=open(str(csv_file),'r', encoding="unicode_escape")

        courses=list()        
        for each_row in file:
            courses.append(each_row)
        for each_element in courses:
            if (each_element.split(' ')[0].startswith(self.departmentEntry.get().upper())) and (each_element.split(' ')[0].endswith(self.departmentEntry.get().upper())) and (each_element.split(' ')[1].startswith(self.comboBox.get())):
                self.coursesBox.insert(END, each_element)

    def clear(self):
        self.pathEntry.delete(0, END)
        self.comboBox.delete(0, END)
        self.departmentEntry.delete(0, END)
        self.coursesBox.delete(0, END)
        self.warBox.delete(0, END)
    
    global list1
    list1=[]
    def click(self, event):
        selection=event.widget.curselection()
        if self.warBox.size() > 5:
            messagebox.showinfo("Info", "You can choose only 6 courses")
        else:
            for i in selection:
                self.f_selected = event.widget.get(i)
                self.warlist = self.warBox.get(0, END)
                fo_selected = self.f_selected.split(',')[2]
                fif_selected = fo_selected.split(' ')[0]
                if  (len(selection) <= 6) and selection:
                    th_selected = self.f_selected.split(',')[0]
                    se_selected = self.f_selected.split(',')
                    if (f"Added {th_selected}") not in self.warlist:
                        self.warBox.insert(0, (f"Added {th_selected}"))
        event_1=event.widget
        click_select = event_1.curselection()
        if click_select:
            for each_select in click_select: 
                global save_select
                save_select=event_1.get(each_select)
        list1.append(save_select)    
    
    def save(self):
        save_csv=open("sample_data.csv", 'w')
        write = csv.writer(save_csv)
        for each_row in list1:
            write.writerow(each_row.split(", "))
        save_csv.close()

def main():
    root = Tk()
    a=SampleData(root)
    root.geometry("820x500+300+300")
    root.minsize(820,500)
    root.maxsize(820,500)
    root.config(bg="Gray")
    root.mainloop()

main()

    

