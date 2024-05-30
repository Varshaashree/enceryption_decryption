from tkinter import *
from tkinter import messagebox
import base64
import os
def decrypt():
     password=code.get()
     if password=='1234':
        screen2=Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#008000")
        message=text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")
        Label(screen2,text="decrypt",font="arial",highlightbackground="#008000").place(x=10,y=0)
        text2=Text(screen2,font="arial 14",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=300,height=150)
        text2.insert(END,decrypt)
     elif password=="":
        messagebox.showerror("Decryption","InputPassword")
     elif password !="1234":
        messagebox.showerror("Decryption","Invalid Password")
def encrypt():
    password=code.get()
    if password=='1234':
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")
        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")
        Label(screen1,text="Encrypt",font="arial",highlightbackground="#ed3833").place(x=10,y=0)
        text2=Text(screen1,font="arial 14",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=300,height=150)
        text2.insert(END,encrypt)
    elif password=="":
        messagebox.showerror("Encryption","InputPassword")
    elif password !="1234":
        messagebox.showerror("Encryption","Invalid Password")
        
    
def main_screen():
    global screen
    global code
    global text1
    screen=Tk()
    screen.geometry('375x398')
    screen.title("Encrypt & Decrypt")
    def reset():
        code.set("")
        text1.delete(1.0,END)
    Label(text="Enter text for encryption and decryption",fg="black",font=("calbri",13)).place(x=10,y=10)
    text1=Text(font=("Times new roman",16),bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)
    Label(text="Enter secret key for encryption and decryption",fg="black",font=("calbri",13)).place(x=10,y=170)
    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("Times new roman",16),show="*").place(x=10,y=200)
    Button(text="Encrypt",height="2",width=23,bg="#ed3833",fg="White",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="Decrypt",height="2",width=23,bg="#008000",fg="White",bd=0,command=decrypt).place(x=200,y=250)
    Button(text="RESET",height="2",width=50,bg="#0000FF",fg="White",bd=0,command=reset).place(x=10,y=300)
    
    
    screen.mainloop()
main_screen()
