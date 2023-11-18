from Fabrics.item_fabric import ItemFabric
from Products.vibranium import Vibranium


class VibraniumGenerator(ItemFabric):
    def create_item(self):
        return Vibranium()