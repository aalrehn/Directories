import logging
from Logger.logger_module import FileLogger
from unittest.mock import patch, MagicMock

def test_log_message():
    with patch('logging.getLogger') as mock_get_logger:
        mock_logger = MagicMock()
        mock_get_logger.return_value = mock_logger
        logger = FileLogger()
        logger.log('Test message')
        mock_logger.info.assert_called_with('Test message')
