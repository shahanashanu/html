

class setexample:
    def printresult(self):
       
        personlist=['Ram','Sita','Parvathi','shiva','Ram']
        print(type(personlist))
        
        personset=set(personlist)
        print(type(personset))

        #print the complete list
        print(personlist)
        
        #print the complete set
        print(personset)
        
        
        #print one element from list
        print(personlist[1])
        
        #print all elements one by one from list
        for person in personset:
            if person.startswith('s'):
                print(person)
                
                
        numberlist=[1,2,3,4,5,6]
        print(type(numberlist))
        
        #print the complete list
        print(numberlist)
        
        #print the complete list
        print(numberlist[1])
        
        #print all elements one by one from list
        for number in numberlist:
            if number>=2:
                print('----------------')
                print(number)               
        
        
       
       
        
        
        
setexample=setexample()
setexample.printresult()
  