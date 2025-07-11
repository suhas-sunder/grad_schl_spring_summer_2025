# operative_link.py
import socket

def initiate_uplink():
    uplink_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    uplink_socket.connect(("localhost", 12347))
    print("🛡️ Secure channel established with Command Node.")

    # Step 1: Transmit agent credentials
    agent_id = input("Agent ID: ")
    access_key = input("Access Key: ")
    auth_payload = f"{agent_id}:{access_key}"
    uplink_socket.send(auth_payload.encode())

    # Step 2: Await authorization
    confirmation = uplink_socket.recv(1024).decode()
    print(confirmation)

    if not confirmation.startswith("✅"):
        uplink_socket.close()
        return

    # Step 3: Send mission report
    transmission = input("🎤 Transmit field report: ")
    uplink_socket.send(transmission.encode())
    mirrored = uplink_socket.recv(1024)
    print(f"📡 Mirror confirmed: {mirrored.decode()}")

    uplink_socket.close()

if __name__ == "__main__":
    initiate_uplink()
