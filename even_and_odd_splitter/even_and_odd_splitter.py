class number_splitter:
    def __init__(self, input_file="numbers.txt"):
        self.input_file = input_file
        self.even_file = "even.txt"
        self.odd_file = "odd.txt"

input_stream = open("numbers.txt", "r")
even_file = open("even.txt", "w")
odd_file = open("odd.txt", "w")

for line in input_stream:
    clean_line = line.strip()
    if clean_line:
        current_number = int(clean_line)
        if current_number % 2 == 0:
            even_file.write(str(current_number) + "\n")
        else:
            odd_file.write(str(current_number) + "\n")

input_stream.close()
even_file.close()
odd_file.close()