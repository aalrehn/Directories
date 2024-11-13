import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = script_dir  # Since main.py is now in the project root
sys.path.insert(0, project_root)

from filesystem.directory_structure import DirectoryStructure
from Logger.logger_module import FileLogger  # Adjusted import
from filesystem.command_executor import CommandExecutor
from filesystem.command_interpreter import CommandInterpreter
from filesystem.file_input_reader import FileInputReader

def main():
    """
    The main driver function that processes commands from a file.
    """
    input_file = os.path.join(project_root, 'input.txt')
    filesystem = DirectoryStructure()
    logger = FileLogger()
    executor = CommandExecutor(filesystem, logger)

    for line in FileInputReader.read_commands(input_file):
        command = CommandInterpreter.interpret_command(line)
        result = executor.execute(command)
        logger.log(result)

if __name__ == '__main__':
    main()
