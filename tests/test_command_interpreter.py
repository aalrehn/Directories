
from filesystem.command_interpreter import CommandInterpreter

def test_interpret_create_command():
    command = 'CREATE fruits'
    result = CommandInterpreter.interpret_command(command)
    assert result == {'operation': 'CREATE', 'source': 'fruits', 'destination': None}

def test_interpret_delete_command():
    command = 'DELETE fruits/apples'
    result = CommandInterpreter.interpret_command(command)
    assert result == {'operation': 'DELETE', 'source': 'fruits/apples', 'destination': None}

def test_interpret_move_command():
    command = 'MOVE fruits/apples vegetables'
    result = CommandInterpreter.interpret_command(command)
    assert result == {'operation': 'MOVE', 'source': 'fruits/apples', 'destination': 'vegetables'}

def test_interpret_list_command():
    command = 'LIST'
    result = CommandInterpreter.interpret_command(command)
    assert result == {'operation': 'LIST', 'source': None, 'destination': None}

def test_interpret_invalid_command():
    command = 'INVALID fruits'
    result = CommandInterpreter.interpret_command(command)
    assert result == {'operation': 'INVALID', 'source': 'fruits', 'destination': None}
