
class FileInputReader:
    """
    A helper class that reads commands from an input file.
    """
    @staticmethod
    def read_commands(filename: str):
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()
