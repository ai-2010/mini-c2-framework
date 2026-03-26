def tcp_only(packet):
    return packet.haslayer('TCP')


def udp_only(packet):
    return packet.haslayer('UDP')


def ip_only(packet):
    return packet.haslayer('IP')
