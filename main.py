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



root = Tk()
root.title("SOPO Sign In") #this is where the name on top of the window goes

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row = 0, sticky =(N, W, E, S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight=1)


name = StringVar()
purpose = StringVar()
purpose.set("use")
email = StringVar()

name_entry = ttk.Entry(mainframe, width=7, textvariable=name)
name_entry.grid(column=2, row=2, sticky=(W, E))


#ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Sign In", command=submit).grid(column=2, row=7, sticky=W)

ttk.Label(mainframe, text="Please sign in below whenever you visit SOPO").grid(column=1, row=1, sticky=W, columnspan=4)
ttk.Label(mainframe, text="Name: ").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="What is your main reason for coming today?").grid(column=1, row=3, sticky=W, columnspan=4)
repair = ttk.Radiobutton(mainframe, text='Repairing my bike', variable=purpose, value='use').grid(column=1, row=4)
donate = ttk.Radiobutton(mainframe, text='Dropping off donation', variable=purpose, value='donate').grid(column=2, row=4)
volunteer = ttk.Radiobutton(mainframe, text='Volunteering', variable=purpose, value='volunteer').grid(column=3, row=4)
other = ttk.Radiobutton(mainframe, text='Other', variable=purpose, value='other').grid(column=4, row=4)
ttk.Label(mainframe, text="If you want to be added to our monthly email, give us information below!").grid(column=1, row=5, sticky=W, columnspan=4)
ttk.Label(mainframe, text="Email: ").grid(column=1, row=6, sticky=E)
email_entry = ttk.Entry(mainframe, width=7, textvariable=email)
email_entry.grid(column=2, row=6, sticky=(W, E))

#ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

name_entry.focus()
root.bind('<Return>', submit)

root.mainloop()