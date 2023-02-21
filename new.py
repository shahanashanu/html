class setexample:

    def printresult(self):
        personlist=['Rash','Dany','John','Mery']
        print(type(personlist))

        personset=set(personlist)
        print(type(personlist))


        #print the complete list
        print(personlist)		

        #print the complete list
        print(personset)
        for person in personset:
            if person.startswith('R'):
                print(person)

     
setexample=setexample()
setexample.printresult()

