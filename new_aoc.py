import os


class NewAdventOfCode:
    def __init__(self, day: str):
        self.day = day

    def new_files_and_folders(self):
        base_path = os.getcwd()
        code_path = os.path.join(base_path, self.day)
        os.mkdir(code_path)
        open(os.path.join(code_path, f"{self.day}.py"), "w").close()
        open(f"{code_path}/input.txt", "w").close()
        test_path = os.path.join(base_path, f"tests/{self.day}")
        os.mkdir(test_path)
        open(f"{test_path}/test_day_{self.day}.py", "w").close()


def main():
    n = NewAdventOfCode(day=input("Which day is it? "))
    n.new_files_and_folders()
    print("Finished!")


if __name__ == "__main__":
    main()
