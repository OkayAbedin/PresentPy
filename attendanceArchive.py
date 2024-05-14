from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import mysql.connector as mysql
import os
import csv
import csv
import os
from tkinter import filedialog
from tkinter import ttk
from tkinter import Label, Button, Frame, Scrollbar
from tkinter.ttk import Treeview

attendance_data=[] 

class AttendanceArchive:
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.geometry("1540x860+0+0")
        self.root.title("Attendance Archive")

        img = Image.open(r"UI\AttendanceArchiveBG.png")
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1540, height=860)

        img1 = Image.open(r"UI\BackBtn.png")
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(f_lbl, image=self.photoimg1, cursor="hand2", bg="black", activebackground="black", bd=0, command=self.root.destroy)
        b1.place(x=1344, y=56, width=126, height=40)

        #variables
        self.var_studentId = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_status = StringVar()

        #Student Information
        class_student_frame = Frame(f_lbl, bg="#FFFBFB")
        class_student_frame.place(x=62, y=291, width=316-10, height=385)

        studentId_label = Label(class_student_frame, text="Student ID", font=("poppins", 10), bg="#FFFBFB")
        studentId_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        studentId_Entry = ttk.Entry(class_student_frame, textvariable=self.var_studentId, font=("poppins", 10))
        studentId_Entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        name_lebel = Label(class_student_frame, text="Name", font=("poppins", 10), bg="#FFFBFB")
        name_lebel.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        name_Entry = ttk.Entry(class_student_frame, textvariable=self.var_name, font=("poppins", 10))
        name_Entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        department_lebel = Label(class_student_frame, text="Department", font=("poppins", 10), bg="#FFFBFB")
        department_lebel.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        department_combo = ttk.Combobox(class_student_frame, textvariable=self.var_department, font=("poppins", 10), state="readonly", width=18)
        department_combo["values"] = ("-","CSE","EEE","BBA","Pharmacy", "English", "Economics", "Mathematics")
        department_combo.current(0)
        department_combo.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        attendance_frame = Frame(f_lbl, bg="#FFFBFB")
        attendance_frame.place(x=62, y=470, width=316-10, height=200)

        date_lebel = Label(attendance_frame, text="Date", font=("poppins", 10), bg="#FFFBFB")
        date_lebel.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        date_Entry = ttk.Entry(attendance_frame, textvariable=self.var_date, font=("poppins", 10))
        date_Entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        time_lebel = Label(attendance_frame, text="Time", font=("poppins", 10), bg="#FFFBFB")
        time_lebel.grid(row=4, column=0, padx=10, pady=10, sticky=W)

        time_Entry = ttk.Entry(attendance_frame, textvariable=self.var_time, font=("poppins", 10))
        time_Entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)

        status_lebel = Label(attendance_frame, text="Attendance", font=("poppins", 10), bg="#FFFBFB")
        status_lebel.grid(row=5, column=0, padx=10, pady=10, sticky=W)

        status_combo = ttk.Combobox(attendance_frame, textvariable=self.var_status, font=("poppins", 10), state="readonly", width=18)
        status_combo["values"] = ("-","Present", "Absent")
        status_combo.current(0)
        status_combo.grid(row=5, column=1, padx=10, pady=10, sticky=W)

        #Import Button
        img2 = Image.open(r"UI\ImportCSVBtn.png")
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b2 = Button(f_lbl, image=self.photoimg2, cursor="hand2", bg="#FFFBFB", activebackground="#FFFBFB", bd=0, command=self.import_data)
        b2.place(x=75, y=670, width=115, height=31)

        #Export Button
        img3 = Image.open(r"UI\ExportCSVBtn.png")
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b3 = Button(f_lbl, image=self.photoimg3, cursor="hand2", bg="#FFFBFB", activebackground="#FFFBFB", bd=0, command=self.export_data)
        b3.place(x=75+115+20, y=670, width=115, height=31)

        #Update Button
        img4 = Image.open(r"UI\UpdateBtn.png")
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b4 = Button(f_lbl, image=self.photoimg4, cursor="hand2", bg="#FFFBFB", activebackground="#FFFBFB", bd=0, command=self.update)
        b4.place(x=75, y=670+41, width=115, height=31)

        #Reset Button
        img5 = Image.open(r"UI\ResetBtn.png")
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b5 = Button(f_lbl, image=self.photoimg5, cursor="hand2", bg="#FFFBFB", activebackground="#FFFBFB", bd=0, command=self.reset)
        b5.place(x=75+115+20, y=670+41, width=115, height=31)

        #Table Frame
        table_frame = Frame(f_lbl, bg="#FFFBFB")
        table_frame.place(x=393, y=291, width=1073-10, height=477-10)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.attendance_table = ttk.Treeview(table_frame, columns=("Student ID", "Name", "Department", "Date", "Time", "Status"), show='headings')
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)

        self.attendance_table.heading("Student ID", text="Student ID")
        self.attendance_table.heading("Name", text="Name")
        self.attendance_table.heading("Department", text="Department")
        self.attendance_table.heading("Date", text="Date")
        self.attendance_table.heading("Time", text="Time")
        self.attendance_table.heading("Status", text="Status")

        self.attendance_table["xscrollcommand"] = scroll_x.set
        self.attendance_table["yscrollcommand"] = scroll_y.set
        self.attendance_table.pack(fill=BOTH, expand=1)

        self.attendance_table.column("Student ID", width=100)
        self.attendance_table.column("Name", width=200)
        self.attendance_table.column("Department", width=100)
        self.attendance_table.column("Date", width=100)
        self.attendance_table.column("Time", width=100)
        self.attendance_table.column("Status", width=100)

        self.attendance_table.bind("<ButtonRelease-1>", self.get_cursor)

    def fetch_data(self, rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END, values=i)

    def import_data(self):
        global attendance_data
        attendance_data.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                attendance_data.append(i)
            self.fetch_data(attendance_data)

    def export_data(self):
        try:
            if len(attendance_data) < 1:
                messagebox.showerror("Error", "No data to export!", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")))
            with open(fln, mode='w', newline='') as myfile:
                csvwriter = csv.writer(myfile, delimiter=",")
                for i in attendance_data:
                    csvwriter.writerow(i)
                messagebox.showinfo("Success", "Data Successfully Exported", parent=self.root)
        except:
            messagebox.showerror("Error", "Failed to export data!", parent=self.root)



    def update(self):
        selected_row_id = self.attendance_table.focus()
        if not selected_row_id:
            messagebox.showerror("Error", "No row selected!", parent=self.root)
            return
        values = (
            self.var_studentId.get(),
            self.var_name.get(),
            self.var_department.get(),
            self.var_date.get(),
            self.var_time.get(),
            self.var_status.get()
        )
        selected_row_index = self.attendance_table.index(selected_row_id)
        self.attendance_table.item(selected_row_id, values=values)
        attendance_data[selected_row_index] = values 
        self.export_data()  

    def get_cursor(self, event):
        cursor_row = self.attendance_table.focus()
        content = self.attendance_table.item(cursor_row)
        row = content["values"]
        self.var_studentId.set(row[0])
        self.var_name.set(row[1])
        self.var_department.set(row[2])
        self.var_date.set(row[3])
        self.var_time.set(row[4])
        self.var_status.set(row[5])


    def reset(self):
        self.var_studentId.set("")
        self.var_name.set("")
        self.var_department.set("-")
        self.var_date.set("")
        self.var_time.set("")
        self.var_status.set("-")



if __name__ == "__main__":
    root = Tk() 
    obj = AttendanceArchive(root)
    root.mainloop()       