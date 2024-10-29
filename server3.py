# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:24:32 2024

@author: 61420
"""

import socket
import ipaddress

def start_server(server_ip):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    server_socket.bind((server_ip, 65432))
    
    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server is listening on {server_ip}:65432...")

    # Wait for a connection
    connection, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")
    
    while True:
        try:
            # Receive the message from the client
            message = connection.recv(1024).decode('utf-8')
            
            if not message:  # If the message is empty, the client has closed the connection
                print("Client has closed the connection.")
                break
            
            print(f"Client: {message}")
            
            # Respond to the client
            response = input("Server (type 'exit' to end): ")
            connection.sendall(response.encode('utf-8'))
            
            if response.lower() == 'exit':
                print("Server ended the connection.")
                break
        
        except (ConnectionResetError, ConnectionAbortedError):
            print("Connection interrupted. Server will shut down.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break
    
    # Close the connection and server socket
    connection.close()
    server_socket.close()
    print("Server closed the connection.")

def main():
    while True:
        # Get the server IP address from user input
        server_ip = input("Enter 'o' to listen for a request from another host, 'l' to listen to localhost, or 'x' to exit: ")
        
        # Check if the user wants to exit
        if server_ip.lower() == 'x':
            print("Exiting...")
            return
        
        # Allow 'localhost' to be treated as '127.0.0.1'
        if server_ip.lower() == 'l':
            server_ip = '127.0.0.1'
        
        # Validate the IP address
        try:
            server_ip = '0.0.0.0'  # to listen on all interfaces
            ipaddress.ip_address(server_ip)  # Validate the IP address
            start_server(server_ip)  # Start the server with the validated IP
            return
        except ValueError:
            print("Invalid IP address. Please enter a valid IP address.")

# Start the server
if __name__ == "__main__":
    main()
