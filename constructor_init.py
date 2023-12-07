class employee:
    empid = 0
    empname = ''
    empadress = ''
    empsalary = 0

    def __init__(self):
        print("this is the  first oop")
    
        
    def getdata(self):
        return str(self.empid) +";"+ self.empname + ";" + self.empadress + ";" + str(self.empsalary)

    def printdata(self):
        print(self.getdata())

emp1 =employee()
emp2 = employee()        
     
      
