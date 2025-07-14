# relay_node.py
import socket

def activate_hub():
    hub_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binding to local relay port
    hub_socket.bind(("localhost", 12346))
    hub_socket.listen(1)
    print("🛰️ EchoNode relay is active on port 12346...")

    receiver, address = hub_socket.accept()
    print(f"🔌 Incoming signal from {address}")

    try:
        while True:
            packet = receiver.recv(1024)
            if not packet:
                break
            print(f"📡 Signal captured: {packet.decode()}")
            receiver.send(packet)  # Echo transmission
    except Exception as err:
        print(f"⚠️ Relay disruption detected: {err}")
    finally:
        receiver.close()
        hub_socket.close()
        print("📴 Relay link disengaged.")

if __name__ == "__main__":
    activate_hub()
