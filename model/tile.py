class Tile(object):

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __str__(self):
        return '[%s]%s' % (self.name, self.desc)