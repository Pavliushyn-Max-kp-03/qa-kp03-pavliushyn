class Directory:
    def __init__(self, dirName, father = None, maxElements = 0):
        self.father = father
        self.dirName = dirName
        self.DIR_MAX_ELEMS = maxElements
        self.numberOfElements = 0
        self.ListOfFiles = []
    def delete(self):
        return
    def listElements(self):
        return
    def move(self, path):
        return