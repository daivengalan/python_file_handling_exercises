class DiaryWriter:
    def __init__(self, filename):
        self.filename = filename

    def collect_lines(self):
        while True:
            user_input = input("Enter line: ")
            # MISTAKE: Opening file inside the loop with 'w' overwrites everything
            with open(self.filename, "w") as file:
                file.write(user_input)

            choice = input("Are there more lines y/n? ")
            if choice.lower() == 'no':
                break
writer = DiaryWriter("mylife.txt")
writer.collect_lines()
