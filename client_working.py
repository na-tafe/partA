"""
filename : client_working.py
"""

import socket
import sys

def start_client(server_ip):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server on the specified IP address at port 65432
        client_socket.connect((server_ip, 65432)) 
        print(f"Connected to server at {server_ip}:65432")

        while True:
            # Get message from the user to send to the server
            message_to_send = input("Enter a message to send to the server (type 'exit' to quit): ")
            client_socket.sendall(message_to_send.encode('utf-8'))

            if message_to_send.lower() == 'exit':
                print("Exiting client.")
                break

            # Receive response from the server
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Server: {response}")

    except ConnectionRefusedError:
        print("Could not connect to the server. Is the server running?")
        sys.exit(1)  # Exit with a status code
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        client_socket.close()
        print("Client connection closed.")

def main():
    server_ip = input("Enter the server IP address to connect to: ")
    start_client(server_ip)

if __name__ == "__main__":
    main()
