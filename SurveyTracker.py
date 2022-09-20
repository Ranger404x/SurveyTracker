__name__ = "SurveyTracker" 
__author__ = "Sarwan Yadav"
__credits__ = "Sarwan Yadav"
__date__ = "22 August 2022"
__email__ = "rangersarwan@gmail.com"

import calendar
import datetime
import tkinter.messagebox as msalert
from datetime import date
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview

import mysql.connector as dbwire
from mysql.connector import Error


def feedbase():
   def calcage():
      def calc():
         year_of_birth = int(year.get())
         monthofbirth = int(months.index(month.get()) + 1)
         dayofbirth = int(date_stringvar.get())

         today = datetime.datetime.now()
         year_now = int(today.year)
         month_now = int(today.month)
         day_now = int(today.day)

         d0 = date(year_of_birth, monthofbirth , dayofbirth)
         d1 = date(year_now, month_now, day_now)

         delta = d1-d0
         totaldays = delta.days
         age_total = totaldays // 365
   
        

         age.config(text=f"Current Age: {age_total} Years Old", foreground="grey")
         age.place(x=40, y= 200)
      
      frame = Frame(root, width=1250, height=615, bg='#FFF', relief="flat")
      frame.place(x=10,y=73)

      Hr = Frame(frame, width=1, height=220, bg='#dddddd')
      HrSM = Frame(frame, width=8, height=1, bg='#dddddd')
      HrS = Frame(frame, width=1, height=220, bg='#dddddd')
      HrU = Frame(frame, width=244, height=1, bg='#dddddd')
      HrF = Frame(frame, width=370, height=1, bg='#dddddd')   
      Hr.place(x = 30, y = 108)
      HrSM.place(x = 30, y = 108)
      HrS.place(x = 400, y = 108)
      HrU.place(x = 156, y = 108)
      HrF.place(x = 30, y =328)
      Ageh = Label(frame)
      Ageh.configure(text="Age Calculator", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","18","bold"))
      Ageh.place(x=40,y=50)
      
      SubHeading = Label(frame)
      SubHeading.place(x=40,y=100)
      SubHeading.configure(text="Select and Calculate", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","9","bold"))
      
      birth_date = Label(frame,text="Date of Birth:",font=("Times","12"), background ="#FFF" )
      birth_date.place(x = 40, y = 140 )

      month = StringVar()
      months = list(calendar.month_abbr)[1:]
      monthchoosen = ttk.Combobox(frame,font=("Times","10"),width=5,textvariable=month)
      monthchoosen.place(x = 150, y = 142)
      monthchoosen['values'] = months
      monthchoosen.current(0)

      date_stringvar = StringVar()
      datechoosen = ttk.Combobox(frame,font=("Times","10"),width=5,textvariable=date_stringvar)
      datechoosen.place(x = 220, y = 142)
      datechoosen['values'] = [num for num in range(1,32)]
      datechoosen.current(0)

      year = StringVar()
     
      yearchoosen = ttk.Combobox(frame,width=7,font=("Times","10"),textvariable=year)
      yearchoosen.place(x = 290, y = 142)
      yearchoosen['values'] = [num for num in range(2014,2081)]
      yearchoosen.current(0) #.set("2002")
      
      calculate = ttk.Button(frame,command=calc, text="Calculate", width=10, padding=1)
      calculate.place(x=40, y=280)

      age = Label(frame)
      age.configure(height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","8","bold"))
      age.place(x = 40, y = 220)
      
      but = Button(frame, command=frame.destroy)
      but.configure(relief="raised", activeforeground="red", cursor="hand2", height=1, width=9,activebackground="#FCFCFC",overrelief="flat", foreground="#000", background="#EEE", borderwidth="0", text="Close")
      but.place(x=130, y=280)
      
   def feedform_dbc():
      def update(rows):
         listBox.delete(*listBox.get_children())
         for i in rows:
            listBox.insert('', 'end', values=i)
      def clear_src():
         try:
            mysqlDb = dbwire.connect(host = "localhost", user="root", password="", database="sac_2045")
            mycursor = mysqlDb.cursor()
         except Exception:
            msalert.showerror("SurveyTarcker", "Connection Failed!")
         Srcen.delete(0, 'end')
         naen.delete(0, 'end')
         doben.delete(0, 'end')
         fathen.delete(0, 'end')
         mothen.delete(0, 'end')
         panen.delete(0, 'end')
         ageen.delete(0, 'end')
         query = "SELECT namedb, dobdb, fnamedb, mnamedb, condb, agedb, gendb From `dat3-6a`"
         mycursor.execute(query)
         rows = mycursor.fetchall()
         update(rows)
        
      g = genvar.get()
      if g== "Male":
         print("male")
         resul = "Male"
      else:
         print("female")
         resul = "Female"
      try:
         child2 = dbwire.connect(host="localhost", user="root", password="", database="sac_2045")
         cursor = child2.cursor()
      except:
         msalert.showerror("Server","Please Ceck Your Connection....  Try Again Later") 
      try:
         f = cname.get()
         f2 = cdob.get()
         f3 = cfname.get()
         f4  = cmname.get()
         f5 = ccon.get()
         f6 = cage.get()
         f7 = resul
         if f == "" or f2 == "" or f3  == "" or f4 == "" or f5 == "" or f6 == "" or f7 == "":
            msalert.showinfo("Sorry", "Blanked Not Allowed")  
         else:    
            auths = 'SELECT * FROM `dat3-6a` WHERE namedb = %s AND dobdb = %s AND fnamedb = %s AND mnamedb = %s AND condb = %s AND agedb = %s AND gendb = %s '
            auth = (f,f2,f3,f4,f5,f6,f7)
            cursor.execute(auths,auth)
            res = cursor.fetchall()
            if res:
               for row in res:
                  if row:
                     f3 = row[2]
                     f4 = row[3]
                     f6 = row[5]
                     msalert.showwarning("Server", "Child Already Registered")
                  else:
                     pass
            else:
               sqli = 'INSERT INTO `dat3-6a`(`namedb`, `dobdb`, `fnamedb`, `mnamedb`, `condb`, `agedb`, `gendb`)  VALUES (%s, %s, %s, %s,%s, %s, %s)'
               valinsrt = (f,f2,f3,f4,f5,f6,f7)
               cursor.execute(sqli,valinsrt)
               child2.commit()
               msalert.showinfo("Information from Server: 127.0.0.1","Details Sumbitted Successfully...")
               child2.close()
               print(sqli, "Successful Submitted")
               clear_src()
              
      except Exception as s:
         print(s)
         naen.delete(0, 'end')
         doben.delete(0, 'end')
         fathen.delete(0, 'end')
         mothen.delete(0, 'end')
         panen.delete(0, 'end')
         ageen.delete(0, 'end')
         child2.rollback()
         child2.close()
         
   def freedform_dbc():
      def update(rows):
         listBox.delete(*listBox.get_children())
         for i in rows:
            listBox.insert('', 'end', values=i)
      def clear_src():
         try:
            mysqlDb = dbwire.connect(host = "localhost", user="root", password="", database="sac_2045")
            mycursor = mysqlDb.cursor()
         except Exception:
            msalert.showerror("SurveyTarcker", "Connection Failed!")
         Srcen.delete(0, 'end')
         naen.delete(0, 'end')
         doben.delete(0, 'end')
         fathen.delete(0, 'end')
         mothen.delete(0, 'end')
         panen.delete(0, 'end')
         ageen.delete(0, 'end')
         query = "SELECT namedb, dobdb, fnamedb, mnamedb, condb, agedb, gendb From `dat0-3`"
         mycursor.execute(query)
         rows = mycursor.fetchall()
         update(rows)
         
      g = genvar.get()
      if g== "Male":
         print("male")
         resul = "Male"
      else:
         print("female")
         resul = "Female"
      try:
         child = dbwire.connect(host="localhost", user="root", password="", database="sac_2045")
         cursor = child.cursor()
      except:
         msalert.showerror("Server","Please Ceck Your Connection....  Try Again Later") 
      try:
         f = cname.get()
         f2 = cdob.get()
         f3 = cfname.get()
         f4  = cmname.get()
         f5 = ccon.get()
         f6 = cage.get()
         f7 = resul
         if f == "" or f2 == "" or f3  == "" or f4 == "" or f5 == "" or f6 == "" or f7 == "":
            msalert.showinfo("Sorry", "Blanked Not Allowed")  
         else:    
            auths = 'SELECT * FROM `dat0-3` WHERE namedb = %s AND dobdb = %s AND fnamedb = %s AND mnamedb = %s AND condb = %s AND agedb = %s AND gendb = %s '
            auth = (f,f2,f3,f4,f5,f6,f7)
            cursor.execute(auths,auth)
            res = cursor.fetchall()
            if res:
               for row in res:
                  if row:
                     f3 = row[2]
                     f4 = row[3]
                     f6 = row[5]
                     msalert.showwarning("Information from Server: 127.0.0.1", "Child Already Registered")
                  else:
                     pass
            else:
               sqli = 'INSERT INTO `dat0-3`(`namedb`, `dobdb`, `fnamedb`, `mnamedb`, `condb`, `agedb`, `gendb`)  VALUES (%s, %s, %s, %s,%s, %s, %s)'
               valinsrt = (f,f2,f3,f4,f5,f6,f7)
               cursor.execute(sqli,valinsrt)
               child.commit()
               msalert.showinfo("Information from Server: 127.0.0.1","Details Sumbitted Successfully  ")
               child.close()
               clear_src()
      except Exception as s:
         print(s)
         naen.delete(0, 'end')
         doben.delete(0, 'end')
         fathen.delete(0, 'end')
         mothen.delete(0, 'end')
         panen.delete(0, 'end')
         ageen.delete(0, 'end')
         F = Label(feedform_fr, text="Something Went Wrong!                       ", height=1, fg="green",
         border=0, bg="#FFF", font=("sans-serif", "9", "bold"))
         F.place(x=40, y=520)
         child.close()
   
   def feedform_(): 
      def destroyer():
         feedform_fr.destroy()
         TreeFrame.destroy() 
      def update(rows):
         listBox.delete(*listBox.get_children())
         for i in rows:
            listBox.insert('', 'end', values=i)
      def clear_src():
         try:
            mysqlDb = dbwire.connect(host = "localhost", user="root", password="", database="sac_2045")
            mycursor = mysqlDb.cursor()
         except Exception:
            msalert.showerror("SurveyTarcker", "Connection Failed!")

         Srcen.delete(0, 'end')
         naen.delete(0, 'end')
         doben.delete(0, 'end')
         fathen.delete(0, 'end')
         mothen.delete(0, 'end')
         panen.delete(0, 'end')
         ageen.delete(0, 'end')
         query = "SELECT namedb, dobdb, fnamedb, mnamedb, condb, agedb, gendb From `dat0-3`"
         mycursor.execute(query)
         rows = mycursor.fetchall()
         update(rows)
            
      def Delete(event):
         naen.delete(0, 'end')
         doben.delete(0, 'end')
         fathen.delete(0, 'end')
         mothen.delete(0, 'end')
         panen.delete(0, 'end')
         ageen.delete(0, 'end')
         row_id = listBox.selection()[0]
         select = listBox.set(row_id)
         naen.insert(0,select['Name'])
         doben.insert(0,select['D.O.B']) 
         fathen.insert(0,select['Father Name']) 
         mothen.insert(0,select['Mother Name']) 
         panen.insert(0,select['Contact']) 
         ageen.insert(0,select['Age (Current)'])  
         ge = select['Gender']
         genvar.set(value=ge)
      def delete():
         try:
            child = dbwire.connect(host="localhost", user="root", password="", database="sac_2045")
            cursor = child.cursor()
         except:
            msalert.showerror("Server","Please Ceck Your Connection....  Try Again Later") 
         try:
            f = cname.get()
            if f == "":
               msalert.showinfo("Sorry", "Blanked Not Allowed")  
            else:
               try:
                  sql = "DELETE FROM `dat0-3` WHERE `namedb`= %s"
                  val = (f, )
                  cursor.execute(sql, val)
                  child.commit()
                  msalert.showinfo("Information from Server: 127.0.0.1", "Record Deleted Successfully...")
                  naen.delete(0, 'end')
                  doben.delete(0, 'end')
                  fathen.delete(0, 'end')
                  mothen.delete(0, 'end')
                  panen.delete(0, 'end')
                  ageen.delete(0, 'end')
                  naen.focus_set()
                  child.close()
                  clear_src()
               except Exception as e:
                  msalert.showerror("Exception", e)
                  child.rollback()
                  child.close()
                  clear_src()
         except Exception as e:
            msalert.showerror("Exception", e)
            clear_src()     
      def update_tree():
         g = genvar.get()
         if g== "Male":
            print("male")
            resul = "Male"
         else:
            print("female")
            resul = "Female"
         try:
            child = dbwire.connect(host="localhost", user="root", password="", database="sac_2045")
            cursor = child.cursor()
         except:
            msalert.showerror("Server","Please Ceck Your Connection....  Try Again Later") 
         try:
            f = cname.get()
            f2 = cdob.get()
            f3 = cfname.get()
            f4  = cmname.get()
            f5 = ccon.get()
            f6 = cage.get()
            f7 = resul
            if f == "" or f2 == "" or f3  == "" or f4 == "" or f5 == "" or f6 == "" or f7 == "":
               msalert.showinfo("Sorry", "Blanked Not Allowed")  
            else:
               sql = 'UPDATE `dat0-3` SET dobdb =%s, fnamedb =%s, mnamedb =%s, condb =%s, agedb =%s, gendb =%s WHERE namedb = %s'
               val = (f2,f3,f4,f5,f6,f7,f)
               cursor.execute(sql, val)
               print(child, cursor, sql, val)
               child.commit()
               msalert.showinfo("Server", "Records Updated Successfully.....")
               clear_src()
         except Exception as s:
            print(s)
            F = Label(feedform_fr, text="Something Went Wrong!                       ", height=1, fg="green",
            border=0, bg="#FFF", font=("sans-serif", "9", "bold"))
            F.place(x=40, y=520)
            clear_src()
      def show():
         try:
            mysqlDb = dbwire.connect(host = "localhost", user="root", password="", database="sac_2045")
            mycursor = mysqlDb.cursor()
         except Exception as E:
            print(E)
            msalert.showerror("Server 'List Not Fetch'","Please Ceck Your Connection....  Try Again Later") 
         mycursor.execute("SELECT `namedb`, `dobdb`, `fnamedb`, `mnamedb`, `condb`, `agedb`, `gendb` FROM `dat0-3`")
         records = mycursor.fetchall() 
         print(records)
         for i, (namedb,dobdb,fnamedb,mnamedb, condb,agedb,gendb) in enumerate(records, start=1):
            listBox.insert("", "end", values=(namedb,dobdb,fnamedb,mnamedb, condb,agedb,gendb))
            mysqlDb.close()

      def search():
         try:
            mysqlDb = dbwire.connect(host = "localhost", user="root", password="", database="sac_2045")
            mycursor = mysqlDb.cursor()
         except Exception:
            msalert.showerror("SurveyTarcker", "Connection Failed!")
         q2 = q.get()
         query = "SELECT namedb, dobdb, fnamedb, mnamedb, condb, agedb, gendb FROM `dat0-3` WHERE `namedb` LIKE '%"+q2+"%' OR `dobdb` LIKE '%"+q2+"%' OR `fnamedb` LIKE '%"+q2+"%' OR `mnamedb` LIKE '%"+q2+"%' OR `agedb` LIKE '%"+q2+"%' OR `condb` LIKE '%"+q2+"%' OR `gendb` LIKE '%"+q2+"%'"
         mycursor.execute(query)
         rows = mycursor.fetchall()
         update(rows)


   
      global cname, cdob, cfname, cmname, ccon, cage, cgen
      global feedform_fr, TreeFrame
      global naen, doben, fathen, mothen, panen, ageen
      global q
      global genvar, listBox, Srcen
      
      cname = StringVar()
      cdob = StringVar()
      cfname = StringVar()
      cmname = StringVar()
      ccon = StringVar()
      cage = StringVar()
      cgen = StringVar()
      feedform_fr = Frame(root, width=1250, height=615, bg='#FFF', relief="flat")
      Hr = Frame(feedform_fr, width=1, height=450, bg='#dddddd')
      HrSM = Frame(feedform_fr, width=6, height=1, bg='#dddddd')
      HrS = Frame(feedform_fr, width=1, height=450, bg='#dddddd')
      HrU = Frame(feedform_fr, width=244, height=1, bg='#dddddd')
      HrF = Frame(feedform_fr, width=370, height=1, bg='#dddddd')
      feedform_fr.place(x=10,y=73)    
      Hr.place(x = 30, y = 108)
      HrSM.place(x = 30, y = 108)
      HrS.place(x = 400, y = 108)
      HrU.place(x = 156, y = 108)
      HrF.place(x = 30, y = 557)
      
      Heading = Label(feedform_fr)
      SubHeading = Label(feedform_fr)
      Heading.place(x=40,y=40)
      SubHeading.place(x=40,y=100)
     
      Name = Label(feedform_fr)
      dob = Label(feedform_fr)
      fathnam = Label(feedform_fr)
      mothnam = Label(feedform_fr)
      panno = Label(feedform_fr)
      agelab = Label(feedform_fr)
      genlab = Label(feedform_fr)
      Treelab = Label(feedform_fr)
      
      naen= Entry(feedform_fr,textvariable = cname)
      doben= Entry(feedform_fr,textvariable = cdob)
      fathen= Entry(feedform_fr)
      mothen= Entry(feedform_fr)
      panen= Entry(feedform_fr)
      ageen= Entry(feedform_fr)
   
      
      Heading.configure(text="0-3 Age Child Group Form", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","18","bold"))
      Treelab.configure(text="List Of Child Registered", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","18","bold"))
      SubHeading.configure(text="Fill Details Carefully", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","9","bold"))
      Name.configure(text="Child Name: ", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","10","bold"))
      dob.configure(text="Date Of Birth: ", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","10","bold"))
      fathnam.configure(text="Father Name: ", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","10","bold"))
      mothnam.configure(text="Mother Name: ", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","10","bold"))
      panno.configure(text="Contact:", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","10","bold"))
      agelab.configure(text="Age (Current): ", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","10","bold"))
      genlab.configure(text="Gender: ", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","10","bold"))
     
      naen.configure(relief="flat", bg="#EEE")
      doben.configure(relief="flat", bg="#EEE")
      fathen.configure(textvariable = cfname,relief="flat", bg="#EEE")
      mothen.configure(textvariable = cmname, relief="flat", bg="#EEE")
      panen.configure(textvariable = ccon, relief="flat", bg="#EEE")
      ageen.configure(textvariable = cage, relief="flat", bg="#EEE")
      
      genvar = StringVar()
      ch1 = Radiobutton(feedform_fr, text= "Male", variable=genvar, value="Male")
      ch1.select()
      ch1.place(x = 250, y = 450)
      ch2 = Radiobutton(feedform_fr, text= "Female", variable=genvar, value="Female")
      ch2.deselect()
      ch2.place(x = 310, y = 450)
     
      Name.place(x=40,y=150)
      dob.place(x=40,y=200)
      fathnam.place(x=40,y=250)
      mothnam.place(x=40,y=300)
      panno.place(x=40,y=350)
      agelab.place(x=40,y=400)
      genlab.place(x=40,y=450)
      Treelab.place(x=500, y =40)
     
      naen.place(x = 250, y= 150)
      doben.place(x = 250, y= 200)
      fathen.place(x = 250, y= 250)
      mothen.place(x = 250, y= 300)
      panen.place(x = 250, y= 350)
      ageen.place(x = 250, y= 400)
      
    
      q = StringVar()
      SerchS = Frame(feedform_fr, width=1, height=50, bg='#dddddd')
      SerMS = Frame(feedform_fr, width=320, height=1, bg='#dddddd')
      SerHr = Frame(feedform_fr, width=1, height=50, bg='#dddddd')
      SerHr.place(x = 1210, y = 45)
     
      SerMS.place(x = 890, y = 45)
     
      SerchS.place(x = 890, y = 45)
      Src = Label(feedform_fr)
      Src.configure(text=" Search  ", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","9","bold")) 
      Src.place(x=900, y= 38)
      Srcen = Entry(feedform_fr, textvariable=q)
      Srcen.configure(relief="flat", bg="#EEE", bd=3)
      Srcen.place(x=900, y=60)
      Srcbtn = Button(feedform_fr, command=search)
      Srcbtn.configure(relief="raised", activeforeground="#D2463E", cursor="hand2", height=1, width=8,
      overrelief="flat", foreground="#000", background="#EEE", borderwidth="0", text="Search")
      Srcbtn.place(x=1050, y=60)
      CBtn = Button(feedform_fr, command=clear_src)
      CBtn.configure(relief="raised", activeforeground="#D2463E", cursor="hand2", height=1, width=8,
      overrelief="flat", foreground="#000", background="#EEE", borderwidth="0", text="Clear")
      CBtn.place(x=1130, y = 60)
      
      style = ttk.Style()
      style.theme_use("clam")
      style.configure("mystyle.Treeview", highlightthickness=0, bd=0)
      style.configure("mystyle.Treeview.Heading", font=('Calibri', 18,'bold')) 
      style.configure("Treeview",background="white",foreground="grey",rowheight=25,fieldbackground="#FCFCFC",font=('Calibri', 9,'bold'))
      style.map('Treeview',background=[('selected', 'orange')])
     
      btn = Button(feedform_fr, command=freedform_dbc)
      btnn = Button(feedform_fr, command=destroyer)
      TreeBtnU = Button(feedform_fr, command=update_tree)
      RBtn = Button(feedform_fr, command=clear_src)
      TreeBtnD = Button(feedform_fr, command=delete)
      D4 = Button(feedform_fr, command=root.destroy)
      btn.configure(relief="raised",activeforeground="orange",cursor="hand2",height=1,width=8,overrelief="flat",foreground="#ffffff",background="orange",borderwidth="0",text="ADD", activebackground="#FCFCFC")
      btnn.configure(relief="raised", activeforeground="RED", cursor="hand2", height=1, width=8,overrelief="flat", foreground="#000", background="#EEE", borderwidth="0", text="CLOSE", activebackground="#FCFCFC")
      TreeBtnU.configure(relief="raised", activeforeground="#1E90FF", cursor="hand2", height=1, width=8,overrelief="flat", foreground="#000", background="#EEE", borderwidth="0", text="UPDATE", activebackground="#FCFCFC")
      RBtn.configure(relief="raised", activeforeground="#1E90FF", cursor="hand2", height=1, width=8,overrelief="flat", foreground="#000", background="#EEE", borderwidth="0", text="REFRESH", activebackground="#FCFCFC")
      TreeBtnD.configure(relief="raised", activeforeground="RED", cursor="hand2", height=1, width=8,overrelief="flat", foreground="#000", background="#EEE", borderwidth="0", text="DELETE", activebackground="#FCFCFC")
      
      btn.place(x=500, y= 535)
      btnn.place(x=950, y=535) 
      TreeBtnU.place(x=600, y=535)
      RBtn.place(x=700, y = 535)
      TreeBtnD.place(x=800, y=535)
       
      D4.configure(relief="raised", activeforeground="RED", cursor="hand2", height=1, width=8,overrelief="flat", foreground="#000", background="#EEE", borderwidth="0", text="EXIT", activebackground="#fcfcfc")
      D4.place(x = 1050, y = 534)
      TreeFrame = Frame(root, width=710, height=400, bg='#FFF', relief="flat")
      TreeFrame.place(x= 500, y = 180)
      
      cols = ('Name','D.O.B','Father Name','Mother Name','Contact','Age (Current)','Gender')
      listBox = ttk.Treeview(TreeFrame, columns=cols, show='headings') 
      
      for col in cols :
         listBox.heading(col, text=col)
         listBox.grid(row=1, column=0,columnspan=2)
         listBox.column(col, minwidth=0, width=100,stretch=NO, anchor=W)
         listBox.pack()
      show()
      listBox.bind('<Double-Button-1>', Delete)
  
   
   def feedform_nd():
      def update(rows):
         listBox.delete(*listBox.get_children())
         for i in rows:
            listBox.insert('', 'end', values=i)
      def destroyer():
         feedform_snd.destroy()
         TreeFrame2.destroy()   
      def clear_src():
         try:
            mysqlDb = dbwire.connect(host = "localhost", user="root", password="", database="sac_2045")
            mycursor = mysqlDb.cursor()
         except Exception:
            msalert.showerror("SurveyTarcker", "Connection Failed!")
         Srcen.delete(0, 'end')
         naen.delete(0, 'end')
         doben.delete(0, 'end')
         fathen.delete(0, 'end')
         mothen.delete(0, 'end')
         panen.delete(0, 'end')
         ageen.delete(0, 'end')
         query = "SELECT namedb, dobdb, fnamedb, mnamedb, condb, agedb, gendb From `dat3-6a`"
         mycursor.execute(query)
         rows = mycursor.fetchall()
         update(rows) 
      def Delete(event):
         naen.delete(0, 'end')
         doben.delete(0, 'end')
         fathen.delete(0, 'end')
         mothen.delete(0, 'end')
         panen.delete(0, 'end')
         ageen.delete(0, 'end')
         row_id = listBox.selection()[0]
         select = listBox.set(row_id)
         naen.insert(0,select['Name'])
         doben.insert(0,select['D.O.B']) 
         fathen.insert(0,select['Father Name']) 
         mothen.insert(0,select['Mother Name']) 
         panen.insert(0,select['Contact']) 
         ageen.insert(0,select['Age (Current)'])  
         ge = select['Gender']
         genvar.set(value=ge)
      def delete():
         try:
            child = dbwire.connect(host="localhost", user="root", password="", database="sac_2045")
            cursor = child.cursor()
         except:
            msalert.showerror("SurveyTarcker", "Connection Failed!")
         try:
            f = cname.get()
            if f == "":
               msalert.showinfo("Sorry", "Blanked Not Allowed")  
            else:
               try:
                  sql = "DELETE FROM `dat3-6a` WHERE `namedb`= %s"
                  val = (f, )
                  cursor.execute(sql, val)
                  child.commit()
                  msalert.showinfo("Information from Server: 127.0.0.1", "Record Deleted Successfully...")
                  naen.delete(0, 'end')
                  doben.delete(0, 'end')
                  fathen.delete(0, 'end')
                  mothen.delete(0, 'end')
                  panen.delete(0, 'end')
                  ageen.delete(0, 'end')
                  naen.focus_set()
                  child.close()
                  clear_src()
               except Exception as e:
                  msalert.showerror("Exception", e)
                  child.rollback()
                  child.close()
                  clear_src()
         except Exception as e:
            msalert.showerror("Exception", e)      
      def update_tree():
         g = genvar.get()
         if g== "Male":
            print("male")
            resul = "Male"
         else:
            print("female")
            resul = "Female"
         try:
            child = dbwire.connect(host="localhost", user="root", password="", database="sac_2045")
            cursor = child.cursor()
         except:
            msalert.showerror("Server","Please Ceck Your Connection....  Try Again Later") 
         try:
            f = cname.get()
            f2 = cdob.get()
            f3 = cfname.get()
            f4  = cmname.get()
            f5 = ccon.get()
            f6 = cage.get()
            f7 = resul
            if f == "" or f2 == "" or f3  == "" or f4 == "" or f5 == "" or f6 == "" or f7 == "":
               msalert.showinfo("Sorry", "Blanked Not Allowed")  
            else:
               sql = 'UPDATE `dat3-6a` SET dobdb =%s, fnamedb =%s, mnamedb =%s, condb =%s, agedb =%s, gendb =%s WHERE namedb = %s'
               val = (f2,f3,f4,f5,f6,f7,f)
               cursor.execute(sql, val)
               print(child, cursor, sql, val)
               child.commit()
              
               msalert.showinfo("Server", "Records Updated Successfully.....")
               clear_src()
         except Exception as s:
            print(s)
            naen.delete(0, 'end')
            doben.delete(0, 'end')
            fathen.delete(0, 'end')
            mothen.delete(0, 'end')
            panen.delete(0, 'end')
            ageen.delete(0, 'end')

            F = Label(feedform_fr, text="Something Went Wrong!                       ", height=1, fg="green",
            border=0, bg="#FFF", font=("sans-serif", "9", "bold"))
            F.place(x=40, y=520)
      def show():
         try:
            mysqlDb = dbwire.connect(host = "localhost", user="root", password="", database="sac_2045")
            mycursor = mysqlDb.cursor()
         except Exception as E:
            print(E)
            msalert.showerror("Server 'List Not Fetch'","Please Ceck Your Connection....  Try Again Later") 
         mycursor.execute("SELECT `namedb`, `dobdb`, `fnamedb`, `mnamedb`, `condb`, `agedb`, `gendb` FROM `dat3-6a`")
         records = mycursor.fetchall() 
         print(records)
         for i, (namedb,dobdb,fnamedb,mnamedb, condb,agedb,gendb) in enumerate(records, start=1):
            listBox.insert("", "end", values=(namedb,dobdb,fnamedb,mnamedb, condb,agedb,gendb))
            mysqlDb.close()
      def search():
         try:
            mysqlDb = dbwire.connect(host = "localhost", user="root", password="", database="sac_2045")
            mycursor = mysqlDb.cursor()
         except Exception:
            msalert.showerror("SurveyTarcker", "Connection Failed!")
         q2 = q.get()
         query = "SELECT namedb, dobdb, fnamedb, mnamedb, condb, agedb, gendb FROM `dat3-6a` WHERE `namedb` LIKE '%"+q2+"%' OR `dobdb` LIKE '%"+q2+"%' OR `fnamedb` LIKE '%"+q2+"%' OR `mnamedb` LIKE '%"+q2+"%' OR `agedb` LIKE '%"+q2+"%' OR `condb` LIKE '%"+q2+"%' OR `gendb` LIKE '%"+q2+"%'"
         mycursor.execute(query)
         rows = mycursor.fetchall()
         update(rows) 
     
   
      global cname, cdob, cfname, cmname, ccon, cage, cgen
      global feedform_snd, TreeFrame2
      global naen, doben, fathen, mothen, panen, ageen
      global q
      global genvar, listBox, Srcen
      
      cname = StringVar()
      cdob = StringVar()
      cfname = StringVar()
      cmname = StringVar()
      ccon = StringVar()
      cage = StringVar()
      cgen = StringVar()
      
    
      feedform_snd = Frame(root, width=1250, height=615, bg='#FFF', relief="flat")
      Hr = Frame(feedform_snd, width=1, height=450, bg='#dddddd')
      HrSM = Frame(feedform_snd, width=6, height=1, bg='#dddddd')
      HrS = Frame(feedform_snd, width=1, height=450, bg='#dddddd')
      HrU = Frame(feedform_snd, width=244, height=1, bg='#dddddd')
      HrF = Frame(feedform_snd, width=370, height=1, bg='#dddddd')
      
      feedform_snd.place(x=10,y=73)    
      Hr.place(x = 30, y = 108)
      HrSM.place(x = 30, y = 108)
      HrS.place(x = 400, y = 108)
      HrU.place(x = 156, y = 108)
      HrF.place(x = 30, y = 557)
     
      Heading = Label(feedform_snd)
      SubHeading = Label(feedform_snd)
      Heading.place(x=40,y=40)
      SubHeading.place(x=40,y=100)
      
      Name = Label(feedform_snd)
      dob = Label(feedform_snd)
      fathnam = Label(feedform_snd)
      mothnam = Label(feedform_snd)
      panno = Label(feedform_snd)
      agelab = Label(feedform_snd)
      genlab = Label(feedform_snd)
      Treelab = Label(feedform_snd)
   
      naen= Entry(feedform_snd,textvariable = cname)
      doben= Entry(feedform_snd,textvariable = cdob)
      fathen= Entry(feedform_snd)
      mothen= Entry(feedform_snd)
      panen= Entry(feedform_snd)
      ageen= Entry(feedform_snd)
     
      Heading.configure(text="3-6 Age Child Group Form", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","18","bold"))
      Treelab.configure(text="List Of Child Registered", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","18","bold"))
      SubHeading.configure(text="Fill Details Carefully", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","9","bold"))
      Name.configure(text="Child Name: ", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","10","bold"))
      dob.configure(text="Date Of Birth: ", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","10","bold"))
      fathnam.configure(text="Father Name: ", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","10","bold"))
      mothnam.configure(text="Mother Name: ", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","10","bold"))
      panno.configure(text="Contact:", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","10","bold"))
      agelab.configure(text="Age (Current): ", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","10","bold"))
      genlab.configure(text="Gender: ", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","10","bold"))
     
      naen.configure(relief="flat", bg="#EEE")
      doben.configure(relief="flat", bg="#EEE")
      fathen.configure(textvariable = cfname,relief="flat", bg="#EEE")
      mothen.configure(textvariable = cmname, relief="flat", bg="#EEE")
      panen.configure(textvariable = ccon, relief="flat", bg="#EEE")
      ageen.configure(textvariable = cage, relief="flat", bg="#EEE")
     
      genvar = StringVar()
      ch1 = Radiobutton(feedform_snd, text= "Male", variable=genvar, value="Male")
      ch1.select()
      ch1.place(x = 250, y = 450)
      ch2 = Radiobutton(feedform_snd, text= "Female", variable=genvar, value="Female")
      ch2.deselect()
      ch2.place(x = 310, y = 450)
     
      Name.place(x=40,y=150)
      dob.place(x=40,y=200)
      fathnam.place(x=40,y=250)
      mothnam.place(x=40,y=300)
      panno.place(x=40,y=350)
      agelab.place(x=40,y=400)
      genlab.place(x=40,y=450)
      Treelab.place(x=500, y =40)
     
      naen.place(x = 250, y= 150)
      doben.place(x = 250, y= 200)
      fathen.place(x = 250, y= 250)
      mothen.place(x = 250, y= 300)
      panen.place(x = 250, y= 350)
      ageen.place(x = 250, y= 400)
    
      q = StringVar()
      SerchS = Frame(feedform_snd, width=1, height=50, bg='#dddddd')
      SerMS = Frame(feedform_snd, width=320, height=1, bg='#dddddd')
      SerHr = Frame(feedform_snd, width=1, height=50, bg='#dddddd')
      SerHr.place(x = 1210, y = 45)
     
      SerMS.place(x = 890, y = 45)
     
      SerchS.place(x = 890, y = 45)
      Src = Label(feedform_snd)
      Src.configure(text=" Search  ", height=1, fg="black", border=0, bg="#FFF", font=("sans-serif","9","bold")) 
      Src.place(x=900, y= 38)
      Srcen = Entry(feedform_snd, textvariable=q)
      Srcen.configure(relief="flat", bg="#EEE", bd=3)
      Srcen.place(x=900, y=60)
      Srcbtn = Button(feedform_snd, command=search)
      Srcbtn.configure(relief="raised", activeforeground="#D2463E", cursor="hand2", height=1, width=8,
      overrelief="flat", foreground="#000", background="#EEE", borderwidth="0", text="Search")
      Srcbtn.place(x=1050, y=60)
      CBtn = Button(feedform_snd, command=clear_src)
      CBtn.configure(relief="raised", activeforeground="#D2463E", cursor="hand2", height=1, width=8,
      overrelief="flat", foreground="#000", background="#EEE", borderwidth="0", text="Clear")
      CBtn.place(x=1130, y = 60)
      
      style = ttk.Style()
      style.theme_use("clam")
      style.configure("mystyle.Treeview", highlightthickness=0, bd=0)
      style.configure("mystyle.Treeview.Heading", font=('Calibri', 18,'bold')) 
      style.configure("Treeview",background="white",foreground="grey",rowheight=25,fieldbackground="#FCFCFC",font=('Calibri', 9,'bold'))
      style.map('Treeview',background=[('selected', 'orange')])
      
      btn = Button(feedform_snd, command=feedform_dbc)
      btnn = Button(feedform_snd, command=destroyer)
      TreeBtnU = Button(feedform_snd, command=update_tree)
      RBtn = Button(feedform_snd, command=clear_src)
      TreeBtnD = Button(feedform_snd, command=delete)
      D4 = Button(feedform_snd, command=root.destroy)
      btn.configure(relief="raised",cursor="hand2",height=1,width=8,overrelief="flat",foreground="#ffffff",background="#4169E1",borderwidth="0",text="ADD", activebackground="#FCFCFC", activeforeground="#1E90FF")
      btnn.configure(relief="raised", activeforeground="RED", cursor="hand2", height=1, width=8,overrelief="flat", foreground="#000", background="#EEE", borderwidth="0", text="CLOSE", activebackground="#FCFCFC")
      TreeBtnU.configure(relief="raised", activeforeground="#1E90FF", cursor="hand2", height=1, width=8,overrelief="flat", foreground="#000", background="#EEE", borderwidth="0", text="UPDATE", activebackground="#FCFCFC")
      RBtn.configure(relief="raised", activeforeground="#1E90FF", cursor="hand2", height=1, width=8,overrelief="flat", foreground="#000", background="#EEE", borderwidth="0", text="REFRESH", activebackground="#FCFCFC")
      TreeBtnD.configure(relief="raised", activeforeground="RED", cursor="hand2", height=1, width=8,overrelief="flat", foreground="#000", background="#EEE", borderwidth="0", text="DELETE", activebackground="#FCFCFC")
      D4.configure(relief="raised", activeforeground="RED", cursor="hand2", height=1, width=8,overrelief="flat", foreground="#000", background="#EEE", borderwidth="0", text="EXIT", activebackground="#FCFCFC")
      
      btn.place(x=500, y= 535)
      btnn.place(x=950, y=535) 
      TreeBtnU.place(x=600, y=535)
      RBtn.place(x=700, y = 535)
      TreeBtnD.place(x=800, y=535)
      D4.place(x = 1050, y = 534)
      
      TreeFrame2 = Frame(root, width=710, height=400, bg='#FFF', relief="flat")
      TreeFrame2.place(x= 500, y = 180)
      
      cols = ('Name','D.O.B','Father Name','Mother Name','Contact','Age (Current)','Gender')
      listBox = ttk.Treeview(TreeFrame2, columns=cols, show='headings') 
      
      for col in cols :
         listBox.heading(col, text=col)
         listBox.grid(row=1, column=0,columnspan=2)
         listBox.column(col, minwidth=0, width=100,stretch=NO, anchor=W)
         listBox.pack()
      show()
      listBox.bind('<Double-Button-1>', Delete)
    
   def about():
      msalert.showinfo("About Us", 
                       """ ***************************************************************
   Application:
   
         Version: 0.1
         Name: SurveyTracker
         Release Date: 28 August 2022
         Server Port: 3306 [MySQL]
         
*** Thanks For Using Our Services ***
               
   Contact:
   
         Developer: Sarwan Yadav
         Gmail: rangersarwan@gmail.com
         Phone Number : +91 8960446756
         Github: @ranger404x
*************************************************************** """) 
         
   root = Tk()
   root.title("Dashboard")
   root.geometry("1280x720")
   #root.resizable(False, False)
   rootFrame = Frame(root, width=1366, height=60, background='#fbfcfc')
   rootFrame.place(x = 0, y = 0) 
   Footer = Frame(root, width = 1366, height=70, bg='#ffffff')
   Footer.place(x = 0, y = 700) 
   Hrt = Frame(root, width=1366, height=1, bg='grey')
   Hr = Frame(root, width=1366, height=1, bg='#dddddd')
 
   
   Hrt.place(x = 0, y = 1)
   Hr.place(x = 0, y = 60)

   Fe1 = Label()
   Fe2 = Button(rootFrame, command=feedform_)
   Fe3 = Button(rootFrame, command=feedform_nd)
   Fe4 = Button(rootFrame, command=calcage)
   Fe5 = Button(rootFrame, command=about)
   HrF = Frame(root, width=1366, height=1, bg='#dddddd')
   HrF.place(x = 0, y = 700)  
    
   Fe1.configure(text="SurveyTracker", height=2, width=20, fg="#1E90FF", border=0, bg="#fbfcfc", font=("","13","bold"))
   Fe2.configure(text="Age Group Ist", width=20, height=2, fg='#000000', border=0, overrelief="flat", bg='#ffffff', activeforeground='#ffffff', activebackground='#000000')
   Fe3.configure(text="Age Group IInd", width=20, height=2, fg='black', border=0, overrelief="flat", bg='white', activeforeground='white', activebackground='black')
   Fe4.configure(text="Age Calculator", width=20, height=2, fg='black', border=0, overrelief="flat", bg='white', activeforeground='white', activebackground='black')
   Fe5.configure(text="About Us", width=20, height=2, fg='black', border=0, overrelief="flat", bg='white', activeforeground='white', activebackground='black')
   Fe1.place(x = 15, y = 10)
   Fe2.place(x = 200, y = 10)
   Fe3.place(x = 350, y = 10)
   Fe4.place(x = 500, y = 10)
   Fe5.place(x = 650, y = 10)
   mainloop()
feedbase()
