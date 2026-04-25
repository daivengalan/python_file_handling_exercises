class IntegerProcessor:
    def __init__(self, source_file):
        self.source_file = source_file
        self.even_file = "double.txt"
        self.odd_file = "triple.txt"

test_run = IntegerProcessor("integers.txt")