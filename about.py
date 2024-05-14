from tkinter import *
from PIL import Image, ImageTk
 

class About:
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.geometry("1540x860+0+0")
        self.root.title("Attendance Archive")

        img = Image.open(r"UI\AboutBG.png")
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1540, height=860)

        img1 = Image.open(r"UI\BackBtn.png")
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(f_lbl, image=self.photoimg1, cursor="hand2", bg="black", activebackground="black", bd=0, command=self.root.destroy)
        b1.place(x=1344, y=56, width=126, height=40)


if __name__ == "__main__":
    root = Tk() 
    obj = About(root)
    root.mainloop()       