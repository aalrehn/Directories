
from filesystem.command_executor import CommandExecutor
from filesystem.directory_structure import DirectoryStructure
from Logger.logger_module import FileLogger

class MockLogger:
    def __init__(self):
        self.messages = []

    def log(self, message):
        self.messages.append(message)

def test_execute_create_command():
    fs = DirectoryStructure()
    logger = MockLogger()
    executor = CommandExecutor(fs, logger)
    command = {'operation': 'CREATE', 'source': 'fruits', 'destination': None}
    result = executor.execute(command)
    assert result == 'CREATE fruits'
    assert 'fruits' in fs.root

def test_execute_delete_command():
    fs = DirectoryStructure()
    fs.create_directory('fruits')
    logger = MockLogger()
    executor = CommandExecutor(fs, logger)
    command = {'operation': 'DELETE', 'source': 'fruits', 'destination': None}
    result = executor.execute(command)
    assert result == 'DELETE fruits'
    assert 'fruits' not in fs.root

def test_execute_move_command():
    fs = DirectoryStructure()
    fs.create_directory('fruits')
    fs.create_directory('vegetables')
    fs.create_directory('fruits/apples')
    logger = MockLogger()
    executor = CommandExecutor(fs, logger)
    command = {'operation': 'MOVE', 'source': 'fruits/apples', 'destination': 'vegetables'}
    result = executor.execute(command)
    assert result == 'MOVE fruits/apples vegetables'
    assert 'apples' in fs.root['vegetables']
    assert 'apples' not in fs.root['fruits']

def test_execute_list_command():
    fs = DirectoryStructure()
    fs.create_directory('fruits')
    fs.create_directory('vegetables')
    logger = MockLogger()
    executor = CommandExecutor(fs, logger)
    command = {'operation': 'LIST', 'source': None, 'destination': None}
    result = executor.execute(command)
    expected_output = '\n'.join(['LIST', 'fruits', 'vegetables'])
    assert result == expected_output

def test_execute_invalid_command():
    fs = DirectoryStructure()
    logger = MockLogger()
    executor = CommandExecutor(fs, logger)
    command = {'operation': 'INVALID', 'source': None, 'destination': None}
    result = executor.execute(command)
    assert result == 'Error: Unsupported command: INVALID'
