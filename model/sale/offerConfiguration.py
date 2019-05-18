class OfferConfiguration(object):
    id: int
    make: int
    model: int
    version: int
    color: int
    edition: int
    modification: int
    imageLink: str
    def __init__(self, id: int, make: int, model: int, version: int, color: int, edition: int, modification: int, imageLink: str):
        self.id = id
        self.make = make
        self.model = model
        self.version = version
        self.color = color
        self.edition = edition
        self.modification = modification
        self.imageLink = imageLink