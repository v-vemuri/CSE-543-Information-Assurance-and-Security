Steps to bypass the source-IP-based authentication scheme:

First, I installed scapy on system from the terminal

Once scapy is installed, I used it to forget UDP packets by running the following command:

scapy -A -d -w udp_email.conf.pcap

1) Used a VPN or proxy to change the IP address to 10.2.4.10.
2) Used a packet sniffer to intercept the flag being sent from FlagServ to the trusted IP address.
3) I then used scapy to forge UDP packets with a source IP of 10.2.4.10. 
4) This however requires that the FlagServ server and the client be on the same network segment.
5) I then received the flag and kept that in flag.txt file
