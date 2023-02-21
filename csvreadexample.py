
import csv
class csvreader:
    def readcsv(self):
        try:
            fileref=open('designation.csv','r')
            csvref=csv.reader(fileref)
            
            for line in csvref:
                print(line)
        except:
            print('file read error')

       
       
        
        
        
csvreader=csvreader()
csvreader.readcsv()
  