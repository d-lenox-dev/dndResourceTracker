import csv

import Item


def add_to_itemslist(new_item: Item.Item):
	master_item_list.append(new_item.as_list())


def read_resources():
	with open('resources.csv', 'r') as items_file_in:
		csv_reader = csv.reader(items_file_in)

		resources = []

		for line in csv_reader:
			resources.append(line)

	items_file_in.close()

	return resources[0]


def write_resources(resource_list: list):
	with open('resources.csv', 'w') as resource_file_out:
		csv_writer = csv.writer(resource_file_out)
		csv_writer.writerow(resource_list)


def read_items():
	with open('items.csv', 'r') as items_file_in:
		csv_reader = csv.reader(items_file_in)

		items = []

		for line in csv_reader:
			name = line[0]
			desc = line[1]
			food = int(line[2])
			basic = int(line[3])
			upgrade = int(line[4])
			unique = int(line[5])
			researched = False
			craftable = False

			if line[6].capitalize() is 'T':
				researched = True

			if line[7].capitalize() is 'T':
				craftable = True

			items.append(Item.Item(name, desc, food, basic, upgrade, unique, researched, craftable))

	items_file_in.close()

	return items


def write_items(items_list: list):
	with open('items.csv', 'w', newline='') as items_file_out:
		csv_writer = csv.writer(items_file_out)

		for item in items_list:
			csv_writer.writerow(item.as_list())


# Master Item List
master_item_list = read_items()

# Master Resource List/Dictionary
master_resource_list = read_resources()
