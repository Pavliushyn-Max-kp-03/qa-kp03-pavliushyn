# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from directory import Directory
from binaryFile import BinaryFile
from bufferFile import BufferFile
from logTextFile import LogTextFile

'''def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')'''
print('this is lab1')
root = Directory('root', 100)
directory1 = Directory('child1', 20, root)
directory2 = Directory('child2', 3, root)
directory3 = Directory('chchild', 10, directory1)

binaryFile1 = BinaryFile('binFile1', 'info1', root)
binaryFile2 = BinaryFile('binFile2', 'info2', directory3)
print(binaryFile2.read())

logTextFile1 = LogTextFile('log1', 'loginfo1', root)
logTextFile2 = LogTextFile('log2', 'This is', directory2)
logTextFile2.appendNewLine(' QA lab1')
print(logTextFile2.read())

bufferFile1 = BufferFile('buf1', 5, root)
bufferFile2 = BufferFile('buf2', 3, directory1)
print(type(root.listOfFiles))
print(root.listOfFiles)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
