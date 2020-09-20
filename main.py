from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# import pandas
from datetime import datetime
import csv

fileName = "data.csv" #make sure there's a txt file called data.txt in the same folder as this program)


# def submit(*args): #this is the function that takes all the submitted data and slips it into the csv file
#     fullname = name.get()
#     reason = purpose.get()
#     now = datetime.now()
#     timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
#     d={'names': [fullname], "reasons": [reason], "timestamp": [timestamp]}
#     df = pandas.DataFrame(data =d)
#     df.to_csv(fileName, mode='a', header=False)
#    # print(df)
#     messagebox.showinfo(message='You\'ve been signed in!' )

def submit(*args): #this is the function that takes all the submitted data and slips it into the csv file
    fullname = name.get()
    fullemail = email.get()
    reason = purpose.get()
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
    dat=[" " + fullname, " " +  reason, " " + fullemail, " " +  timestamp]
    with open('data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(dat)
    name_entry.delete(first=0, last=100)
    email_entry.delete(first=0, last=100)
    messagebox.showinfo(message='You\'ve been signed in!' )

    
    # df = pandas.DataFrame(data =d)
    # df.to_csv(fileName, mode='a', header=False)
   # print(df)

def checkInfo(): #checks if they've signed in before
    #
    #code to check if they've signe din before, and set previous to "true" or "False"
    previous = True
    if previous:
        confirmSignIn()
    else:
        getInfo()


def confirmSignIn(): #if their ID number is in the DB then it gives them the info to confirm 
    confirm=Toplevel()
    lbl = Label(confirm, text="If your ID Number is the following press confirm").pack()
    lbl = Label(confirm, text=idNumberEntry).pack()
    closebtn = Button(confirm, text="the info is correct", command=confirm.destroy).pack()


def getInfo(): #if their ID number is not in the DB then it asks for the info we want   
    getInfo=Toplevel()
    lbl = Label(getInfo, text="from getInfo the secon dwindow").pack()



root = Tk()
root.title("Fixie Sign In") #this is where the name on top of the window goes


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row = 0, sticky =(N, W, E, S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight=1)

idNumberEntry = StringVar
idNumber = IntVar #i'm guessing I may need to do some cleanup of the ID number before submitting it.


ttk.Label(mainframe, text="Please swipe your card").grid(column=1, row=1, sticky=W, columnspan=4)



id_entry = ttk.Entry(mainframe, width=7, textvariable=idNumberEntry)
id_entry.grid(column=2, row=2, sticky=(W, E))

#https://stackoverflow.com/questions/19148242/tkinter-entry-widget-is-detecting-input-text-possible on ID number




ttk.Button(root, text="Sign In", command=checkInfo).grid(column=2, row=7, sticky=W)




mainloop()


# root = Tk()
# root.title("SOPO Sign In") #this is where the name on top of the window goes

# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row = 0, sticky =(N, W, E, S))
# root.columnconfigure(0, weight = 1)
# root.rowconfigure(0, weight=1)


# name = StringVar()
# purpose = StringVar()
# purpose.set("use")
# email = StringVar()

# name_entry = ttk.Entry(mainframe, width=7, textvariable=name)
# name_entry.grid(column=2, row=2, sticky=(W, E))


# #ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
# ttk.Button(mainframe, text="Sign In", command=submit).grid(column=2, row=7, sticky=W)

# ttk.Label(mainframe, text="Please sign in below whenever you visit SOPO").grid(column=1, row=1, sticky=W, columnspan=4)
# ttk.Label(mainframe, text="Name: ").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="What is your main reason for coming today?").grid(column=1, row=3, sticky=W, columnspan=4)
# repair = ttk.Radiobutton(mainframe, text='Repairing my bike', variable=purpose, value='use').grid(column=1, row=4)
# donate = ttk.Radiobutton(mainframe, text='Dropping off donation', variable=purpose, value='donate').grid(column=2, row=4)
# volunteer = ttk.Radiobutton(mainframe, text='Volunteering', variable=purpose, value='volunteer').grid(column=3, row=4)
# other = ttk.Radiobutton(mainframe, text='Other', variable=purpose, value='other').grid(column=4, row=4)
# ttk.Label(mainframe, text="If you want to be added to our monthly email, give us information below!").grid(column=1, row=5, sticky=W, columnspan=4)
# ttk.Label(mainframe, text="Email: ").grid(column=1, row=6, sticky=E)
# email_entry = ttk.Entry(mainframe, width=7, textvariable=email)
# email_entry.grid(column=2, row=6, sticky=(W, E))

# #ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)


# for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# name_entry.focus()
# root.bind('<Return>', submit)

# root.mainloop()