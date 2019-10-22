class university:
    def __init__(self,a):
        print("phagwara")
    def displayUniversityName(self):
        print("Lovely Professional University")
class section:
    def displaySection(self):
        print("D1E37")
class sectionMentor:
    def displayMentor(self):
        print("Kumar Vishal")

class student(university,section,sectionMentor):
    def studentDetails(self):
        super().displayUniversityName()
        super().displaySection()
        super().displayMentor()
        print("Name: Rohit")
s1=student("kk")
s1.studentDetails()
