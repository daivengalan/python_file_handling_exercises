file_path = "students.txt"

with open(file_path, "r") as data:
    for line in data:
        print(line)