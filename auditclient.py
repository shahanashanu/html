from audit import Audit

class Auditclient:
    def printresult(self):
       
        audit=Audit()

        x=input('Please enter a messege  ')
        num1=input('Please enter num1  ')
        num2=input('Please enter num2  ')

        intnum2=int(num2)
        intnum1=int(num1)
        intnum1=int(num1)
        print(type(num1))
        print(type(num2))

        print(type(intnum1))
        print(type(intnum2))

        numlist=[int(num1),int(num2)]
        audit.printAudit(x)

        audit.calculatesum(int(num1),int(num2))
        audit.calculateproduct(int(num1),int(num2))
        audit.calculateproduct1(numlist)
        
        
auditclient=Auditclient()
auditclient.printresult()
  