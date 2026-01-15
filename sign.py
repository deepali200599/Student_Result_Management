from tkinter import*
from PIL import Image , ImageTk #pip install pillow
from tkinter import ttk  , messagebox
import sqlite3
# from login import LoginClass
import os
class SignClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student result Management System")
        self.root.geometry("1400x580+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #====title=====
        
        # title=Label(self.root,text="Add Student Results",font=("goudy old style",20,"bold"),bg="lightyellow",fg="#262626").place(x=10,y=15,width=1380,height=50)

        self.left=ImageTk.PhotoImage(file="clock.webp")
        left=Label(self.root,image=self.left).place(x=80,y=90,width=400,height=500)

        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=90,width=700,height=550)

        title=Label(frame1,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="green").place(x=50,y=30)

        email=Label(frame1,text="EMAIL ADDRESS",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightyellow")
        self.txt_email.place(x=50,y=150,width=400 ,height=35)

        password=Label(frame1,text="PASSWORD",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=220)
        self.txt_pass=Entry(frame1,font=("times new roman",15),bg="lightyellow")
        self.txt_pass.place(x=50,y=270,width=400,height=35)

        btn_reg=Button(frame1,text="Register new Account ?",font=("goudy old style",20,"bold"),bd=0,bg="white",fg="#B00857",cursor="hand2",command=self.add_login).place(x=50,y=310)

        btn_login=Button(frame1,text="Login",font=("goudy old style",20,"bold"),bg="#289898",fg="white",cursor="hand2",command=self.login).place(x=170,y=380,width=180,height=40)
    
    
    def add_login(self):
        from login import LoginClass
        self.root.destroy()
        root=Tk()
        
        obj=LoginClass(root)
        root.mainloop()
         
   


    def login(self):
        if self.txt_email.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","All Fields are required ",parent=self.root)
        else:
           try:
            con=sqlite3.connect(database="rms.db")
            cur=con.cursor()
            cur.execute("select * from employee where email=? and  password=?",(self.txt_email.get(),self.txt_pass.get()))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid USERNAME & PASSWORD ",parent=self.root)
                

            else:
                messagebox.showinfo("Sucess",f"Welcome {self.txt_email.get()}",parent=self.root)
                self.root.destroy()
                os.system("python dashboard.py")
             
           except Exception as es:
               messagebox.showerror("Error",f"Error due to : {str(es)}",parent=self.root)
              

if __name__=="__main__":
    root=Tk()
    obj=SignClass(root)
    root.mainloop()