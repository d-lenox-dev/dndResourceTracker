
class Item:
	def __init__(self,
				 name: str,
				 food_req: int,
				 basic_req: int,
				 upgrade_req: int,
				 unique_req: int):

		self.name = name
		self.food_req = food_req
		self.basic_req = basic_req
		self.upgrade_req = upgrade_req
		self.unique_req = unique_req
		self.researched = False

	def as_list(self):
		item_as_list = [self.name, self.food_req, self.basic_req, self.upgrade_req, self.unique_req]
		return item_as_list
