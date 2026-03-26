from scapy.all import sniff
from packet_parser import parse_packet


def main():
    print('Packet sniffer ishga tushdi. CTRL+C bilan to‘xtating.')
    sniff(prn=parse_packet, store=False)


if __name__ == '__main__':
    main()
