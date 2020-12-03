class ReadLines(object):
    def __init__(self, file_input: str):
        with open(file_input) as reader:
            self.inputs = [line.rstrip() for line in reader]
