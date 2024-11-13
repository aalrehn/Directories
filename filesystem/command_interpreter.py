
class CommandInterpreter:
    
    @staticmethod
    def interpret_command(command_str: str) -> dict:

        parts = command_str.strip().split()
        operation = source = destination = None
        if len(parts) == 1:
            operation = parts[0]
        elif len(parts) == 2:
            operation, source = parts
        elif len(parts) == 3:
            operation, source, destination = parts
        return {'operation': operation, 'source': source, 'destination': destination}
