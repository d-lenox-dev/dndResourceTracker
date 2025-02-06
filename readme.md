# DND Resource Tracker and Item Manager

---

## Version 0.1.1

---
This program is for all the DND lovers who want a more convenient way to track resources and manage items. The program
is small and uses basic csv files as the save data. This program is NOT complete and has very limited functionality.
Crashes and errors are to be expected.

### Resource Tracking

As of right now, the program uses its own conversion rates for
adventurers allocated to certain tasks.

- The general formula:
    * `Resource` = round((`allocation` - 0.5) / `required peoples`) x `amount gained`
- Allocating to smithing will give 3 base materials per 10 adventurers and 2 upgrade materials per 20 adventurers
- Allocating to the kitchen will increase food by 10 units of food per 10 adventurers and 15 units per 20 adventurers
- Allocating to defense will increase security by 5 units per 10 adventurers and 10 units per 20 adventurers
- Allocating to training will increase army strength by 2 units per 10 adventurers
- Allocating to research will increase unique materials by 1 per 10 adventurers and 3 per 20 adventurers

The amounts gained per every 10 and 20 does stack. For example, in the kitchen, 30 allocated adventurers would trigger
the 10 allotment twice and the 20 allotment once, giving you 35 units of food rather than 25, if they only triggered
once. In the future, the idea of customizability is in the works. This would allow the user to give 25 units of food per
10, as an example.

### Item Management

Included with the software is a Comma Separated Values (CSV) file that contains example items. In v0.11B there is no way
to edit that file without manually changing the values inside the CSV. In future versions, users will be able to add and
remove items to that list. A great example of how to use the list is when the user's party finds an item, they should be
able to add that item to the list. An initial item will start with 0 values and show not researched. Once declared
researched by the DM, users can add the information about the item to the list.

# Change Log

---

## v0.11B

---

* Moved cycling functions to a handler file
* Added items list functionality
* When a user clicks on an item within the scrollable list, a new window should pop up displaying information

## v0.1.1

---

* Versioning changed to reflect `vX.X.X`
* Changed the `Item` class to initial with 0 values and added craftable boolean
* Modified `items.csv` to reflect changes to the `Item` object class
  * changed two example items to reflect items from my campaign
* Updated `csv_handler.py` to reflect changes to the `Item` object class
* Added getter and setter functions to the `Item` object class
* Added an `as_dict` function to the `Item` object class
* `json_handler.py` added change data storage to JSON files instead of CSV
  * `items.json` and `resources.json` added as a result
  * `items.csv` and `resources.csv` may be delete after program is reworked
* Began reworking the main program to use JSON instead of CSV