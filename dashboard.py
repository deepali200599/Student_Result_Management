from tkinter import*
from PIL import Image , ImageTk #pip install pillow
from course import CourseClass
from student import studentClass
from result import ResultClass
from report import ReportClass
import sqlite3

from tkinter import  messagebox
import os

class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student result Management System")
        self.root.geometry("1500x750+0+0")
        self.root.config(bg="white")

        #====icons=====

        self.logo_dash=ImageTk.PhotoImage(file="register.jpg")


        #====title====
        title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#574ABF",fg="white").place(x=0,y=0,relwidth=1,height=60)
        
        #===Menu=====
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1500,height=80)

        btn_course=Button(M_Frame,text="course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=40,y=4,width=200,height=40)

        btn_course=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=280,y=4,width=200,height=40)

        btn_course=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_resultt).place(x=510,y=4,width=200,height=40)
        
        btn_course=Button(M_Frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=750,y=4,width=200,height=40)

        btn_course=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=1000,y=4,width=200,height=40)

        btn_course=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.Exit).place(x=1250,y=4,width=200,height=40)

     #===Content window=======
        self.lbl_img=Image.open("book.avif")
      
        self.bg_img=ImageTk.PhotoImage(self.lbl_img)
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=450,y=250,width=920,height=250)

        #========clock image========

        self.lbl_imgs=Image.open("clock.webp")
        # self.lbl_img=self.lbl_img.resize((920,350),Image.alpha_composite)
        self.bgs_imgs=ImageTk.PhotoImage(self.lbl_imgs)
        self.lbl_bgs=Label(self.root,image=self.bgs_imgs).place(x=50,y=250,width=300,height=400)
    #=======update drrtials=====
        self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#3d1a0f",fg="white")
        self.lbl_course.place(x=400,y=530,width=300,height=100)
        self.lbl_student=Label(self.root,text="Total Students\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#3d1a0f",fg="white")
        self.lbl_student.place(x=750,y=530,width=300,height=100)
        self.lbl_result=Label(self.root,text="Total Results\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#3d1a0f",fg="white")
        self.lbl_result.place(x=1100,y=530,width=300,height=100)
    #====footer====
        footer=Label(self.root ,text="SRMS-Student Result Management System\nContact us for any technical issue: 987XXXX90",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        self.update_details()
    
    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
          cur.execute("select * from course ")
          cr=cur.fetchall()
          self.lbl_course.config(text=f"Total Courses[{str(len(cr))}]")

          cur.execute("select * from result ")
          cr=cur.fetchall()
          self.lbl_result.config(text=f"Total Results[{str(len(cr))}]")

          cur.execute("select * from student ")
          cr=cur.fetchall()
          self.lbl_student.config(text=f"Total Students[{str(len(cr))}]")

          self.lbl_course.after(200,self.update_details)
            
        except Exception as ex:
          messagebox.showerror("Error",f"Error due to {str(ex)}")
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)

    def add_resultt(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ResultClass(self.new_win)

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ReportClass(self.new_win)    

    
    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python sign.py")

    def Exit(self):
        op=messagebox.askyesno("Confirm","Do you really want Exit?",parent=self.root)
        if op==True:
            self.root.destroy()
            



     



if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()