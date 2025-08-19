from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("Login System")

        # Background Image
        img = Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\Admin block.jpg")
        self.bg = ImageTk.PhotoImage(img)
        
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame
        frame = Frame(self.root, bg="white")
        frame.place(x=480, y=100, width=340, height=500)
 
if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
