class LogTextFile:
    def __init__(self, fileName, info, father = None):
        self.fileName = fileName
        self.father = father
        self.info = info
    def delete(self):
        return
    def move(self, path):
        return
    def read(self):
        return self.info
    def appendNewLine(self, newLine):
        self.info += newLine
        self.info += '\n'