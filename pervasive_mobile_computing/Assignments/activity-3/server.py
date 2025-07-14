<<<<<<< HEAD
# server.py
import socket

def run_server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Updated port to avoid "port in use" error
    server_sock.bind(("localhost", 12346))  
    server_sock.listen(1)
    print("TEST: Bluetooth server listening on port 12346...")

    client_sock, client_addr = server_sock.accept()
    print(f"🔗 Connected to {client_addr}")

    try:
        while True:
            data = client_sock.recv(1024)
            if not data:
                break
            print(f"📨 Received: {data.decode()}")
            client_sock.send(data)  # Echo back
    except Exception as e:
        print(f"❗ Error: {e}")
    finally:
        client_sock.close()
        server_sock.close()
        print("🔌 Connection closed.")

if __name__ == "__main__":
    run_server()
=======
# server.py
import socket

def run_server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Updated port to avoid "port in use" error
    server_sock.bind(("localhost", 12346))  
    server_sock.listen(1)
    print("TEST: Bluetooth server listening on port 12346...")

    client_sock, client_addr = server_sock.accept()
    print(f"🔗 Connected to {client_addr}")

    try:
        while True:
            data = client_sock.recv(1024)
            if not data:
                break
            print(f"📨 Received: {data.decode()}")
            client_sock.send(data)  # Echo back
    except Exception as e:
        print(f"❗ Error: {e}")
    finally:
        client_sock.close()
        server_sock.close()
        print("🔌 Connection closed.")

if __name__ == "__main__":
    run_server()
>>>>>>> cad0cd06e96ba923c36e069bba3069896216c126
