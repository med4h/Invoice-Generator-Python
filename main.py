from customtkinter import *
from spinbox import Spinbox

app = CTk()
app.geometry("800x400")
app.title("Multiverse Invoice Generator Project")

frame = CTkFrame(app)
frame.pack()

first_name_label = CTkLabel(frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = CTkLabel(frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = CTkEntry(frame)
last_name_entry = CTkEntry(frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)


phone_label = CTkLabel(frame, text="Phone")
phone_label.grid(row=0, column=2)
phone_entry = CTkEntry(frame)
phone_entry.grid(row=1, column=2)

qty_label = CTkLabel(frame, text="Qty")
qty_label.grid(row=2, column=0)
qty_entry = Spinbox(frame, min_value=0, max_value=float('inf'), width=phone_entry.winfo_reqwidth(), height=phone_entry.winfo_reqheight())
qty_entry.grid(row=3, column=0)

description_label = CTkLabel(frame, text="Description")
description_label.grid(row=2, column=1)
description_entry = CTkEntry(frame)
description_entry.grid(row=3, column=1)

unit_price_label = CTkLabel(frame, text="Unit Price")
unit_price_label.grid(row=2, column=2)
unit_price_entry = CTkEntry(frame)
unit_price_entry.grid(row=3, column=2)

app.mainloop()