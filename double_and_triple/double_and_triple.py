class IntegerProcessor:
    def __init__(self, source_file):
        self.source_file = source_file
        self.even_file = "double.txt"
        self.odd_file = "triple.txt"

    def process_numbers(self):
        with open(self.source_file, "r") as source, \
                open(self.even_file, "w") as even_out, \
                open(self.odd_file, "w") as odd_out:

            for line in source:
                cleaned_line = line.strip()
                if not cleaned_line:  # skip empty lines
                    continue
                val = int(cleaned_line)