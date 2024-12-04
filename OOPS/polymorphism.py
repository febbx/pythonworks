#polymorphism : more than one form.

#method overloading : same method name and diff no of parameters.

class Operations:

    def add(self,num1,num2):
        print(num1 + num2)

    def add(self, num1, num2, num3):
        print(num1 + num2 + num3)

obj=Operations()
obj.add(10,30,40)
