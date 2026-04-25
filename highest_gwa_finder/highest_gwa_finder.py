file_path = "students.txt"

with open(file_path, "r") as data:
    for line in data:
        info = line.strip().split(",")
        name = info[0]
        gwa = info[1]
        print(f"Name: {name} | GWA: {gwa}")