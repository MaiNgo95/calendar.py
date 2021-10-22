from tkinter import *
from tkcalendar import *
root = Tk()
root.iconbitmap('MaiNgoCalendar')
root.title("MaiNGoCalendar")
root.geometry("600x600")

cal = Calendar(root, selectmode ="day", year= 2020, month=5,day=22)
cal.pack(pady=20)
# make a function to choose the date
def grab_date():
    label.config(text=cal.get_date())

mybutton = Button(root, text="take note", command = grab_date)
mybutton.pack(pady=20)

label = Label(root, text='')
label.pack(pady=20)
root.mainloop()
