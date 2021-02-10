#importing necessay module
from tkinter import *
from tkinter import messagebox

#creating funtion to store data in textfile
def submit():
    with open("record.txt",'a') as f:
        f.write(f"{name.get(),age.get(),gender.get(),DanceForm.get(),school.get(),DOA.get()}\n")

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
DOA=StringVar()

#setting the logo 
root.iconbitmap('icon.ico')

#setting the default size and title
root.geometry("700x600")
root.title("Dance Class Management Software")

#adding the title "Juyal dance Academey"
Label(text="Juyal Dance Academey",bg="black",fg="white",font=('Times',25),relief=GROOVE).pack(pady=30)

#adding different column for entering details
Label(text="Name",font=('Arial',18)).place(x=20,y=120)
Label(text="Age",font=('Arial',18)).place(x=20,y=170)
Label(text="Gender",font=('Arial',18)).place(x=20,y=220)
Label(text="Dance Form",font=('Arial',18)).place(x=20,y=270)
Label(text="School",font=('Arial',18)).place(x=20,y=320)
Label(text="Date of Admission",font=('Arial',18)).place(x=20,y=370)

#creating entry widget for accepting values
Entry(root,textvariable=name,font=("Arial",18)).place(x=300,y=120)
Entry(root,textvariable=age,font=("Arial",18)).place(x=300,y=170)
Entry(root,textvariable=DanceForm,font=("Arial",18)).place(x=300,y=270)
Entry(root,textvariable=school,font=("Arial",18)).place(x=300,y=320)
Entry(root,textvariable=DOA,font=("Arial",18)).place(x=300,y=370)

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