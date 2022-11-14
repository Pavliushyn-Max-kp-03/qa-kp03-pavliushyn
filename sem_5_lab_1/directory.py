class Directory:
    def __init__(self, dirName, maxElements = 0, father = None):
        self.father = father
        self.dirName = dirName
        self.DIR_MAX_ELEMS = maxElements
        self.numberOfElements = 0
        self.listOfFiles = []
    def __del__(self):
        print('Destructor called, ' + self.dirName + 'was deleted')
        return
    def listElements(self):
        result = self.dirName + ':('
        for item in self.listOfFiles:
           if type(item) is Directory:
               result += item.listElements()
           else:
               result += item.fileName + ', ' + '\n'
        result += '), '
        return result
    def move(self, path):
        if (path.numberOfElements >= path.DIR_MAX_ELEMS + 1):
            print('This directory is full, try other')
            return
        self.father = path
        self.father.listOfFiles.append(self)
        self.father.numberOfElements += 1
        return
