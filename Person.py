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
