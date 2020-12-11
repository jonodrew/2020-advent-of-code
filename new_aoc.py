import os


class NewAdventOfCode:
    def __init__(self, day: str):
        self.day = day

    def new_files_and_folders(self):
        base_path = "/home/jonathan/projects/2020-advent-of-code/"
        code_path = os.path.join(base_path, self.day)
        os.mkdir(code_path)
        os.mknod(f"{code_path}/{self.day}.py")
        os.mknod(f"{code_path}/input.txt")
        test_path = os.path.join(base_path, f"tests/{self.day}")
        os.mkdir(test_path)
        os.mknod(f"{test_path}/test_day_{self.day}.py")


def main():
    n = NewAdventOfCode(day=input("Which day is it? "))
    n.new_files_and_folders()
    print("Finished!")


if __name__ == "__main__":
    main()
