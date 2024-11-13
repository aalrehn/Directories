
from filesystem.directory_structure import DirectoryStructure
from Logger.logger_module import FileLogger

class CommandExecutor:
    """
    A class responsible for executing parsed commands on the directory structure.

    Attributes:
        filesystem (DirectoryStructure): The directory structure on which operations are performed.
        logger (FileLogger): The logger used to log command execution results.
    """
    def __init__(self, filesystem: DirectoryStructure, logger: FileLogger):

        self.filesystem = filesystem
        self.logger = logger

    def execute(self, command: dict) -> str:
        """
        Executes a command on the directory structure.

        Args:
            command (dict): A dictionary containing the command to execute and its arguments, with keys:
                - 'operation' (str): The command to execute (e.g., 'CREATE', 'LIST', 'MOVE', 'DELETE').
                - 'source' (str): The source path for the command, if applicable.
                - 'destination' (str): The destination path for the command, if applicable.

        Returns:
            str: A message indicating the result of the command. Returns an error message if the command is unsupported.
        """
        if command.get('operation') == 'CREATE':
            return self.filesystem.create_directory(path=command.get('source'))
        if command.get('operation') == 'LIST':
            return self.filesystem.show_structure()
        if command.get('operation') == 'MOVE':
            return self.filesystem.move_directory(src=command.get('source'), dest=command.get('destination'))
        if command.get('operation') == 'DELETE':
            return self.filesystem.delete_directory(path=command.get('source'))
        return f"Error: Unsupported command: {command.get('operation')}"