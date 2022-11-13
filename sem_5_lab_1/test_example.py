def test_func():
    print(5)
from types import NoneType
from array import array
from directory import Directory
from binaryFile import BinaryFile
from logTextFile import LogTextFile
from bufferFile import BufferFile


class TestingDir:
    fatherDirectory = Directory('fatherDirectory1')
    def test_directoryCreate(self):
        maxElements = 7
        name = 'dir1'
        directory = Directory(name, maxElements)
        assert directory.DIR_MAX_ELEMS == maxElements
        assert directory.numberOfElements == 0
        assert directory.dirName == name
        assert type(directory.father) is NoneType
        #assert type(directory.listOfFiles) is str
    def test_directoryMove(self):
        directory = Directory('directory1')
        assert type(directory.father) is NoneType
        directory.move(self.fatherDirectory)
        assert directory.father == self.fatherDirectory
    def test_directoryDel(self):
        directory = Directory('directory2')
        del directory
        assert 'directory' not in locals()
class TestingBinaryFile:
    fatherDirectory = Directory('fatherDirectory2')
    def test_binaryFileCreate(self):
        name = 'binary1'
        info = 'kdvjiviufsvvush'
        binaryFile = BinaryFile(name, info, self.fatherDirectory)
        assert binaryFile.fileName == name
        assert binaryFile.info == info
        assert binaryFile.read() == info
        assert binaryFile.father == self.fatherDirectory
    def test_binaryFileMove(self):
        name = 'binary2'
        info = 'kdvjiviufsvvffush'
        binaryFile = BinaryFile(name, info, self.fatherDirectory)
        assert type(binaryFile.father) is NoneType
        binaryFile.move(self.fatherDirectory)
        assert binaryFile.father == self.fatherDirectory
    def test_binaryFileDel(self):
        binaryFile = BinaryFile('binary3')
        del binaryFile
        assert 'binaryFile' not in locals()

class TestingLogTextFile:
    fatherDirectory = Directory('fatherDirectory3')
    def test_logFileCreate(self):
        name = 'log1'
        logTextFile = LogTextFile(name, self.fatherDirectory)
        assert logTextFile.fileName == name
        assert logTextFile.read() == ''
        assert logTextFile.father == self.fatherDirectory
    def test_logFileMove(self):
        name = 'log2'
        logFile = LogTextFile(name)
        assert type(logFile.father) is NoneType
        logFile.move(self.fatherDirectory)
        assert logFile.father == self.fatherDirectory
    def test_logFileDel(self):
        logTextFile = LogTextFile('log3')
        del logTextFile
        assert 'logTextFile' not in locals()
    def test_logFileAddLine(self):
        name = 'log4'
        info = 'info'
        logFile = LogTextFile(name, info)
        assert logFile.read() == info
        logFile.appendNewLine('new line')
        assert 'line' in logFile.read()
class TestingBufferFile:
    fatherDirectory = Directory('fatherDirectory4')
    def test_BufferFileCreate(self):
        name = 'buffer'
        size = 7
        bufferFile = BufferFile(name, size, self.fatherDirectory)
        assert bufferFile.MAX_BUF_FILE_SIZE == size
        assert bufferFile.father == self.fatherDirectory
        assert bufferFile.fileName == name
    def test_BufferFileMove(self):
        name = 'buffer'
        info = 'ekwfjwiojfi'
        bufferFile = BufferFile(name, info)
        assert type(bufferFile.father) is NoneType
        bufferFile.move(self.fatherDirectory)
        assert bufferFile.father == self.fatherDirectory
    def test_BufferFileDel(self):
        bufferFile = BufferFile('buff')
        del bufferFile
        assert 'bufferFile' not in locals()
    def test_BufferFileConsume(self):
        name = 'buffer2'
        size = 7
        bufferFile = BufferFile(name, size)
        element1 = 'e1'
        element2 = 'e2'
        bufferFile.push(element1)
        #bufferFile.push(element1)
        bufferFile.push(element2)
        assert bufferFile.consume() == element1
        assert bufferFile.consume() == element2
        assert bufferFile.consume() == None










