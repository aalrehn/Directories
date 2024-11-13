import pytest
from filesystem.directory_structure import DirectoryStructure

def test_create_directory():
    fs = DirectoryStructure()
    result = fs.create_directory('fruits')
    assert result == 'CREATE fruits'
    assert 'fruits' in fs.root

def test_create_nested_directories():
    fs = DirectoryStructure()
    fs.create_directory('fruits/apples')
    assert 'fruits' in fs.root
    assert 'apples' in fs.root['fruits']

def test_delete_directory():
    fs = DirectoryStructure()
    fs.create_directory('fruits')
    result = fs.delete_directory('fruits')
    assert result == 'DELETE fruits'
    assert 'fruits' not in fs.root

def test_delete_nonexistent_directory():
    fs = DirectoryStructure()
    result = fs.delete_directory('fruits')
    expected_message = 'DELETE fruits\nCannot delete fruits - fruits does not exist'
    assert result == expected_message

def test_move_directory():
    fs = DirectoryStructure()
    fs.create_directory('fruits')
    fs.create_directory('vegetables')
    fs.create_directory('fruits/apples')
    result = fs.move_directory('fruits/apples', 'vegetables')
    assert result == 'MOVE fruits/apples vegetables'
    assert 'apples' in fs.root['vegetables']
    assert 'apples' not in fs.root['fruits']

def test_move_nonexistent_directory():
    fs = DirectoryStructure()
    fs.create_directory('vegetables')
    result = fs.move_directory('fruits/apples', 'vegetables')
    expected_message = 'MOVE fruits/apples vegetables\nCannot move fruits/apples - fruits does not exist'
    assert result == expected_message

def test_show_structure():
    fs = DirectoryStructure()
    fs.create_directory('fruits')
    fs.create_directory('fruits/apples')
    fs.create_directory('vegetables')
    result = fs.show_structure()
    expected_output = '\n'.join([
        'LIST',
        'fruits',
        '  apples',
        'vegetables'
    ])
    assert result == expected_output

def test_locate_directory_exists():
    fs = DirectoryStructure()
    fs.create_directory('fruits/apples')
    exists, parent = fs.locate_directory('fruits/apples')
    assert exists is True
    assert 'apples' in parent

def test_locate_directory_not_exists():
    fs = DirectoryStructure()
    fs.create_directory('fruits')
    exists, missing_folder = fs.locate_directory('fruits/apples')
    assert exists is False
    assert missing_folder == 'apples'