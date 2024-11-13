
from filesystem.file_input_reader import FileInputReader
from unittest.mock import mock_open, patch

def test_read_commands():
    mock_data = 'CREATE fruits\nCREATE vegetables\nLIST\n'
    with patch('builtins.open', mock_open(read_data=mock_data)) as mock_file:
        commands = list(FileInputReader.read_commands('input.txt'))
        mock_file.assert_called_once_with('input.txt', 'r')
    assert commands == ['CREATE fruits', 'CREATE vegetables', 'LIST']
