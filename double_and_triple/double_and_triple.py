class IntegerProcessor:
    def __init__(self, source_file):
        self.source_file = source_file
        self.even_file = "double.txt"
        self.odd_file = "triple.txt"

    def process_numbers(self):
        with open(self.source_file, "r") as source:
            for line in source:
                val = int(line.strip())
                if val % 2 == 0:
                    # even logic here
                    pass
                else:
                    # odd logic here
                    pass
