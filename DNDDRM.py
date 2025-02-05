import tkinter
from tkinter import messagebox
import customtkinter
import Items
import csv_handler as csvh
import main_function_handler as mfh

master_resource_list = mfh.master_resource_list
master_item_list = mfh.master_item_list


def rack_day():
    error_text.configure(text="")
    try:

        used_adventurers = int(smithing_box.get()) + int(kitchen_box.get()) + int(defense_box.get()) + int(
            research_box.get()) + int(training_box.get())
        num_adventurers_num.configure(text=used_adventurers)
        if int(used_adventurers) > int(master_resource_list[6]):
            error_text.configure(text="too many adventurers")
        else:
            mfh.cycle_smithing(smithing.get(), smithing_basic_num, smithing_upgraded_num)
            mfh.cycle_cooking(cooking.get(), cooking_report_num)
            mfh.cycle_defense(defense.get(), defense_report_num)
            mfh.cycle_research(research.get(), research_report_num)

    except ():
        error_text.configure(text="")


# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("DND Day Resource Manager (DRM)")

# Grid Config
app.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')
app.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1, uniform='a')

# UI elements
# Titles
smithing_title = customtkinter.CTkLabel(app, text="Smithing")
smithing_title.grid(row=0, column=0)

cooking_title = customtkinter.CTkLabel(app, text="Cooking")
cooking_title.grid(row=0, column=1)

defense_title = customtkinter.CTkLabel(app, text="Defense")
defense_title.grid(row=0, column=2)

research_title = customtkinter.CTkLabel(app, text="Research")
research_title.grid(row=0, column=3)

training_title = customtkinter.CTkLabel(app, text="Training")
training_title.grid(row=0, column=4)

# Smithing
smithing = tkinter.IntVar()
smithing_box = customtkinter.CTkEntry(app, height=40, textvariable=smithing)
smithing_box.grid(padx=10, row=1, column=0, sticky="new")

# Cooking
cooking = tkinter.IntVar()
kitchen_box = customtkinter.CTkEntry(app, height=40, textvariable=cooking)
kitchen_box.grid(padx=10, row=1, column=1, sticky="new")

# Defense
defense = tkinter.IntVar()
defense_box = customtkinter.CTkEntry(app, height=40, textvariable=defense)
defense_box.grid(padx=10, row=1, rowspan=2, column=2, sticky="new")

# Research
research = tkinter.IntVar()
research_box = customtkinter.CTkEntry(app, height=40, textvariable=research)
research_box.grid(padx=10, row=1, column=3, sticky="new")

# Training
training = tkinter.IntVar()
training_box = customtkinter.CTkEntry(app, height=40, textvariable=training)
training_box.grid(padx=10, row=1, column=4, sticky="new")

# Download button
download_button = customtkinter.CTkButton(app, height=40, text="Complete Day", command=rack_day)
download_button.grid(padx=10, row=2, column=2, sticky="new")

# Error Print
error_text = customtkinter.CTkLabel(app, text_color="red", text="")
error_text.grid(row=3, column=2, sticky="new")

# Stats
num_adventurers = customtkinter.CTkLabel(app, text="Used Adventurers: ")
num_adventurers.grid(row=2, column=0)
num_adventurers_num = customtkinter.CTkLabel(app, text="0")
num_adventurers_num.grid(row=2, column=1)

total_adventurers = customtkinter.CTkLabel(app, text="Total Adventurers: ")
total_adventurers.grid(row=3, column=0)
total_adventurers_num = customtkinter.CTkLabel(app, text=master_resource_list[6])
total_adventurers_num.grid(row=3, column=1)

smithing_basic_title = customtkinter.CTkLabel(app, text="Basic Materials: ")
smithing_basic_title.grid(row=4, column=0)
smithing_basic_num = customtkinter.CTkLabel(app, text=master_resource_list[1])
smithing_basic_num.grid(row=4, column=1)

smithing_upgraded_title = customtkinter.CTkLabel(app, text="Upgraded Materials: ")
smithing_upgraded_title.grid(row=5, column=0)
smithing_upgraded_num = customtkinter.CTkLabel(app, text=master_resource_list[2])
smithing_upgraded_num.grid(row=5, column=1)

cooking_report_title = customtkinter.CTkLabel(app, text="Food: ")
cooking_report_title.grid(row=6, column=0)
cooking_report_num = customtkinter.CTkLabel(app, text=master_resource_list[0])
cooking_report_num.grid(row=6, column=1)

defense_report = customtkinter.CTkLabel(app, text="Defense: ")
defense_report.grid(row=7, column=0)
defense_report_num = customtkinter.CTkLabel(app, text=master_resource_list[4])
defense_report_num.grid(row=7, column=1)

research_report = customtkinter.CTkLabel(app, text="Unique Materials: ")
research_report.grid(row=8, column=0)
research_report_num = customtkinter.CTkLabel(app, text=master_resource_list[3])
research_report_num.grid(row=8, column=1)

training_report = customtkinter.CTkLabel(app, text="Army Strength: ")
training_report.grid(row=9, column=0)
training_report_num = customtkinter.CTkLabel(app, text=master_resource_list[5])
training_report_num.grid(row=9, column=1)

# Items Listing
items_list = customtkinter.CTkScrollableFrame(app,
                                              height=230,
                                              width=390)
items_list.grid(rowspan=5, row=3, columnspan=4, column=2)

for item in master_item_list:
    bt = customtkinter.CTkButton(
        items_list,
        text=item.name,
        command=lambda: mfh.item_info_window(item)
    )
    bt.pack(pady=5)


item_add_button = customtkinter.CTkButton(
    app,
    text="Add Item",
    command=mfh.create_item
)


# on close saving function
def on_close():
    if messagebox.askyesno("Save", "Save before closing?"):
        csvh.write_resources(master_resource_list)
        app.destroy()
    else:
        app.destroy()


# Run App
app.protocol("WM_DELETE_WINDOW", on_close)
app.mainloop()
