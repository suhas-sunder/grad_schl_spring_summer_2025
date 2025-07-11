import socket
import threading

# Simulated username:password store
AUTHORIZED_CLIENTS = {
    "user1": "pass1",
    "suhas": "secure123",
}

def handle_client(client_sock, client_addr):
    print(f"🔗 Connected to {client_addr}")

    try:
        # Step 1: Receive credentials
        credentials = client_sock.recv(1024).decode().strip()
        username, password = credentials.split(":")

        # Step 2: Authenticate
        if AUTHORIZED_CLIENTS.get(username) != password:
            client_sock.send("❌ Authentication failed.".encode())
            print(f"❌ Auth failed for {client_addr} ({username})")
            client_sock.close()
            return

        client_sock.send("✅ Authentication successful.".encode())
        print(f"✅ {username} authenticated from {client_addr}")

        # Step 3: Echo loop
        while True:
            data = client_sock.recv(1024)
            if not data:
                break
            print(f"📨 Received from {username}: {data.decode()}")
            client_sock.send(data)

    except Exception as e:
        print(f"❗ Error with {client_addr}: {e}")
    finally:
        client_sock.close()
        print(f"🔌 Disconnected {client_addr}")

def run_server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(("localhost", 12347))  # New port
    server_sock.listen(5)
    print("🔵 Multi-client server listening on port 12347...")

    try:
        while True:
            client_sock, client_addr = server_sock.accept()
            thread = threading.Thread(target=handle_client, args=(client_sock, client_addr))
            thread.daemon = True
            thread.start()
    except KeyboardInterrupt:
        print("🔻 Server shutting down.")
    finally:
        server_sock.close()

if __name__ == "__main__":
    run_server()
import socket
import threading

# Simulated username:password credentials
AUTHORIZED_CLIENTS = {
    "suhas": "secure123",
    "user1": "pass1",
    "guest": "welcome"
}

def handle_client(client_sock, client_addr):
    print(f"🔗 Connected to {client_addr}")

    try:
        # Step 1: Receive credentials
        credentials = client_sock.recv(1024).decode().strip()
        username, password = credentials.split(":")

        # Step 2: Authenticate
        if AUTHORIZED_CLIENTS.get(username) != password:
            client_sock.send("❌ Authentication failed.".encode())
            print(f"❌ Auth failed for {client_addr} ({username})")
            client_sock.close()
            return

        client_sock.send("✅ Authentication successful.".encode())
        print(f"✅ {username} authenticated from {client_addr}")

        # Step 3: Echo loop
        while True:
            data = client_sock.recv(1024)
            if not data:
                break
            print(f"📨 Received from {username}: {data.decode()}")
            client_sock.send(data)

    except Exception as e:
        print(f"❗ Error with {client_addr}: {e}")
    finally:
        client_sock.close()
        print(f"🔌 Disconnected {client_addr}")

def run_server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(("localhost", 12347))  # Port used for simulation
    server_sock.listen(5)
    print("🔵 Multi-client server listening on port 12347...")

    try:
        while True:
            client_sock, client_addr = server_sock.accept()
            thread = threading.Thread(target=handle_client, args=(client_sock, client_addr))
            thread.daemon = True
            thread.start()
    except KeyboardInterrupt:
        print("🔻 Server shutting down.")
    finally:
        server_sock.close()

if __name__ == "__main__":
    run_server()
