#importing necessay module
from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import datetime

#connecting mysql databasse
mydb=mysql.connector.connect(host="localhost",user="root",password="root123",database="personal")
mycursor=mydb.cursor()



#creating funtion to store data in database
def submit():
    
    #table name is ABC_Dance 
    sql="INSERT INTO ABC_Dance (name,age,gender,DanceForm,school) VALUES (%s,%s,%s,%s,%s) "
    val=(name.get(),age.get(),gender.get(),DanceForm.get(),school.get())
    mycursor.execute(sql,val)

    mydb.commit()

    #displaying thanku message
    messagebox.showinfo("Thanks..","Your records have been submitted")
    quit()



#GUI iterferance
root=Tk()

#initializing variables(DOA=Date Of Admission)
name=StringVar()
age=StringVar()
gender=StringVar()
DanceForm=StringVar()
school=StringVar()


#setting the logo 
root.iconbitmap('icon.ico')

#setting the default size and title
root.geometry("700x600")
root.title("Dance Class Management Software")

#adding the title "Juyal dance Academey"
Label(text="ABC Dance Academey",bg="black",fg="white",font=('Times',25),relief=GROOVE).pack(pady=30)

#adding different column for entering details
Label(text="Name",font=('Arial',18)).place(x=20,y=120)
Label(text="Age",font=('Arial',18)).place(x=20,y=170)
Label(text="Gender",font=('Arial',18)).place(x=20,y=220)
Label(text="Dance Form",font=('Arial',18)).place(x=20,y=270)
Label(text="School",font=('Arial',18)).place(x=20,y=320)

#creating entry widget for accepting values
Entry(root,textvariable=name,font=("Arial",18)).place(x=300,y=120)
Entry(root,textvariable=age,font=("Arial",18)).place(x=300,y=170)
Entry(root,textvariable=DanceForm,font=("Arial",18)).place(x=300,y=270)
Entry(root,textvariable=school,font=("Arial",18)).place(x=300,y=320)


#creating radiobutton for gender
Radiobutton(root,text="Male",variable=gender,value="M",font=("Arial",18)).place(x=300,y=220)
Radiobutton(root,text="Female",variable=gender,value="F",font=("Arial",18)).place(x=400,y=220)


#creating agreement button
Checkbutton(root,text="I accept the terms and policies of the academy.",font=("Arial",15)).place(x=200,y=450)

#creating button to store data
Button(text="Submit",command=submit,font=("Arial",20),bd=4,relief=RAISED).pack(side=BOTTOM,pady=25)



#giving credits
Label(text="By : Mayank Kumar Gupta 12 'D'",font=("Arial",12)).place(x=450,y=550)
 
#end the code here
root.mainloop()
