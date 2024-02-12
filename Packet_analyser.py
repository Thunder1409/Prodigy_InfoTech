from scapy.all import sniff, IP, UDP, TCP, ICMP, ARP, Raw

def packet_callback(packet):
    # print(packet.show())

    if IP in packet:
        src_ip = packet[IP].src
        des_ip = packet[IP].dst

        print("Source IP -: ", src_ip)
        print("Destination IP -: ", des_ip)


    protocol = "Other"
    if UDP in packet:
        protocol = "UDP"

    elif TCP in packet:
        protocol = "TCP"

    elif ICMP in protocol:
        protocol = "ICMP"

    elif ARP in protocol:
        protocol = "ARP"

    else:
        pass

    print("Protocol -: ", protocol)

    if Raw in packet:
        print("Data -: ", packet[Raw].load.hex())



sniff(prn=packet_callback, filter="ip", count=1) #change number of packet you want to count