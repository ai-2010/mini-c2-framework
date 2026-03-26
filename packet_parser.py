from scapy.all import IP, TCP, UDP


def parse_packet(packet):
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst
        proto = packet[IP].proto
        payload = bytes(packet.payload)
        print(f'Source: {src} | Destination: {dst} | Protocol: {proto} | Payload-size: {len(payload)}')

        if TCP in packet:
            print('  TCP', packet[TCP].sport, '->', packet[TCP].dport)
        elif UDP in packet:
            print('  UDP', packet[UDP].sport, '->', packet[UDP].dport)
