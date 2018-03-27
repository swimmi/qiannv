import random

from db.db_helper import DBHelper
from model.item import Item

class Equip(Item):

    def __init__(self, name):
        self.name = name
        self.tiles = []
        self.color = random.randint(0, 3)
        self.db = DBHelper()
        self.generate_tiles()

    def generate_tiles(self):
        total_tiles = self.db.get_tile()
        count = 8
        if self.color == 0:
            count = 10
        if self.color == 1:
            count = 7
        while count > 0:
            count -= 1
            i = random.randint(0, len(total_tiles) - 1)
            self.tiles.append(total_tiles[i])

    def __str__(self):
        str = self.name
        str += '\n'
        for tile in self.tiles:
            str += '[%s]%s\n' % (tile.name, tile.desc)
        return str