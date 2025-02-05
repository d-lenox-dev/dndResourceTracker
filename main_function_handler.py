import tkinter
import customtkinter
import Items
import csv_handler as csvh


master_resource_list = csvh.master_resource_list
master_item_list = csvh.master_item_list


def item_info_window(item: Items):
    item_window = tkinter.Toplevel()
    item_window.geometry("480x500")
    item_window.title("Item Information")
    item_window.columnconfigure((0, 1, 2), weight=1, uniform='a')
    item_window.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1, uniform='a')

    item_name = customtkinter.CTkLabel(item_window, text=item.name, text_color="black")
    item_name.grid(column=1, columnspan=3, row=0)
    item_desc = customtkinter.CTkLabel(item_window, text=item.description, text_color="black")
    item_desc.grid(columnspan=3, row=1, rowspan=5)



def create_item():
    item_create_window = tkinter.Toplevel()
    item_create_window.geometry("480x500")
    item_create_window.title("Create an Item")
    item_create_window.columnconfigure((0, 1, 2), weight=1, uniform='a')
    item_create_window.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1, uniform='a')

    name_input = tkinter.StringVar()
    name_input_box = customtkinter.CTkEntry(item_create_window, height=40, textvariable=name_input)

    desc_input = tkinter.StringVar()
    desc_input_box = customtkinter.CTkEntry(item_create_window, height=240, textvariable=desc_input)


def cycle_smithing(allocation: int, basic_amt: customtkinter.CTkLabel, upgraded_amt: customtkinter.CTkLabel):
    gained_basic = round((allocation - 0.5) / 10) * 3
    gained_upgrade = round((allocation - 0.5) / 20) * 2
    master_resource_list[1] = int(master_resource_list[1]) + gained_basic
    master_resource_list[2] = int(master_resource_list[2]) + gained_upgrade
    basic_amt.configure(text=master_resource_list[1])
    upgraded_amt.configure(text=master_resource_list[2])


def cycle_cooking(allocation: int, food_amt: customtkinter.CTkLabel):
    gained_food_tier_1 = round((allocation - 0.5) / 10) * 10
    gained_food_tier_2 = round((allocation - 0.5) / 20) * 15
    total_food_gained = gained_food_tier_2 + gained_food_tier_1
    master_resource_list[0] = int(master_resource_list[0]) + total_food_gained
    food_amt.configure(text=master_resource_list[0])


def cycle_defense(allocation: int, defense_amt: customtkinter.CTkLabel):
    gained_defense_tier_1 = round((allocation - 0.5) / 10) * 5
    gained_defense_tier_2 = round((allocation - 0.5) / 20) * 10
    total_defense_gained = gained_defense_tier_1 + gained_defense_tier_2
    master_resource_list[4] = int(master_resource_list[4]) + total_defense_gained
    defense_amt.configure(text=master_resource_list[4])


def cycle_research(allocation: int, research_amt: customtkinter.CTkLabel):
    gained_unique_tier_1 = round((allocation - 0.5) / 10) * 1
    gained_unique_tier_2 = round((allocation - 0.5) / 20) * 3
    total_unique_gained = gained_unique_tier_1 + gained_unique_tier_2
    master_resource_list[3] = int(master_resource_list[3]) + total_unique_gained
    research_amt.configure(text=master_resource_list[3])
