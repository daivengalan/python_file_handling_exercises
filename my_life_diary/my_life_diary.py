class LifeDiaryWriter:
    def __init__(self, output_file):
        self.output_file = output_file

    def start_writing(self):
        # Ask for the name once at the very beginning
        user_name = input("Before we start, what is your name? ").strip()
        print(f"Hi {user_name}, let's start writing your diary!\n")

        try:
            with open(self.output_file, "w") as file:
                while True:
                    current_line = input("Enter line: ")
                    file.write(current_line + "\n")

                    # Now using the user's name in the prompt
                    prompt_text = f"Are there more lines, {user_name}? (y/n): "
                    user_choice = input(prompt_text).lower().strip()

                    # Using startswith('n') so "no" or "n" both work
                    if user_choice.startswith('n'):
                        print(f"\nThanks for sharing, {user_name}. Check {self.output_file} for your entries!")
                        break

        except IOError as error_message:
            print(f"Could not write to file: {error_message}")

if __name__ == "__main__":
    my_life_logger = LifeDiaryWriter("mylife.txt")
    my_life_logger.start_writing()
