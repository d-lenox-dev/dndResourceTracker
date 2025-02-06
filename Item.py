class Item:
	def __init__(self, name: str, description: str = "Not Researched", food_req: int = 0, basic_req: int = 0,
				 upgrade_req: int = 0, unique_req: int = 0,
				 researched: bool = False, craftable: bool = False):
		self.name = name
		self.description = description
		self.food_req = food_req
		self.basic_req = basic_req
		self.upgrade_req = upgrade_req
		self.unique_req = unique_req
		self.researched = researched
		self.craftable = craftable

	def as_list(self):
		item_as_list = [self.name, self.food_req, self.basic_req, self.upgrade_req, self.unique_req]
		return item_as_list

	def as_dict(self):
		item = {
			"name": self.name,
			"desc": self.description,
			"food": self.food_req,
			"basic": self.basic_req,
			"upgrade": self.upgrade_req,
			"unique": self.unique_req,
			"researched": self.researched,
			"craftable": self.craftable
		}
		return item


def from_dict(item_dict: dict):
	return Item(item_dict["name"], item_dict["desc"], item_dict["food"], item_dict["basic"], item_dict["upgrade"],
				item_dict["unique"], item_dict["researched"], item_dict["craftable"])
