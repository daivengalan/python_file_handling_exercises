class Student:
    def __init__(self, student_name, gwa_score):
        self.student_name = student_name
        self.gwa_score = float(gwa_score)

class GwaProcessor:
    def __init__(self, file_source):
        self.file_source = file_source
        self.students = []

    def load_data(self):
        with open(self.file_source, "r") as file:
            for line in file:
                name, gwa = line.strip().split(",")
                self.students.append(Student(name, gwa))
# (Keep the classes from Commit 6, then add this method inside GwaProcessor)
    def get_highest(self):
        # MISTAKE: Using max() assumes a higher number is better
        highest = max(self.students, key=lambda s: s.gwa_score)
        return highest

# (Add at the bottom)
processor = GwaProcessor("students.txt")
processor.load_data()
top = processor.get_highest()
print(f"Highest goes to {top.student_name} with {top.gwa_score}")