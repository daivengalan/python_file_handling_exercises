class Student:
    def __init__(self, student_name, gwa_score):
        self.student_name = student_name
        self.gwa_score = float(gwa_score)

# testing if the class works
test_student = Student("Test User", "1.75")
print(test_student.student_name, test_student.gwa_score)