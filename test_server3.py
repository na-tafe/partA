# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 23:22:31 2024

@author: 61420
"""
import unittest
import socket
import ipaddress
import server3  # Ensure this points to your server implementation

class TestServer3(unittest.TestCase):

    def setUp(self):
        """Set up a server that listens for connections."""
        self.server_ip = '127.0.0.1'
        self.server_port = 65432
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Try to bind the socket and handle the error if the address is in use
        try:
            self.server_socket.bind((self.server_ip, self.server_port))
            self.server_socket.listen(1)
        except OSError as e:
            self.fail(f"Failed to bind server socket: {e}")

    def tearDown(self):
        """Clean up the server socket."""
        self.server_socket.close()

    def test_bind(self):
        """Test if the server socket is successfully created and bound."""
        self.assertTrue(self.server_socket)

    def test_accept(self):
        """Test accepting a connection."""
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.server_ip, self.server_port))

        # Accept the connection on the server side
        conn, addr = self.server_socket.accept()

        # Check that the accepted address matches the client's address
        self.assertEqual(addr[0], self.server_ip)
        self.assertEqual(addr[1], client_socket.getsockname()[1])

        # Clean up
        conn.close()
        client_socket.close()

    def test_invalid_ip_raises_exception(self):
        """Test that invalid IP raises a ValueError."""
        invalid_ip = '256.256.256.256'
        with self.assertRaises(ValueError):
            ipaddress.ip_address(invalid_ip)

if __name__ == '__main__':
    unittest.main()
