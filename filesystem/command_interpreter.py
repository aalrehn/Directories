
class CommandInterpreter:
    """
    A utility class for parsing command strings into structured components.
    """
    @staticmethod
    def interpret_command(command_str: str) -> dict:
        """
        Parses a command string and separates it into operation and arguments.

        Args:
            command_str (str): The command string to interpret, e.g., 'MOVE fruits/apples vegetables'.

        Returns:
            dict: A dictionary containing:
                - 'operation': The command to execute (e.g., 'CREATE', 'MOVE', 'DELETE', 'LIST').
                - 'source': The source path, if applicable (e.g., 'fruits/apples').
                - 'destination': The destination path, if applicable (e.g., 'vegetables').
        """
        parts = command_str.strip().split()
        operation = source = destination = None
        if len(parts) == 1:
            operation = parts[0]
        elif len(parts) == 2:
            operation, source = parts
        elif len(parts) == 3:
            operation, source, destination = parts
        return {'operation': operation, 'source': source, 'destination': destination}
