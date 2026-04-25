class IntegerProcessor:
    def __init__(self, source_file):
        self.source_file = source_file
        self.even_file = "double.txt"
        self.odd_file = "triple.txt"

    def process_numbers(self):
        with open(self.source_file, "r") as source:
            for line in source:
                number = int(line.strip())
                print(f"Reading: {number}")
