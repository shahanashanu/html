

class filereadexample:
    def printresult(self):
        try:
            fileref=open('firstreadexample.txt','r')
            for line in fileref:
                print(line)
        except:
            print('file read error')

       
       
        
        
        
filereadexample=filereadexample()
filereadexample.printresult()
  