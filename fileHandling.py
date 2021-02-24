class FileHandling:
    def __init__(self, fileName):
        self.pointer = open(fileName, 'r')
        self.pointer.readline()
        self.pointer.readline()
    def readLine(self):
        return self.pointer.readline()
    
