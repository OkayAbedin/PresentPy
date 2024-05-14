from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as mysql
import cv2
from datetime import datetime
from time import strftime
from tkinter import filedialog

class SwiftAttendance:

    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.geometry("1540x860+0+0")
        self.root.title("Swift Attendance")

        img = Image.open(r"UI\SwiftAttendanceBG.png")
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1540, height=860)

        img1 = Image.open(r"UI\BackBtn.png")
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(f_lbl, image=self.photoimg1, cursor="hand2", bg="black", activebackground="black", bd=0, command=self.root.destroy)
        b1.place(x=1344, y=56, width=126, height=40)

        img2 = Image.open(r"UI\MarkAttendanceBtn.png")
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b2 = Button(f_lbl, image=self.photoimg2, cursor="hand2", bg="black", activebackground="black", bd=0, command=self.face_recog)
        b2.place(x=46, y=350, width=1404, height=249)

    def get_file_path(self):
        file_path = filedialog.askopenfilename()
        return file_path

    def mark_attendance(self, i, n, d, file_path):
        with open(file_path, "r+", newline="\n") as file:
            myDataList = file.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split((","))
                nameList.append(entry[0])
            if ((i not in nameList) and (n not in nameList) and (d not in nameList)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                file.writelines(f"\n{i},{n},{d},{d1}, {dtString},Present")

             
    def face_recog(self):
        file_path = self.get_file_path()
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coords = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)
                id, pred = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100*(1-pred/300))

                con = mysql.connect(host="localhost", user="root", password="root", database="presentpy")
                mycursor = con.cursor()

                mycursor.execute("SELECT name FROM student WHERE studentId="+str(id))
                n = mycursor.fetchone()
                n = "+".join(n)

                mycursor.execute("SELECT studentId FROM student WHERE studentId="+str(id))
                i = mycursor.fetchone()
                i = "+".join(i)

                mycursor.execute("SELECT department FROM student WHERE studentId="+str(id))
                d = mycursor.fetchone()
                d = "+".join(d)


                if confidence > 75:
                    cv2.putText(img, f"ID: {i}", (x,y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 1, cv2.LINE_AA)
                    cv2.putText(img, f"Name: {n}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 1, cv2.LINE_AA)
                    cv2.putText(img, f"Department: {d}", (x,y-35), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 1, cv2.LINE_AA)
                    self.mark_attendance(i, n, d, file_path)
                else:
                    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 3)
                    cv2.putText(img, "Unknown", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,0,255), 1, cv2.LINE_AA)
                coords = [x, y, w, h]
            return coords



        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier(r"package\haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_capture = cv2.VideoCapture(0)

        while True:
            ret, img = video_capture.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Swift Attendance", img)

            if cv2.waitKey(1) == 13:
                break
        video_capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk() 
    obj = SwiftAttendance(root)
    root.mainloop()