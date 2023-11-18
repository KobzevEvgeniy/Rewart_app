from Fabrics.item_fabric import ItemFabric
from Products.pearl import Perl


class PerlGenerator(ItemFabric):
    def create_item(self):
        return Perl()