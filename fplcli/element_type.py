class ElementType(object):
    def __init__(self, j):
        self.id_ = j['id']
        self.plural_name = j['plural_name']
        self.plural_name_short = j['plural_name_short']
        self.singular_name = j['singular_name']
        self.singular_name_short = j['singular_name_short']