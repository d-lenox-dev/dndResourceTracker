import json

import Item
import csv_handler


def resources_as_dict(resources: list[int]):
	dict_list = {"resources": [
		{"food": resources[0],
		 "basic": resources[1],
		 "upgrade": resources[2],
		 "unique": resources[3],
		 "security": resources[4],
		 "strength": resources[5],
		 "adventurers": resources[6]
		 }
	]}
	return dict_list


def items_to_dict(items: list[Item.Item]):
	dict_list = []

	for item in items:
		dict_list.append(item.as_dict())

	items_dict = {'items': dict_list}
	return items_dict


def create_items_json(items_dict: dict):
	with open("items.json", "w") as f:
		json.dump(items_dict, f)


def read_items_json():
	with open("items.json", "r") as f:
		data = json.load(f)
		f.close()

	items_list = []

	for item in data["items"]:
		items_list.append(Item.from_dict(item))

	return items_list


def create_resources_json(resources_dict: dict):
	with open("resources.json", "w") as f:
		json.dump(resources_dict, f)


def read_resources_json():
	with open("resources.json", "r") as f:
		data = json.load(f)
		f.close()
	return data


create_items_json(items_to_dict(csv_handler.master_item_list))

resource_data = read_resources_json()
items_data = read_items_json()
