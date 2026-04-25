class DiaryWriter:
    def __init__(self, filename):
        self.filename = filename

    def collect_lines(self):
        while True:
            user_input = input("Enter line: ")
            # MISTAKE: Opening file inside the loop with 'w' overwrites everything
            with open(self.filename, "a") as file:
                file.write(user_input + "\n ")

            choice = input("Are there more lines y/n? ")
            if choice.lower() == 'no':
                break

    def write_to_diary(self):
        try:
            while True:
                user_text = input("Enter line: ")
                with open(self.filename, "a") as file:
                    file.write(user_text + "\n")

                choice = input("Are there more lines y/n? ")
                if choice.lower() == 'n':
                    break
        except Exception as error:
            print(f"Something went wrong: {error}")

writer = DiaryWriter("mylife.txt")
writer.collect_lines()