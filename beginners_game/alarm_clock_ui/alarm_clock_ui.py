from tkinter import *
import time
import tkinter.font as tk_font
root = Tk()

helv = tk_font.Font(family="Helvetica",size=20,weight="bold")
font_arial = tk_font.Font(family='Arial', size=24, weight='normal', slant='italic', underline=1)


root.title("Alarm Clock UI")

root.geometry("500x250")
frame = Frame(root)
frame.pack()

label = Label(frame, text="Alarm Clock", font=font_arial)
label.pack()

labelDate = Label(frame, justify=CENTER, font=helv)
labelDate.pack(padx=3, pady=10)

def clock():
    date = time.localtime()
    dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "saturday", 6: "Sunday"}
    timeFormatted = f"{dict.get(date[6])} / {date[1]} / {date[0]} , {date[3]}:{date[4]}:{date[5]}"
    labelDate.config(text=timeFormatted)
    root.after(1000, clock)

clock()

root.mainloop()