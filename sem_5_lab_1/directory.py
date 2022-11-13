class Directory:
    def __init__(self, dirName, maxElements = 0, father = None):
        self.father = father
        self.dirName = dirName
        self.DIR_MAX_ELEMS = maxElements
        self.numberOfElements = 0
        self.listOfFiles = []
    def delete(self):
        return
    def listElements(self):
        return
    def move(self, path):
        return