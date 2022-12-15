#!/usr/bin/python3
import random
import pyperclip as pc
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import tkinter as tk

root = tk.Tk()
#root.geometry('250x120')
root.title('Strongth Password Generator')
leng = tk.StringVar()
characteres = "#0a*G1bH2cI3dJ4eK5fL:6gM7hN8iO9jP=kQ¿lR?mS(nT)oU[pV]qW{rX}sY+tZ-u_v.w,x<y>z@A$;B€C^D!E¡F'"

class Content:
    def __init__(self, leng):

        tk.Label(root, text="Enter Password Length: \n Is recomended to use more than 10 characteres").pack()

        entry = tk.Frame(root)
        entry.pack(padx=10,pady=10,expand=True)

        label_entry = tk.Entry(entry, textvariable=leng)
        label_entry.pack(fill='x', expand=True)
        label_entry.focus()


        test = tk.Label(root, text=leng.get())
        
        button2 = tk.Button(root,text="[ -Countinue- ]",command=Content.feedback)
        button2.pack()

        button = tk.Button(root,text="[!] Exit",command=root.destroy)
        button.pack()
        
        #self.leng = leng.get()
    def feedback():
        Password = ""
        try:
           
            for i in range(int(leng.get())):
                Password = characteres[random.randrange(0,len(characteres))] + Password

            msg = f'Password Generated: {Password} \n [i] With a length of {leng.get()} \n\n [i] Click "OK" to copy it!!'
            showinfo(
                    title='Password Generated',
                    message=msg
                    )
            pc.copy(Password)
           
        except:
            msg = f'Use a valid input as integers, not "{leng.get()}"'
            showinfo(
                    title='User Error!',
                    message=msg
                    )

obj = Content(leng)

root.mainloop()

