
from filesystem.directory_structure import DirectoryStructure
from Logger.logger_module import FileLogger

class CommandExecutor:
 
    def __init__(self, filesystem: DirectoryStructure, logger: FileLogger):

        self.filesystem = filesystem
        self.logger = logger

    def execute(self, command: dict) -> str:

        if command.get('operation') == 'CREATE':
            return self.filesystem.create_directory(path=command.get('source'))
        if command.get('operation') == 'LIST':
            return self.filesystem.show_structure()
        if command.get('operation') == 'MOVE':
            return self.filesystem.move_directory(src=command.get('source'), dest=command.get('destination'))
        if command.get('operation') == 'DELETE':
            return self.filesystem.delete_directory(path=command.get('source'))
        return f"Error: Unsupported command: {command.get('operation')}"