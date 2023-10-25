from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password ():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_text.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save ():
    websight_name= name_web.get()
    email = name_text.get()
    passwords= pass_text.get()

    if len(websight_name)==0 or len(email)==0 or len(passwords)==0 :
        messagebox.showerror(title="Oops",message="Pleas don't leave any field empty ! ")
    else :
        is_ok= messagebox.askokcancel(title = websight_name, message=f"These are the details entered : \nEmail : {email}\nPassword : {passwords} \nIs it ok to save ?")
        if is_ok :
            with open("data.txt", "a") as data_file:
                data_file.write(f"{websight_name} | {email}  | {passwords }\n")
                name_web.delete(0,END)
                pass_text.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(width=400,height=400,pady=50,padx=50)

canvas = Canvas(width=200,height=200)
lock_image= PhotoImage(file="logo.png")
canvas.create_image(100,100,image= lock_image)
canvas.grid(row=0,column=1)

websight= Label(text="Websight ")
websight.grid(row=1,column=0)

name_web= Entry(width=50)
name_web.focus()
name_web.grid(row=1,column=1,columnspan=2)
name= Label(text="Email/Username ")
name.grid(row=2,column=0)

name_text= Entry(width=50)
name_text.insert(0,"ishankhekre123456@gmail.com")
name_text.grid(row=2,column=1,columnspan=2)

password = Label(text="Password")
password.grid(row=3,column=0)

pass_text = Entry(width=33)
pass_text.grid(row=3,column=1)

gen_pass = Button(text="Generat Password", command=generate_password)
gen_pass.grid(row=3,column=2)

add= Button(text="Add",width=43, command=save)
add.grid(row=4,column=1,columnspan=2)








window.mainloop()