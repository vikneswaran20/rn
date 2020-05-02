import uuid


class UUID:
    def __init__(self, iteration, delimiter):
        self.iteration = iteration
        self.delimiter = delimiter

    def genrate_random(self):
        uuids = [str(uuid.uuid4()) for i in range(self.iteration)]
        return self.delimiter.join(uuids)
