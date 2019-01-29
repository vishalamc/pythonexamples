

#CGPA Calculator
CA_Total=100
CA_Wtg=25
MTT_Total=40
MTT_Wtg=20
ETE_Total=70
ETE_Wtg=50


course_code=input("Enter course code\n")
CA_obtained_Marks=float(input("Enter total CA obtained marks\n"))
MTT_obtained_Marks=float(input("Enter total MTT obtained marks\n"))
ETE_obtained_Marks=float(input("Enter total ETE obtained marks\n"))
Att=float(input("Enter total Attendance Marks\n"))
CA=(CA_obtained_Marks*CA_Wtg)/CA_Total
MTT=(MTT_obtained_Marks*MTT_Wtg)/MTT_Total
ETE=(ETE_obtained_Marks*ETE_Wtg)/ETE_Total
Total=CA+MTT+ETE+Att  
print("---Report Card----")
print("Percentage in",course_code,Total,end="")
print("%")
print("CGPA in",course_code,Total/10,end="")
