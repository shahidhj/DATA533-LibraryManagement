from User.Student import Student
from User.Teacher import Teacher

Shahid = Student(name="Shahid", address="Springfield",studentId=123455678,phoneNo="132445",email="shahid.h@abc.com",gender="M",status="Present Student")
Shahid.amount = 123
Shahid.getName()
Shahid.getAddress()
Shahid.getBalance()
Shahid.getGender()
Shahid.getnoDue()
Shahid.setAddress("Changed from Springfield to Rutland")
Shahid.paySubscriptionFees(1234)

Shahid.display()

Khalad = Teacher(name="Khalad",address="UBC",email="Khalad@UBC.ca",gender="Male",phoneNo="455657",employeeId="1243",department="CS",salary=99999,role="Prof")
Khalad.addSubjects("Data 533")
Khalad.addSubjects("Data 540")
Khalad.subscriptionFees(100)
Khalad.updateResearchAreas("Human computer Interaction")
Khalad.display()
Khalad.updateResearchAreas("Machine Learning")
Khalad.display()



