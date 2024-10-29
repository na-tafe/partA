# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:18:19 2024

@author: 61420
"""

import unittest
from unittest.mock import patch, MagicMock
import socket
import client_working

class TestClient(unittest.TestCase):
    
    @patch('client_working.socket.socket')
    def test_successful_connection_and_message_exchange(self, mock_socket):
        # Create a mock socket instance
        mock_instance = MagicMock()
        mock_socket.return_value = mock_instance

        # Mock the connect method
        mock_instance.connect.return_value = None

        # Mock the recv method to return a response
        mock_instance.recv.return_value = b'Hello from server!'

        # Simulate user input for sending a message
        with patch('builtins.input', side_effect=['Hello server!', 'exit']):
            client_working.start_client('127.0.0.1')

        # Check if connect was called with the correct arguments
        mock_instance.connect.assert_called_with(('127.0.0.1', 65432))

        # Check if sendall was called with the right message
        mock_instance.sendall.assert_any_call(b'Hello server!')
        mock_instance.sendall.assert_any_call(b'exit')
        
        # Check if the socket was closed
        mock_instance.close.assert_called_once()

    @patch('client_working.socket.socket')
    def test_connection_refused(self, mock_socket):
        # Create a mock socket instance
        mock_instance = MagicMock()
        mock_socket.return_value = mock_instance

        # Mock the connect method to raise an exception
        mock_instance.connect.side_effect = ConnectionRefusedError

        with patch('builtins.input', side_effect=['Hello server!']):
            with self.assertRaises(SystemExit):  # expecting the script to exit
                client_working.start_client('127.0.0.1')

        # Ensure close was called on the socket
        mock_instance.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
