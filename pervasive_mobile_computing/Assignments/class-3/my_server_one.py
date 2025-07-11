# command_node.py
import socket
import threading

# Mock clearance database
AUTHORIZED_AGENTS = {
    "echo77": "cipherX",
    "nova9": "zenith42",
    "phantom": "ghostwalk"
}

def process_agent(link, address):
    print(f"🛰️ Comm uplink received from {address}")

    try:
        # Phase 1: Credential decryption
        incoming = link.recv(1024).decode().strip()
        agent_code, clearance = incoming.split(":")

        # Phase 2: Identity confirmation
        if AUTHORIZED_AGENTS.get(agent_code) != clearance:
            link.send("❌ Access denied: invalid credentials.".encode())
            print(f"🚫 Clearance failure for {address} ({agent_code})")
            link.close()
            return

        link.send("✅ Access granted: welcome, agent.".encode())
        print(f"🛡️ Agent {agent_code} verified from {address}")

        # Phase 3: Open signal loop
        while True:
            signal = link.recv(1024)
            if not signal:
                break
            print(f"📡 Intel from {agent_code}: {signal.decode()}")
            link.send(signal)

    except Exception as fault:
        print(f"⚠️ Link disruption with {address}: {fault}")
    finally:
        link.close()
        print(f"📴 Signal link terminated for {address}")

def activate_command_node():
    control_tower = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    control_tower.bind(("localhost", 12347))  # Spy port active
    control_tower.listen(5)
    print("🔐 Command Node monitoring port 12347...")

    try:
        while True:
            channel, origin = control_tower.accept()
            ops_thread = threading.Thread(target=process_agent, args=(channel, origin))
            ops_thread.daemon = True
            ops_thread.start()
    except KeyboardInterrupt:
        print("🛑 Shutdown initiated—Command Node going dark.")
    finally:
        control_tower.close()

if __name__ == "__main__":
    activate_command_node()
