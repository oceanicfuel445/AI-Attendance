from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Student:
     def __init__(self, root):
        self.root = root
        self.root.geometry("1400x720+0+0")
        self.root.title("Face Recognition System")
        # First Image
        img = Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\icons8-classroom-100.png")
        img = img.resize((400, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img) 
        
        f_lbl = Label(self.root, image=self.photoimg) #RESIZE IMAGE
        f_lbl.place(x=0, y=0, width=400, height=130)
        
        # Second Image
        img1 = Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\icons8-classroom-100.png")
        img1 = img1.resize((400, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1) 
        
        f_lbl = Label(self.root, image=self.photoimg) #RESIZE IMAGE
        f_lbl.place(x=600, y=0, width=400, height=130)
        
        # Third Image
        
        img2 = Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\icons8-classroom-100.png")
        img2 = img2.resize((400, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2) 
        
        f_lbl = Label(self.root, image=self.photoimg2) #RESIZE IMAGE
        f_lbl.place(x=1200, y=0, width=400, height=130)

        # bg image
        img3 = Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\Admin block.jpg")
        img3 = img3.resize((1540, 720), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3) 
        
        bg_img = Label(self.root, image=self.photoimg3) #RESIZE IMAGE
        bg_img.place(x=0, y=130, width=1500, height=620)
        
        #Title
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("Arial", 35, "bold"), bg="white", fg="Black")
        title_lbl.place(x=0, y=0, width=1540, height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1500,height=550)

        #left frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Arial",12,"bold"))
        Left_frame.place(x=10,y=5,width=660,height=500)
        
        img_left= Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\Admin block.jpg")
        img_left= img2.resize((645, 110), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left) 
        
        f_lbl = Label(Left_frame, image=self.photoimg_left) #RESIZE IMAGE
        f_lbl.place(x=5, y=0, width=645, height=90)
        
        #current course

        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("Arial",12,"bold"))
        current_course_frame.place(x=5,y=90,width=645,height=120)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("Arial",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dept_combo=ttk.Combobox(current_course_frame,font=("Arial",12,"bold"),width=17,state="read only")
        dept_combo["values"]=("Select Department","CSE","ETE","ECE","ASE","ME","CH")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("Arial",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,font=("Arial",12,"bold"),width=17,state="read only")
        course_combo["values"]=("Select Course","FE","SE","TE","FE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

       

        #Year
        year_label=Label(current_course_frame,text="Year",font=("Arial",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,font=("Arial",12,"bold"),width=17,state="read only")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

         #Semester
        Semester_label=Label(current_course_frame,text="Semester",font=("Arial",12,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)

        Semester_combo=ttk.Combobox(current_course_frame,font=("Arial",12,"bold"),width=17,state="read only")
        Semester_combo["values"]=("Select Semester","I","II","III","IV","V","VI","VII","VIII")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("Arial",12,"bold"))
        class_student_frame.place(x=5,y=210,width=645,height=260)

        #Student ID
        Studentid_label=Label(class_student_frame,text="Student ID:",font=("Arial",12,"bold"),bg="white")
        Studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentid_entry=ttk.Entry(class_student_frame,width=17,font=("Arial",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student name
        Studentname_label=Label(class_student_frame,text="Student Name:",font=("Arial",12,"bold"),bg="white")
        Studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentname_entry=ttk.Entry(class_student_frame,width=17,font=("Arial",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Class Division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("Arial",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        class_div_entry=ttk.Entry(class_student_frame,width=17,font=("Arial",12,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll no
        roll_no__label=Label(class_student_frame,text="Roll no:",font=("Arial",12,"bold"),bg="white")
        roll_no__label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,width=17,font=("Arial",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("Arial",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_entry=ttk.Entry(class_student_frame,width=17,font=("Arial",12,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        DOB_label=Label(class_student_frame,text="DOB:",font=("Arial",12,"bold"),bg="white")
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        DOB_entry=ttk.Entry(class_student_frame,width=17,font=("Arial",12,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        email_label=Label(class_student_frame,text="Email:",font=("Arial",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,width=17,font=("Arial",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        #Phone
        phone_label=Label(class_student_frame,text="Phone No:",font=("Arial",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(class_student_frame,width=17,font=("Arial",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #Address
        address_label=Label(class_student_frame,text="Address:",font=("Arial",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,width=17,font=("Arial",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher name:",font=("Arial",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(class_student_frame,width=17,font=("Arial",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #Radio button
        radiobtn1=ttk.Radiobutton(class_student_frame,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,text="No Photo Sample",value="Yes")
        radiobtn2.grid(row=5,column=1)

        #buttons frame
        btn_frame=LabelFrame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=197,width=604,height=35)

        save_btn=Button(btn_frame,text="Save",width=9,font=("Arial",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=9,font=("Arial",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=9,font=("Arial",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=9,font=("Arial",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        take_photo_btn=Button(btn_frame,text="TakePhoto",width=9,font=("Arial",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=4)

        update_photo_btn=Button(btn_frame,text="UpdatePhoto",width=9,font=("Arial",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=5)


        #Right frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Arial",12,"bold"))
        Right_frame.place(x=680,y=5,width=800,height=500)

        img_right= Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\Admin block.jpg")
        img_right= img2.resize((638, 110), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right) 
        
        f_lbl = Label(Right_frame, image=self.photoimg_right) #RESIZE IMAGE
        f_lbl.place(x=5, y=0, width=638, height=90)
        
        # Search Frame
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("Arial",12,"bold"))
        Search_frame.place(x=0,y=100,width=790,height=80)
        
        Search_label=Label(Search_frame,text="Search by",font=("Helvetica",12,"bold"),bg="green",fg = "white")
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        Search_combo=ttk.Combobox(Search_frame,font=("Arial",12,"bold"),width=17,state="read only")
        Search_combo["values"]=("Select Student By","Roll No","Name")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        Search_entry=ttk.Entry(Search_frame,width=17,font=("Helvetica",12,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        Search_btn=Button(Search_frame,text="Search",width=9,font=("Helvetica",12,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        ShowAll_btn=Button(Search_frame,text="Show All",width=9,font=("Helvetica",12,"bold"),bg="blue",fg="white")
        ShowAll_btn.grid(row=0,column=4)
        
        Table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=3,y=185,width=790,height=250)
        
        scroll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.StudentTable = ttk.Treeview(Table_frame,column = ('dep','course','year','sem','id','name','roll','gender','dob','photostat'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side= BOTTOM,fill=X)
        scroll_y.pack(side= RIGHT,fill=Y)
        scroll_x.config(command=self.StudentTable.xview)
        scroll_y.config(command=self.StudentTable.yview)
        
        self.StudentTable.heading("dep",text = "Department")
        self.StudentTable.heading("course",text = "Course")
        self.StudentTable.heading("year",text = "Year")
        self.StudentTable.heading("sem",text = "Semester")
        self.StudentTable.heading("id",text = "ID NO")
        self.StudentTable.heading("name",text = "Name")
        self.StudentTable.heading("roll",text = "Department")
        self.StudentTable.heading("gender",text = "Gender")
        self.StudentTable.heading("dob",text = "Date of Birth") 
        self.StudentTable.heading("photostat",text = "Photo Status")       
         
        self.StudentTable["show"] = "headings"
        
        self.StudentTable.column("dep",width=100)
        self.StudentTable.column("course",width=100)
        self.StudentTable.column("year",width=100)
        self.StudentTable.column("sem",width=100)
        self.StudentTable.column("id",width=100)
        self.StudentTable.column("name",width=100)
        self.StudentTable.column("roll",width=100)
        self.StudentTable.column("gender",width=100)
        self.StudentTable.column("dob",width=100)
        self.StudentTable.column("photostat",width=150)
        
        
        
        
        self.StudentTable.pack(fill=BOTH,expand=1)   
        
       
        

        

        
        
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()