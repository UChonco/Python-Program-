class student:
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.grade = []

    def add_grade(self,grade):
        if 0 <= grade <= 100:
            self.grade.append(grade)
            print(f"Successful added Grade {grade}, to {self.name} grade ")
        else:
            print("Invalid Grade ! Please enter valod grade")
    
    def calculate_average(self):
        average = sum(self.grade) / len(self.grade)
        return average
    
    def is_passing(self):
        grading = self.calculate_average() >= 60
        return grading

    def display_info(self):
        passing = "Passed" if self.is_passing() else "Failed"
        print(f"{"_"*40}")
        print("______Grading System______")
        print(f"Student: {self.student_id} \n Name: {self.name} \n Average Grade: {self.calculate_average()}\n Status: {passing}")

name = input("Enter your name : ")
student_id =input("Enter your student ID : ")
s = student(name,student_id)

grade=float(input("Enter your first Grade: "))
grade1=float(input("Enter your Second Grade: "))
grade2=float(input("Enter your Third Grade: "))
grade3=float(input("Enter your Fourty Grade: "))

s.add_grade(grade)
s.add_grade(grade1)
s.add_grade(grade2)
s.add_grade(grade3)


s.display_info()
