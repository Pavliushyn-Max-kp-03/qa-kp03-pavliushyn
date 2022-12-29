class LogTextFile:
    def __init__(self, id, fileName, info, father = None):
        self.fileName = fileName
        self.father = father
        self.info = info
        self.id = id
    def __delete__(self):
        print('Destructor called', + self.fileName + 'was deleted')
        return
    def move(self, path):
        if (path.numberOfElements >= path.DIR_MAX_ELEMS + 1):
            print('This directory is full, try other')
            return
        self.father = path
        self.father.listOfFiles.append(self)
        self.father.numberOfElements += 1
        return
    def read(self):
        return self.info
    def appendNewLine(self, newLine):
        self.info += newLine
        self.info += '\n'
