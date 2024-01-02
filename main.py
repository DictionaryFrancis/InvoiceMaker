import customtkinter
from customtkinter import *

app = CTk()
app.geometry("500x400")


# Bill to
optionA = {
    "company_name": "A",
    "comapny_address": "2 Douglas Street",
    "company_number": "083XXXXXXX",
    "company_VAT": "XXXXXXX-XX"
}

optionB = {
    "company_name": "B",
    "comapny_address": "10 Tuckey Street",
    "company_number": "083XXXXXXX",
    "company_VAT": "XXXXXXX-XX"
}
#

options = CTkComboBox(master=app, values=["Company A", "Company B"])
options.place(relx=0.2, rely=0.3, anchor="center")

# Btn

def handle_option():
    company_choose = options.get()
    if company_choose == "Company A":
        print(optionA)
    elif company_choose == "Company B":
        print(optionB)

btn_option = CTkButton(master=app,text="Submit", corner_radius=32,command=handle_option)
btn_option.place(relx=0.2, rely=0.4, anchor="center")

app.mainloop()
