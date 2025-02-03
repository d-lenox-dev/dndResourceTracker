import csv
import Items


def add_to_itemslist(new_item: Items.Item):
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
            item = Items.Item(line[0], int(line[1]), int(line[2]), int(line[3]), int(line[4]))
            items.append(item)

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
