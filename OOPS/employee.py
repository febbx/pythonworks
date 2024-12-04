class Employee:
    
    #intializing attributes of student class

    def set_stdnt(self,name,rollnum,age,course):
        self.name=name
        self.rollnum=rollnum
        self.age=age
        self.course=course

    def display(self):
        print(self.name,self.rollnum,self.age,self.course)

stud1=Employee()

stud1.set_stdnt("feby",7,22,"django")


stud1.display()