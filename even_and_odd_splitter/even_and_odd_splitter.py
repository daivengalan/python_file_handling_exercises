input_stream = open("numbers.txt", "r")
even_file = open("even.txt", "w")
odd_file = open("odd.txt", "w")

for line in input_stream:
    current_number = int(line.strip())
    if current_number % 2 == 0:
        even_file.write(str(current_number) + "\n")
    else:
        odd_file.write(str(current_number) + "\n")

input_stream.close()
even_file.close()
odd_file.close()