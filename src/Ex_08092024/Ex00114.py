class ExcelReader:
    @staticmethod
    def readexcelfile():
        print("Read data form the excel file")

class Mysqlconnection():
    @staticmethod
    def Sqlconn():
        print("Database connection is done")
class TC1:

    def runtc(self):
        ExcelReader.readexcelfile()
        Mysqlconnection.Sqlconn()

tc = TC1()
tc.runtc()
