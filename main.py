import customtkinter
from tkinter import *
import ttkbootstrap as tb
from customtkinter import *
from datetime import date
from tkinter import ttk
from ttkbootstrap.dialogs import Querybox
import mysql.connector

# MySQL Adjust


# Connect to MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="@Tragom22",
    database="testdatabase"
)

mycursor = connection.cursor()

# # If you want to add new person
# while True: # True to create an infinite loop
#     add_new_person = str(input("Add new person (yes/no) >>"))
#     if add_new_person == "yes":
#         # Insert data into the table
#         insert_data_query = "INSERT INTO new_table (company_name, company_address, company_number, company_VAT) VALUES (%s, %s)"
#         person_name = input("Enter person's name: ")
#         person_age = int(input("Enter person's age: "))
#         user_data = (person_name, person_age)
#
#         mycursor.execute(insert_data_query, user_data)
#     elif add_new_person == "no":
#         break

# Commit the changes
connection.commit()

# Select data from the table
select_data_query = "SELECT * FROM new_table"
mycursor.execute(select_data_query)

# Fetch the results
results = mycursor.fetchall()



# Close the cursor and connection
mycursor.close()
connection.close()

# Finish MySQL


# App config
app = CTk()
app.geometry("800x500")
app.title("Invoice Maker!")

# Date
my_date = tb.DateEntry(app, bootstyle="dark", firstweekday=0, startdate=date.today())
my_date.place(x=-10, y=-50)

#

# Bill to
options_dict = {}
len_in_options_dic = 0

for row in results:
    person_id = row[0]
    option = {
        "company_name": row[1],
        "company_address": row[2],
        "company_number": row[3],
        "company_VAT": row[4]
    }

    if person_id not in options_dict:
        options_dict[person_id] = {}

    options_dict[person_id].update({"options": option})

    len_in_options_dic = len(options_dict)

print(len_in_options_dic)



# Build a Table
game_frame = Frame(app)
game_frame.pack()



my_game = ttk.Treeview(game_frame)

my_game['columns'] = ("company_name", "company_address", "company_number","company_VAT")

my_game.column("#0", width=0, stretch=NO)
my_game.column("company_name", anchor=CENTER, width=130)
my_game.column("company_address", anchor=CENTER, width=130)
my_game.column("company_number", anchor=CENTER, width=130)
my_game.column("company_VAT", anchor=CENTER, width=130)

my_game.heading("#0", text="", anchor=CENTER)
my_game.heading("company_name", text="Company Name", anchor=CENTER)
my_game.heading("company_address", text="Company Address", anchor=CENTER)
my_game.heading("company_number", text="Company Number", anchor=CENTER)
my_game.heading("company_VAT", text="Company VAT", anchor=CENTER)

for i in range(1, len_in_options_dic + 1):
    my_game.insert(parent='', index='end', text='',
                 values=(options_dict[i]['options']['company_name'], options_dict[i]['options']["company_address"], options_dict[i]['options']["company_number"], options_dict[i]['options']["company_VAT"]))

my_game.pack()


#
#
# label_date = CTkLabel(master=app, text="Select the Date")
# label_date.place(relx=0.2, rely=0.50, anchor="center")
# my_date = tb.DateEntry(app, bootstyle="dark", firstweekday=0, startdate=date.today())
# my_date.place(relx=0.2, rely=0.55, anchor="center")
#
# label_test = CTkLabel(master=app, text="Select the Company")
# label_test.place(relx=0.2, rely=0.65, anchor="center")
# options = CTkComboBox(master=app, values=["Company A", "Company B"])
# options.place(relx=0.2, rely=0.70, anchor="center")


# Btn
#
# def handle_option():
#     company_choose = options.get()
#     if company_choose == "Company A":
#         print(f'Company name is :' + optionA["company_name"])
#         print(f'Company adress is :' + optionA["company_address"])
#     elif company_choose == "Company B":
#         print(f'Company name is :' + optionB["company_name"])
#         print(f'Company adress is :' + optionB["company_address"])
#
#     print(f"Date of the Invoice: {my_date.entry.get()}")
#
#     app.quit()

#
# btn_option = CTkButton(master=app, text="Submit", corner_radius=32, command=handle_option)
# btn_option.place(relx=0.2, rely=0.85, anchor="center")

app.mainloop()
