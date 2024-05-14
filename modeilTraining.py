from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from studentHub import StudentHub
import cv2
import os
import numpy as np
from tkinter import messagebox

class ModelTraining:

    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.geometry("1540x860+0+0")
        self.root.title("Model Training")
    
        img = Image.open(r"UI\ModelTrainingBG.png")
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1540, height=860)

        img1 = Image.open(r"UI\BackBtn.png")
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(f_lbl, image=self.photoimg1, cursor="hand2", bg="black", activebackground="black", bd=0, command=self.root.destroy)
        b1.place(x=1344, y=56, width=126, height=40)

        img2 = Image.open(r"UI\TrainModelBtn.png")
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b2 = Button(f_lbl, image=self.photoimg2, cursor="hand2", bg="black", activebackground="black", bd=0, command=self.train_classifier)
        b2.place(x=46, y=350, width=1404, height=249)

    def train_classifier(self):
        data_dir = 'dataset'
        path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
        ids = np.array(ids)

    # Train the classifier and save the model as a .xml file
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Model Training Completed!")

        

if __name__ == "__main__":
    root = Tk() 
    obj = ModelTraining(root)
    root.mainloop()