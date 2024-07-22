import tkinter as tk
import requests
from tkinter import*
import json

root=tk.Tk()

def get_insult():
    try:
        response=requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
        content=json.loads(response.content)
        insult=content['insult']
        insult_label=Label(text=insult,padx=20,pady=20)
        insult_label.grid(row=0)
        Button(text='Get another one',padx=20,pady=10,width=40,command=lambda:get_new_insult(insult_label)).grid(row=1)

    except Exception as err:
        Label(text='Error connecting to internet, try again later...',width=100,padx=20,pady=40).pack()



def get_new_insult(insult_label):
  insult_label.config(text='')
  get_insult()

get_insult()

root.mainloop()