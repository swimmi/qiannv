class Role(object):

    def __init__(self, name, career):
        self.name = name
        self.career = career

    def __str__(self):
        return 'name: %s, career: %s' % (self.name, self.career)