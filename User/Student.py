class Person:

    def __init__(self,name,address,phoneNo,email,gender):
        self.__name = name
        self.__address =address
        self.__phoneNo = phoneNo
        self.__email = email
        self.__gender = gender

    def getName(self):
        return self.__name

    def getGender(self):
        return self.__gender

    def getPhoneNo(self):
        return self.__phoneNo

    def getEmail(self):
        return self.__email

    def getAddress(self):
        return self.__address

    def setName(self,name):
        self.__name = name

    def setGender(self,gender):
        self.__gender = gender

    def setPhoneNo(self,phoneNo):
        self.__phoneNo = phoneNo

    def setEmail(self,email):
        self.__email = email

    def setAddress(self,address):
        self.__address = address

    def display(self):
        print("Name",self.__name)
        print("Address",self.__address)
        print("Email",self.__gender)
        print("PhoneNumber",self.__phoneNo)
        print("Gender",self.__gender)

class Student(Person):

    def __init__(self,studentId,name,address,phoneNo,email,gender,status):
        super().__init__(name,address,phoneNo,email,gender)
        self.studentId = studentId
        self.balance = None
        self.noDue = None
        self.__status = status
        self.amount = None
        self.totalAmount = 1200

    def paySubscriptionFees(self,fees):
        self.amount = self.amount + fees
        return self.amount

    def getTotalAmountPaid(self):
        return self.amount

    def getBalance(self):
        return self.totalAmount - self.amount

    def getStatus(self):
        return self.status

    def updateStatus(self,status):
        self.__status= status

    def getnoDue(self):
        if self.amount == self.totalAmount:
            print( "No due pending")
            return self
        print("You need to pay pending amount for No Due certificate which is ",self.totalAmount-self.amount)

    def display(self):
        super().display()
        print("Display Amount paid",self.amount)
        print("Status in college",self.__status)





        