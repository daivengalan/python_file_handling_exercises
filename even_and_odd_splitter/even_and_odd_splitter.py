input_stream = open("numbers.txt", "r")
for line in input_stream:
    current_number = int(line.strip())
    if current_number % 2 == 0:
        print(f"{current_number} is even")
    else:
        print(f"{current_number} is odd")
input_stream.close()