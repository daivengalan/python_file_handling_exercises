class DiaryWriter:
    def __init__(self, filename):
        self.filename = filename

    def collect_lines(self):
        while True:
            line = input("Enter line: ")
            more = input("Are there more lines y/n? ")
            if more.lower() == 'n':
                break

writer = DiaryWriter("mylife.txt")
writer.collect_lines()