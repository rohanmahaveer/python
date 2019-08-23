from tkinter import *
def click():
    weight=int(textentry.get())
    height=int(textentry1.get())
    bmi=(weight)/(height*height)
    output.set("Your BMI is %.2f" % bmi)
window =Tk()
window.title(" MY FIRST GUI")
window.configure(background="yellow")

Label (window,text="TO CALCULATE YOUR BMI ",fg="black",bg="yellow") .grid(row=100, column=200)
Label (window,text="weight ",fg="black",bg="yellow") .grid(row=300, column=200)
textentry =Entry(window,width=20,bg="white")
textentry.grid(row=500, column=200)
Label (window,text=" height ",fg="black",bg="yellow") .grid(row=600, column=200)
textentry1 =Entry(window,width=20,bg="white")
textentry1.grid(row=800, column=200)
Button(window,text="SUBMIT",bg="red",width=6,command=click) .grid(row=1000,column=200)
textentry2 =Entry(window,width=20,bg="white")
textentry2.grid(row=800, column=200)
Label (window,text=" answer ",fg="black",bg="yellow") .grid(row=1200, column=200)
output=Text(window,bg="white")
output.grid(row=1400,column=200)

window.mainloop()

