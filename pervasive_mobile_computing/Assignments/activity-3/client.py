<<<<<<< HEAD
# client.py
import socket

def run_client():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Updated to match server port
    client_sock.connect(("localhost", 12346))
    print("🟢 Connected to simulated Bluetooth server.")

    message = input("Enter a message to send: ")
    client_sock.send(message.encode())

    data = client_sock.recv(1024)
    print(f"🪞 Echoed from server: {data.decode()}")

    client_sock.close()

if __name__ == "__main__":
    run_client()
=======
# client.py
import socket

def run_client():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Updated to match server port
    client_sock.connect(("localhost", 12346))
    print("🟢 Connected to simulated Bluetooth server.")

    message = input("Enter a message to send: ")
    client_sock.send(message.encode())

    data = client_sock.recv(1024)
    print(f"🪞 Echoed from server: {data.decode()}")

    client_sock.close()

if __name__ == "__main__":
    run_client()
>>>>>>> cad0cd06e96ba923c36e069bba3069896216c126
