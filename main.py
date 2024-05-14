from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from studentHub import StudentHub
from modeilTraining import ModelTraining
from swiftAttendance import SwiftAttendance
from attendanceArchive import AttendanceArchive
from about import About
from help import Help
from tkinter import messagebox


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.geometry("1540x860+0+0")
        self.root.title("Present Py")

        #Dashboard Background Image
        img = Image.open(r"UI\DashboardBG.png")
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1540, height=860)

        #Student Hub Button
        img1 = Image.open(r"UI\StudentHubBtn.png")
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(f_lbl, image=self.photoimg1, cursor="hand2", bg="black", activebackground="black", bd=0, command= self.student_Hub)
        b1.place(x=56, y=441, width=270, height=335)

        #Swift Attendance Button
        img2 = Image.open(r"UI\SwiftAttendanceBtn.png")
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b2 = Button(f_lbl, image=self.photoimg2, cursor="hand2", bg="black", activebackground="black", bd=0, command=self.swift_attendance)
        b2.place(x=348, y=441, width=270, height=335)

        #Attendance Archive Button
        img3 = Image.open(r"UI\AttendanceArchiveBtn.png")
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b3 = Button(f_lbl, image=self.photoimg3, cursor="hand2", bg="black", activebackground="black", bd=0, command=self.attendance_Archive)
        b3.place(x=639, y=441, width=270, height=335)

        #Photo Archive Button
        img4 = Image.open(r"UI\BiometricVaultBtn.png")
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b4 = Button(f_lbl, image=self.photoimg4, cursor="hand2", bg="black", activebackground="black", bd=0, command=self.open_Image)
        b4.place(x=932, y=441, width=270, height=335)

        #Model Training Button
        img5 = Image.open(r"UI\ModelTrainingBtn.png")
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b5 = Button(f_lbl, image=self.photoimg5, cursor="hand2", bg="black", activebackground="black", bd=0, command=self.model_Training)
        b5.place(x=1223, y=441, width=270, height=335)

        #Get Help Button
        img6 = Image.open(r"UI\GetHelpBtn.png")
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b6 = Button(f_lbl, image=self.photoimg6, cursor="hand2", bg="black", activebackground="black", bd=0, command=self.help)
        b6.place(x=1016, y=77, width=185, height=185)

        #About Button
        img7 = Image.open(r"UI\AboutBtn.png")
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b7 = Button(f_lbl, image=self.photoimg7, cursor="hand2", bg="black", activebackground="black", bd=0, command=self.about)
        b7.place(x=1197, y=218, width=155, height=155)

        #Exit Button
        img8 = Image.open(r"UI\ExitBtn.png")
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b8 = Button(f_lbl, image=self.photoimg8, cursor="hand2", bg="black", activebackground="black", bd=0, command=self.exit)
        b8.place(x=1320, y=92, width=126, height=126)

        
    # Function Buttons
    def student_Hub(self):
        self.new_window = Toplevel(self.root)
        self.app = StudentHub(self.new_window)

    def open_Image(self):
        os.startfile("dataset")
    
    def model_Training(self):
        self.new_window = Toplevel(self.root)
        self.app = ModelTraining(self.new_window)

    def swift_attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = SwiftAttendance(self.new_window)

    def attendance_Archive(self):
        self.new_window = Toplevel(self.root)
        self.app = AttendanceArchive(self.new_window)

    def about(self):
        self.new_window = Toplevel(self.root)
        self.app = About(self.new_window)

    def help(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)
        
    def exit(self):
        ask = messagebox.askyesno("Exit", "Do you want to exit?", parent=self.root)
        if ask:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk() 
    obj = Face_Recognition_System(root)
    root.mainloop()