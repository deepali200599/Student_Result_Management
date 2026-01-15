from tkinter import*
from PIL import Image , ImageTk #pip install pillow
from tkinter import ttk  , messagebox
import sqlite3
class ResultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student result Management System")
        self.root.geometry("1400x580+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #====title=====
        
        title=Label(self.root,text="Add Student Results",font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1380,height=50)
     #==========================labels======================================

     #========================var=========================
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_fullmarks=StringVar()
        self.roll_list=[]
        self.fetch_roll()
        lbl_select=Label(self.root,text="Select Student",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=100)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=160)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=220)
        lbl_marks_obt=Label(self.root,text="Marks Obtained",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=280)
        lbl_full_marks=Label(self.root,text="Full marks",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=340)

        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.txt_student.place(x=280,y=100,width=200)
        self.txt_student.set("Select")
        
        btn_searh=Button(self.root,text="Search",font=("goudy old style",20,"bold"),bg="#cbad3f",fg="white",cursor="hand2",command=self.search).place(x=500,y=100,width=120,height=35)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",20,"bold"),bg="lightyellow",state='readonly').place(x=280,y=160,width=350)
        txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",20,"bold"),bg="lightyellow",state='readonly').place(x=280,y=220,width=350)
        txt_marks=Entry(self.root,textvariable=self.var_marks,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=280,y=280,width=350)
        txt_fullmark=Entry(self.root,textvariable=self.var_fullmarks,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=280,y=340,width=350)

        #==============================button=======================================================================

        btn_add=Button(self.root,text="Submit",font=("times new roman",15),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=self.add).place(x=300,y=420,width=120,height=35)
        btn_clear=Button(self.root,text="Clear",font=("times new roman",15),bg="lightgray",activebackground="lightgray",cursor="hand2",command=self.clear).place(x=470,y=420,width=120,height=35)

        #===Content window=======
        self.lbl_img=Image.open("result.avif")
      
        self.bg_img=ImageTk.PhotoImage(self.lbl_img)
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=630,y=200,width=850,height=300)
    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
          if self.var_name.get()=="":
              messagebox.showerror("Error ","Please search Student Record ",parent=self.root)
          else:
              cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get(),))
              row=cur.fetchone()
              if row !=None:
                   messagebox.showerror("Error ","Result  already Present",parent=self.root)
              else:
                  per=(int(self.var_marks.get())*100/int(self.var_fullmarks.get()))
                  cur.execute("insert into result (roll,name,course,marks,full_marks,per) values(?,?,?,?,?,?,?)",(
                     self.var_roll.get(),
                      self.var_name.get(),
                      self.var_course.get(),
                      self.var_marks.get(),
                      self.var_fullmarks.get(),
                      str(per)
                    
                  ))   
                  con.commit()
                  messagebox.showinfo("Sucess","Result Added sucessfully",parent=self.root) 
                  
        

        except Exception as ex:
          messagebox.showerror("Error",f"Error due to {str(ex)}")
    def clear(self):
        self.var_roll.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),

        self.var_marks.set(""),
        self.var_fullmarks.set("")
        
       

    def search(self):
      con=sqlite3.connect(database="rms.db")
      cur=con.cursor()
      try:
         cur.execute("SELECT name,course FROM student WHERE roll=?", ( self.var_roll.get(),))
         row=cur.fetchone()
         if row!=None:
          self.var_name.set(row[0])
          self.var_course.set(row[1])
         else:
             messagebox.showerror("Error","No Record Found",parent=self.root)
      except Exception as ex:
          messagebox.showerror("Error",f"Error due to {str(ex)}")
    def fetch_roll(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
          cur.execute("select roll from student ")
          rows=cur.fetchall()
        
          if len(rows)>0:
            for row in rows:
                self.roll_list.append(row[0])
               
        
         
        except Exception as ex:
           messagebox.showerror("Error",f"Error due to {str(ex)}")




if __name__=="__main__":
    root=Tk()
    obj=ResultClass(root)
    root.mainloop()