from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector as mysql
import cv2
import os
import glob

class StudentHub:
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.geometry("1540x860+0+0")
        self.root.title("Student Hub")

        #variables
        self.var_studentId = StringVar()
        self.var_name = StringVar()
        self.var_date_of_birth = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_program = StringVar()
        self.var_department = StringVar()
        self.var_semester = StringVar()
        self.var_course = StringVar()

        #Student Hub Background Image
        img = Image.open(r"UI\StudentHubBG.png")
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1540, height=860)

        #Back Button
        img1 = Image.open(r"UI\BackBtn.png")
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(f_lbl, image=self.photoimg1, cursor="hand2", bg="black", activebackground="black", bd=0, command=self.root.destroy)
        b1.place(x=1344, y=56, width=126, height=40)

        #Class Student Information
        class_student_frame = Frame(f_lbl, bg="#FFFBFB")
        class_student_frame.place(x=62, y=291, width=553-10, height=385)

        studentId_label = Label(class_student_frame, text="Student ID", font=("poppins", 10), bg="#FFFBFB")
        studentId_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        studentId_Entry = ttk.Entry(class_student_frame, textvariable=self.var_studentId, font=("poppins", 10))
        studentId_Entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        name_lebel = Label(class_student_frame, text="Name", font=("poppins", 10), bg="#FFFBFB")
        name_lebel.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        name_Entry = ttk.Entry(class_student_frame, textvariable=self.var_name, font=("poppins", 10))
        name_Entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        date_of_birth_label = Label(class_student_frame, text="Date of Birth", font=("poppins", 10), bg="#FFFBFB")
        date_of_birth_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        date_of_birth_Entry = ttk.Entry(class_student_frame, textvariable=self.var_date_of_birth, font=("poppins", 10))
        date_of_birth_Entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)
        
        gender_label = Label(class_student_frame, text="Gender", font=("poppins", 10), bg="#FFFBFB")
        gender_label.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("poppins", 10), state="readonly", width=18)
        gender_combo["values"] = ("-","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=4, padx=10, pady=10, sticky=W)

        email_label = Label(class_student_frame, text="Email", font=("poppins", 10), bg="#FFFBFB")
        email_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        email_Entry = ttk.Entry(class_student_frame, textvariable=self.var_email, font=("poppins", 10))
        email_Entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        phone_label = Label(class_student_frame, text="Phone", font=("poppins", 10), bg="#FFFBFB")
        phone_label.grid(row=3, column=3, padx=10, pady=10, sticky=W)

        phone_Entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, font=("poppins", 10))
        phone_Entry.grid(row=3, column=4, padx=10, pady=10, sticky=W)


        #current course information
        current_course_frame = Frame(f_lbl, bg="#FFFBFB")
        current_course_frame.place(x=62, y=515, width=553-10, height=150)

        program_lebel = Label(current_course_frame, text="Program       ", font=("poppins", 10), bg="#FFFBFB")
        program_lebel.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        program_combo = ttk.Combobox(current_course_frame, textvariable=self.var_program, font=("poppins", 10), state="readonly", width=18)
        program_combo["values"] = ("-","B.Sc.","M.Sc.","BBA","MBA", "B.Pharm", "M.Pharm", "BA", "MA")
        program_combo.current(0)
        program_combo.grid(row=0, column=1, padx=10, pady=10, sticky=W)
        
        department_lebel = Label(current_course_frame, text="Department", font=("poppins", 10), bg="#FFFBFB")
        department_lebel.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        department_combo = ttk.Combobox(current_course_frame, textvariable=self.var_department, font=("poppins", 10), state="readonly", width=14)
        department_combo["values"] = ("-","CSE","EEE","BBA","Pharmacy", "English", "Economics", "Mathematics")
        department_combo.current(0)
        department_combo.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        semester_lebel = Label(current_course_frame, text="Semester", font=("poppins", 10), bg="#FFFBFB")
        semester_lebel.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("poppins", 10), state="readonly", width=18)
        semester_combo["values"] = ("-","Spring 2024", "Fall 2024")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        course_lebel = Label(current_course_frame, text="Course", font=("poppins", 10), bg="#FFFBFB")
        course_lebel.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("poppins", 10), state="readonly", width=14)
        course_combo["values"] = ("-","CSE221","CSE222","CSE321","CSE315", "CSE101", "MAT111", "ENG123")
        course_combo.current(0)
        course_combo.grid(row=1, column=3, padx=10, pady=10, sticky=W)


        #Save Button
        img2 = Image.open(r"UI\SaveBtn.png")
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b2 = Button(f_lbl, image=self.photoimg2, cursor="hand2", bg="#FFFBFB", activebackground="#FFFBFB", bd=0, command=self.add_data)
        b2.place(x=75, y=647, width=115, height=31)

        #Update Button
        img3 = Image.open(r"UI\UpdateBtn.png")
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b3 = Button(f_lbl, image=self.photoimg3, cursor="hand2", bg="#FFFBFB", activebackground="#FFFBFB", bd=0, command=self.update_data)
        b3.place(x=75+115+20, y=647, width=115, height=31)

        #Delete Button
        img4 = Image.open(r"UI\DeleteBtn.png")
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b4 = Button(f_lbl, image=self.photoimg4, cursor="hand2", bg="#FFFBFB", activebackground="#FFFBFB", bd=0, command=self.delete)
        b4.place(x=75+115+20+115+20, y=647, width=115, height=31)

        #Reset Button
        img5 = Image.open(r"UI\ResetBtn.png")
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b5 = Button(f_lbl, image=self.photoimg5, cursor="hand2", bg="#FFFBFB", activebackground="#FFFBFB", bd=0, command=self.reset)
        b5.place(x=75+115+20+115+20+115+20, y=647, width=115, height=31)

        #Add Photo Sample Button
        img6 = Image.open(r"UI\AddPhotoSampleBtn.png")
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b6 = Button(f_lbl, image=self.photoimg6, cursor="hand2", bg="#FFFBFB", activebackground="#FFFBFB", bd=0, command=self.generate_dataset)
        b6.place(x=75, y=647+31+20, width=243, height=31)

        #Update Photo Sample Button
        img7 = Image.open(r"UI\UpdatePhotoSampleBtn.png")
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b7 = Button(f_lbl, image=self.photoimg7, cursor="hand2", bg="#FFFBFB", activebackground="#FFFBFB", bd=0, command=self.update_dataset)
        b7.place(x=75+243+33, y=647+31+20, width=243, height=31)


        #Search System
        search_frame = Frame(f_lbl, bg="#FFFBFB")
        search_frame.place(x=641, y=291, width=820, height=385)

        search_lebel = Label(search_frame, text="Search By", font=("poppins", 10), bg="#FFFBFB")
        search_lebel.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("poppins", 10), state="readonly", width=18)
        search_combo["values"] = ("Student-ID")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=20, pady=10, sticky=W)

        search_Entry = ttk.Entry(search_frame, font=("poppins", 10))
        search_Entry.grid(row=0, column=2, padx=20, pady=10, sticky=W)


        #Search Button
        img8 = Image.open(r"UI\SearchBtn.png")
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b8 = Button(search_frame, image=self.photoimg8, cursor="hand2", bg="#FFFBFB", activebackground="#FFFBFB", bd=0, command=lambda: self.search_data(search_Entry.get()))
        b8.grid(row=0, column=3, padx=20, pady=10, sticky=W)

        #Show All Button
        img9 = Image.open(r"UI\ShowAllBtn.png")
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b9 = Button(search_frame, image=self.photoimg9, cursor="hand2", bg="#FFFBFB", activebackground="#FFFBFB", bd=0, command=self.show_all)
        b9.grid(row=0, column=4, padx=20, pady=10, sticky=W)

        #Table Frame
        table_frame = Frame(search_frame, bg="#FFFBFB")
        table_frame.place(x=0, y=50, width=820, height=335)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=("Student ID", "Name", "Program", "Department", "Semester", "Course", "Email", "Phone", "DoB", "Gender"), show='headings')
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)

        self.student_table.heading("Student ID", text="Student ID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Program", text="Program")
        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("DoB", text="DoB")
        self.student_table.heading("Gender", text="Gender")

        self.student_table["xscrollcommand"] = scroll_x.set
        self.student_table["yscrollcommand"] = scroll_y.set
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.column("Student ID", width=100)
        self.student_table.column("Name", width=200)
        self.student_table.column("Program", width=100)
        self.student_table.column("Department", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Email", width=200)
        self.student_table.column("Phone", width=100)
        self.student_table.column("DoB", width=100)
        self.student_table.column("Gender", width=100)

        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    
    #Function Declaration

    def add_data(self):
        if self.var_studentId.get() == "" or self.var_name.get() == "" or self.var_date_of_birth.get() == "" or self.var_gender.get() == "-" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_program.get() == "-" or self.var_department.get() == "-" or self.var_semester.get() == "-" or self.var_course.get() == "-":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                con = mysql.connect(host="localhost", user="root", password="root", database="presentpy")
                cur = con.cursor()
                cur.execute("insert into student(studentId, name, program, department, semester, course, email, phone, dob, gender) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
                            (self.var_studentId.get(), self.var_name.get(), self.var_program.get(), self.var_department.get(), self.var_semester.get(), self.var_course.get(), self.var_email.get(), self.var_phone.get(), self.var_date_of_birth.get(), self.var_gender.get()))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Success", "Student Added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    def fetch_data(self):
        con = mysql.connect(host="localhost", user="root", password="root", database="presentpy")
        cur = con.cursor()
        cur.execute("select * from student")
        data = cur.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in data:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()


    def get_cursor(self, event=""):
        selected_row = self.student_table.focus()
        data = self.student_table.item(selected_row)
        row = data['values']

        if row and len(row) >= 10: 
            self.var_studentId.set(row[0])
            self.var_name.set(row[1])
            self.var_date_of_birth.set(row[8])
            self.var_gender.set(row[9])
            self.var_department.set(row[3])
            self.var_program.set(row[2])
            self.var_semester.set(row[4])
            self.var_course.set(row[5])
            self.var_phone.set(row[7])
            self.var_email.set(row[6])
        else:
            pass
    
    def update_data(self):
        if self.var_studentId.get() == "":
            messagebox.showerror("Error", "Please select a student to update")
        else:
            try:
                con = mysql.connect(host="localhost", user="root", password="root", database="presentpy")
                cur = con.cursor()
                confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to update this student record?")
                if confirmation:
                    cur.execute("update student set name=%s, program=%s, department=%s, semester=%s, course=%s, email=%s, phone=%s, dob=%s, gender=%s where studentId=%s",
                                (self.var_name.get(), self.var_program.get(), self.var_department.get(), self.var_semester.get(), self.var_course.get(), self.var_email.get(), self.var_phone.get(), self.var_date_of_birth.get(), self.var_gender.get(), self.var_studentId.get()))
                    con.commit()
                    self.fetch_data()
                    self.clear()
                    con.close()
                    messagebox.showinfo("Success", "Student record updated successfully")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def clear(self):
        self.var_studentId.set("")
        self.var_name.set("")
        self.var_date_of_birth.set("")
        self.var_gender.set("-")
        self.var_department.set("-")
        self.var_program.set("-")
        self.var_semester.set("-")
        self.var_course.set("-")
        self.var_phone.set("")
        self.var_email.set("")

    def delete(self):
        if self.var_studentId.get() == "":
            messagebox.showerror("Error", "Please select a student to delete.", parent=self.root)
        else:
            try:
                con = mysql.connect(host="localhost", user="root", password="root", database="presentpy")
                cur = con.cursor()
                confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this student record?", parent=self.root)
                if confirmation:
                    cur.execute("DELETE FROM student WHERE studentId = %s", (self.var_studentId.get(),))
                    con.commit()
                    con.close()
                    self.fetch_data()
                    self.clear()
                    messagebox.showinfo("Success", "Student deleted successfully.", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)

    def reset(self):
        self.clear()
        self.fetch_data()

    def search_data(self, studentId):
        try:
            con = mysql.connect(host="localhost", user="root", password="root", database="presentpy")
            cur = con.cursor()
            cur.execute("SELECT * FROM student WHERE studentId = %s", (studentId,))
            data = cur.fetchall()
            con.close()
            if data:
                self.student_table.delete(*self.student_table.get_children())
                for row in data:
                    self.student_table.insert('', END, values=row)
            else:
                messagebox.showinfo("Info", "No student found with this ID.", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)

    def show_all(self):
        try:
            con = mysql.connect(host="localhost", user="root", password="root", database="presentpy")
            cur = con.cursor()
            cur.execute("SELECT * FROM student")
            data = cur.fetchall()
            con.close()
            if data:
                self.student_table.delete(*self.student_table.get_children())
                for row in data:
                    self.student_table.insert('', END, values=row)
            else:
                messagebox.showinfo("Info", "No data found.", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)

    
    #Add photo samples
    def generate_dataset(self):
        if self.var_studentId.get() == "" or self.var_name.get() == "" or self.var_date_of_birth.get() == "" or self.var_gender.get() == "-" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_program.get() == "-" or self.var_department.get() == "-" or self.var_semester.get() == "-" or self.var_course.get() == "-":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                con = mysql.connect(host="localhost", user="root", password="root", database="presentpy")
                cur = con.cursor()
                cur.execute("select * from student")
                res = cur.fetchall()
                id = 0
                for x in res:
                    id += 1
                cur.execute("update student set name=%s, program=%s, department=%s, semester=%s, course=%s, email=%s, phone=%s, dob=%s, gender=%s where studentId=%s",
                            (self.var_name.get(), self.var_program.get(), self.var_department.get(), self.var_semester.get(), self.var_course.get(), self.var_email.get(), self.var_phone.get(), self.var_date_of_birth.get(), self.var_gender.get(), self.var_studentId.get()==id+1))
                con.commit()    
                self.fetch_data()
                self.clear()
                con.close()

                #load from opencv
                face_classifier = cv2.CascadeClassifier(r"package\haarcascade_frontalface_default.xml")      

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        cropped_face = img[y:y+h, x:x+w]
                        return cropped_face
                    
                cap = cv2.VideoCapture(0)
                imgId = 0
                while True:
                    ret, myframe = cap.read()
                    cropped_face = face_cropped(myframe)
                    if cropped_face is not None:
                        imgId += 1
                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "dataset/user." + str(id) + "." + str(imgId) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(imgId), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)
                    if cv2.waitKey(1) == 13 or int(imgId) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed successfully!", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error during dataset generation: {str(e)}", parent=self.root)
    
    #update photo samples
    def update_dataset(self):
        if self.var_studentId.get() == "" or self.var_name.get() == "" or self.var_date_of_birth.get() == "" or self.var_gender.get() == "-" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_program.get() == "-" or self.var_department.get() == "-" or self.var_semester.get() == "-" or self.var_course.get() == "-":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                # Delete old samples
                files = glob.glob('dataset/user.' + str(self.var_studentId.get()) + '.*.jpg')
                for f in files:
                    os.remove(f)

                # Generate new samples
                face_classifier = cv2.CascadeClassifier(r"package\haarcascade_frontalface_default.xml")      

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        cropped_face = img[y:y+h, x:x+w]
                        return cropped_face
                    
                cap = cv2.VideoCapture(0)
                imgId = 0
                while True:
                    ret, myframe = cap.read()
                    cropped_face = face_cropped(myframe)
                    if cropped_face is not None:
                        imgId += 1
                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "dataset/user." + str(self.var_studentId.get()) + "." + str(imgId) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(imgId), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)
                    if cv2.waitKey(1) == 13 or int(imgId) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Updating dataset completed successfully!", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error during dataset update: {str(e)}", parent=self.root)    

if __name__ == "__main__":
    root = Tk() 
    obj = StudentHub(root)
    root.mainloop()