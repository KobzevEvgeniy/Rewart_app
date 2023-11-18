from Fabrics.item_fabric import ItemFabric
from Products.amber import Amber


class AmberGenerator(ItemFabric):
    def create_item(self):
        return Amber()
