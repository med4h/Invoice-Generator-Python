from customtkinter import *
from spinbox import Spinbox
from tkinter import ttk, Tk, messagebox
from docxtpl import DocxTemplate
import datetime
import os


def clear_item():
    qty_entry.set(value=0)
    description_entry.delete(0, "end")
    unit_price_entry.delete(0, "end")

def new_invoice():
    first_name_entry.delete(0, "end")
    last_name_entry.delete(0, "end")
    phone_entry.delete(0, "end")
    clear_item()
    treeview.delete(*treeview.get_children())
    invoice_list.clear()


invoice_list = []
def add_item():
    try:
        qty = int(qty_entry.get())
        desc = description_entry.get()
        price = float(unit_price_entry.get())                                                   
        phone = phone_entry.get()

        if not all(char.isdigit() or char in "()-" for char in phone):
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Invalid Input")
        return

    line_total = round(qty * price, 2)
    invoice_item = [qty, desc, price, line_total]
    treeview.insert('', 0, values=invoice_item)
    clear_item()
    invoice_list.append(invoice_item)

def generate_invoice():
    doc = DocxTemplate("Invoice_Generator.docx")
    name = first_name_entry.get() + " " + last_name_entry.get()
    phone = phone_entry.get()
    subtotal = sum(item[3] for item in invoice_list)
    salestax = 0.0725
    tax_amount = subtotal * salestax
    total = subtotal + tax_amount

    doc.render({
        "name": name,
        "phone": phone,
        "invoice_list": invoice_list,
        "subtotal": f"{subtotal:.2f}",
        "salestax": f"{salestax * 100:.2f}%",
        "total": f"{total:.2f}",
    })

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    doc_name = os.path.join(desktop_path, "new_invoice_" + name + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M%S") + ".docx")
    doc.save(doc_name)

    messagebox.showinfo("Invoice Complete", "Invoice Complete")

    new_invoice()



app = CTk()
app.title("INVOGEN")
#add icon to title bar SOMEHOW....

frame = CTkFrame(app, fg_color="#222324")
frame.pack()

set_default_color_theme("green")

first_name_label = CTkLabel(frame, text="First Name", font=("heebo", 12, "bold"))
first_name_label.grid(row=0, column=0)
last_name_label = CTkLabel(frame, text="Last Name", font=("heebo", 12, "bold"))
last_name_label.grid(row=0, column=1)

first_name_entry = CTkEntry(frame)
last_name_entry = CTkEntry(frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)


phone_label = CTkLabel(frame, text="Phone", font=("heebo", 12, "bold"))
phone_label.grid(row=0, column=2)
phone_entry = CTkEntry(frame)
phone_entry.grid(row=1, column=2)

qty_label = CTkLabel(frame, text="Quantity", font=("heebo", 12, "bold"))
qty_label.grid(row=2, column=0)
qty_entry = Spinbox(frame, min_value=0, max_value=float('inf'), width=phone_entry.winfo_reqwidth()+ 15, height=phone_entry.winfo_reqheight())
qty_entry.grid(row=3, column=0)

description_label = CTkLabel(frame, text="Description", font=("heebo", 12, "bold"))
description_label.grid(row=2, column=1)
description_entry = CTkEntry(frame)
description_entry.grid(row=3, column=1)

unit_price_label = CTkLabel(frame, text="Unit Price", font=("heebo", 12, "bold"))
unit_price_label.grid(row=2, column=2)
unit_price_entry = CTkEntry(frame)
unit_price_entry.grid(row=3, column=2)

add_button = CTkButton(frame, text="Add Item", fg_color="#218802", hover_color="#1C7202", command= add_item)
add_button.grid(row=4, column=1, pady=20)

columns= ("qty", "description", "price", "total")
treeview = ttk.Treeview(frame, columns=columns, show="headings")
treeview.heading("qty", text="Qty")
treeview.heading("description", text="Description")
treeview.heading("price", text="Price")
treeview.heading("total", text="Total")

treeview.grid(row=5, column=0, columnspan=3, padx=20, pady=10)

generate_button = CTkButton(frame, text="Generate", fg_color="#218802", hover_color="#1C7202", command=generate_invoice)
generate_button.grid(row=6, column=2, pady=5)

new_invoice_button = CTkButton(frame, text="New Invoice", fg_color="#218802", hover_color="#1C7202", command=new_invoice)
new_invoice_button.grid(row=6, column=0, pady=20)

app.mainloop()
