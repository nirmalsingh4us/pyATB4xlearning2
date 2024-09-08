from abc import ABC, abstractmethod

class Excelreader(ABC):
    @abstractmethod
    def Readfromexcel(self):
        pass

class Browser:
    @abstractmethod
    def startbrowser(self):
        pass
    @abstractmethod
    def stopbrowser(self):
        pass

class TC1(Browser):

    def startbrowser(self):
        print("Enter the browsername")
    def stopbrowser(self):
        print("Stop the browser")
    def Readfromexcel(self):
        print("Export the data in the excel file")
    def testcase(self):
        self.startbrowser()
        self.Readfromexcel()
        self.stopbrowser()

tc =TC1()
tc.testcase()