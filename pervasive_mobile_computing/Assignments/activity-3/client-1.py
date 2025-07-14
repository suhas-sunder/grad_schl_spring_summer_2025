import socket

def run_client():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(("localhost", 12347))
    print("🟢 Connected to server.")

    # Step 1: Send credentials
    username = input("Username: ")
    password = input("Password: ")
    credentials = f"{username}:{password}"
    client_sock.send(credentials.encode())

    # Step 2: Receive authentication result
    auth_response = client_sock.recv(1024).decode()
    print(auth_response)

    if not auth_response.startswith("✅"):
        client_sock.close()
        return

    # Step 3: Send message to echo
    message = input("Enter message to send: ")
    client_sock.send(message.encode())
    data = client_sock.recv(1024)
    print(f"🪞 Echoed from server: {data.decode()}")

    client_sock.close()

if __name__ == "__main__":
    run_client()
