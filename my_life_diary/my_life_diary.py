class LifeDiaryWriter:
   def __init__(self, output_file):
       self.output_file = output_file
   def start_writing(self):
       try:
           with open(self.output_file, "w") as file:
               while True:
                   current_line = input("Enter line: ")
                   file.write(current_line + "\n")

                   user_choice = input("Are there more lines y/n? ").lower().strip()

                   if user_choice == 'no':
                       print("File writing complete. Check mylife.txt!")
                       break

       except IOError as error_message:
           print(f"Could not write to file: {error_message}")

if __name__ == "__main__":
   my_life_logger = LifeDiaryWriter("mylife.txt")
   my_life_logger.start_writing()
