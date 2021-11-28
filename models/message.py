class Message:
    
    def __init__(self, message: str, node, extra = None):
        self.message = message
        self.node = node
        self.extra = extra

    def __str__(self):
        output = self.message
        output += "*"*7
        output += str(node)
        if extra:
            output += str(extra)
        return output
