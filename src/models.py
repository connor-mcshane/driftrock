class User(object):
    """ Small class used to separate json data from program logic """

    def __init__(self, id, email):
        self.id = id
        self.email = email


class Purchase(object):
    """ Small class used to separate json data from program logic """

    def __init__(self, user_id, item, spend):
        self.user_id = user_id
        self.item = item
        self.spend = spend
