# messenger.py
import socket

def launch_transmitter():
    transmitter = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Updated to connect to local message hub on port 12346
    transmitter.connect(("localhost", 12346))
    print("📡 Link established with EchoNode server.")

    payload = input("📥 Compose your transmission: ")
    transmitter.send(payload.encode())

    reply = transmitter.recv(1024)
    print(f"🔁 Response from EchoNode: {reply.decode()}")

    transmitter.close()

if __name__ == "__main__":
    launch_transmitter()
