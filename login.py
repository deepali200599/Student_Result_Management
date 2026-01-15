from tkinter import*
from PIL import Image , ImageTk #pip install pillow
from tkinter import ttk  , messagebox
import sqlite3
from sign import SignClass
import os

class LoginClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1500x610+40+170")
        
        # self.root.config(bg="white")
        # self.root.focus_force()
        # #====title=====
        
        # title=Label(self.root,text="Add Studen",font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1380,height=50)

        #=========================Left Image=============================================

        self.left=ImageTk.PhotoImage(file="register.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=60,width=400,height=500)

        #============================================Register Frame================

        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=60,width=700,height=550)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)


        

        title=Label(frame1,text="First Name",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightyellow")
        self.txt_fname.place(x=50,y=130,width=250)

        title=Label(frame1,text="Last Name",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightyellow")
        self.txt_lname.place(x=370,y=130,width=250)


        #==================================================================================

        contact=Label(frame1,text="Contact",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=180)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightyellow")
        self.txt_contact.place(x=50,y=210,width=250)

        email=Label(frame1,text="Email",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=370,y=180)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightyellow")
        self.txt_email.place(x=370,y=210,width=250)



        question=Label(frame1,text="Question",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=260)
        self.cmb_question=ttk.Combobox(frame1,font=("times new roman",15),state='readonly')
        self.cmb_question['values']=("Select","Your First Pet name","Your Birth place","Your BestFriend Name")
        self.cmb_question.place(x=50,y=290,width=250)
        self.cmb_question.current(0)

        answer=Label(frame1,text="Answer",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=370,y=260)
        self.cmb_answer=ttk.Combobox(frame1,font=("times new roman",15))
        self.cmb_answer.place(x=370,y=290,width=250)
 



        password=Label(frame1,text="Password",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=340)
        self.txt_pass=Entry(frame1,font=("times new roman",15),bg="lightyellow")
        self.txt_pass.place(x=50,y=370,width=250)

        cpass=Label(frame1,text="Confirm Password",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=370,y=340)
        self.txt_cpass=Entry(frame1,font=("times new roman",15),bg="lightyellow")
        self.txt_cpass.place(x=370,y=370,width=250)

        #==================terms==============
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",20),bg="white").place(x=50,y=420)


        
        btn_reg=Button(frame1,text="Register Now",font=("goudy old style",15,"bold"),bg="#d1245b",fg="white",cursor="hand2",command=self.registerdata).place(x=170,y=480,width=150,height=40)

        btn_login=Button(frame1,text="Sign in",font=("goudy old style",15,"bold"),bg="#5f2e94",fg="white",cursor="hand2",command=self.add_sign).place(x=400,y=480,width=120,height=40)
    # def login_window(self):
    #     self.root.destroy()
    #     import sign

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_answer.delete(0,END)
        
        self.txt_cpass.delete(0,END)
        self.txt_pass.delete(0,END)
        self.cmb_question.current(0)
    def add_sign(self):
        self.root.destroy()
        os.system("python sign.py")
    def registerdata(self):
        # print(self.var_fname.get(),self.txt_lname.get())
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.txt_pass.get()=="" or self.txt_cpass.get()=="" or self.cmb_answer.get()=="" or self.cmb_question.get()=="Select":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        elif self.txt_pass.get()!=self.txt_cpass.get():
            messagebox.showerror("Error","Password and Confirm Password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("error","Please Agree our terms and Condition",parent=self.root)

            
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get()),)
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("error","User Already Exists , Please try with another email",parent=self.root)
                else:
                    cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password)values(?,?,?,?,?,?,?)",(
                        self.txt_fname.get(),
                        self.txt_lname.get(),
                        self.txt_contact.get(),
                        self.txt_email.get(),
                        self.cmb_question.get(),
                        self.cmb_answer.get(),
                        self.txt_pass.get()
                        
                        
                        
                    ))
                    con.commit()
                    
                    messagebox.showinfo("Sucess","Register Sucessfully",parent=self.root)
                    self.clear()
                    
                    self.add_sign()
            except Exception as es:
                messagebox.showerror("error",f"Error due to:{str(es)}",parent=self.root)

        




if __name__=="__main__":
    root=Tk()
    obj=LoginClass(root)
    root.mainloop()