from Fabrics.item_fabric import ItemFabric
from Products.onyx import Onyx


class OnyxGenerator(ItemFabric):
    def create_item(self):
        return Onyx()