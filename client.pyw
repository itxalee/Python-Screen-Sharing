import vidstream
import threading
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description="Screen sharing client")
parser.add_argument("ip", help="Receiver IP address")
parser.add_argument("port", type=int, help="Receiver port number")
args = parser.parse_args()

# Start the screen sharing client
sender = vidstream.ScreenShareClient(args.ip, args.port)

t = threading.Thread(target=sender.start_stream)
t.start()

while input("Type 'STOP' to stop sharing: ").upper() != 'STOP':
    continue

sender.stop_stream()
