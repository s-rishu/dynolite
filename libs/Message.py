class Message:
    def __init__(self, type, args):
        self.type = type
        self.args = args

    def __str__(self):
        return "Message type %s" % self.type 