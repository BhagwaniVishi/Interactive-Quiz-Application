#Designing Question Frame - I'll insert only Question, Category and option1
#Similarly you add more fields
#Step 1: Perform necessary imports
from tkinter import *
from tkinter import messagebox
import mysql.connector as my #aliasing
import dbconfig #as created on 27-Jul
import sys


#Step 2 : Obtain database connection
mydb=None #Empty variable
try:
 mydb = my.connect(**dbconfig.config) #Concept of dictionary unpack
except Exception as ex:
 messagebox.showinfo('Database Exception' , str(ex))
 sys.exit(0) #Terminate Program
#Step 3: Create cursor - to execute sql query
cursor=mydb.cursor(dictionary=True)
#Step 4. Create Tk() object
win=Tk()
win.geometry('400x300')
win.title('Questions Frame-By Ajay')
#Step 5. Define some bind variables to link with ui
qid=IntVar()
question=StringVar()
category=StringVar()
option1=StringVar()
#option2=StringVar()
#option3=StringVar()
#option4=StringVar()
#answer=StringVar()
#Step 6. Event Handler Fn
def addClick():
 pass #Do nothing
def editClick():
 pass #Do nothing
def saveClick():
 pass
def deleteClick():
 pass
def navigationClick():
 pass
#Step 7. Design UI
#Creating object with variable is known as 'Anonymous Object'
Label(win, text="Qid:" ).grid(row=0, column=0)
txtQid=Entry(win, width='10',textvariable=qid, state='readonly')
txtQid.grid(row=0, column=1, padx='10' ,pady='10')
btnAdd=Button(win, width='10', text='Add', command=addClick)
btnAdd.grid(row=0, column=2)
Label(win, text="Question").grid(row=1, column=0)
txtQuestion=Entry(win,width='10', textvariable=question, state='readonly')
txtQuestion.grid(row=1, column=1)
btnEdit=Button(win, width='10', text='Edit', command=editClick)
btnEdit.grid(row=1, column=2)


Label(win, text="Category:").grid(row=2, column=0)
txtCategory=Entry(win, width='10', textvariable=category, state='readonly')
txtCategory.grid(row=2, column=1)
btnSave=Button(win, width='10' ,text='Save', command=saveClick)
btnSave.grid(row=2, column=2)

Label(win, text="Option1:").grid(row=3, column=0)
txtOption1=Entry(win, width='10', textvariable=option1, state='readonly')
txtOption1.grid(row=3, column=1)
btnDelete=Button(win, width='10', text='Delete', command=deleteClick)
btnDelete.grid(row=3, column=2)
btn=Button(win ,text='First', width='10', command=navigationClick)
btn.grid(row=4 , column=0)
btn=Button(win ,text='Previous', width='10', command=navigationClick)
btn.grid(row=4, column=1)
btn=Button(win ,text='Next', width='10', command=navigationClick)
btn.grid(row=5 , column=0)
btn=Button(win ,text='Last', width='10', command=navigationClick)
btn.grid(row=5 , column=1)
win.mainloop()
