class BufferFile:
    def __init__(self, fileName, maxSize = 0, father = None):
        self.fileName = fileName
        self.father = father
        self.info = []
        self.MAX_BUF_FILE_SIZE = maxSize
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
    def push(self, item):
        if len(self.info) >= self.MAX_BUF_FILE_SIZE:
            print('This file is full with items')
            return
        self.info.append(item)
    def consume(self):
        if len(self.info) >= 1:
            temp = self.info[0]
            self.info.pop(0)
            return temp
        return None