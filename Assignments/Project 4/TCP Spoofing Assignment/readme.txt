I started by downloading the openvpn configuration file.

sudo openvpn --config vvvemuri@asu.edu.conf
Then I set the interface to tap0
sudo tcpdump -i tap0 -w vvvemuri@asu.edu.conf.pcap
```
I have installed virtual machine to complete this assignment and mounted ubuntu 22.04 iso image.
Then I installed python3,scapy and Wireshark using the command prompt.
Wireshark is used as network analyzer to monitor the packets that is been sent through the assigned sources.
Then I created a python script:
First I set the source and destination ports to 13337 
I used vpn_source_address which was my machine vpn (Keeps changing whenever we turn on and off) and the trusted_source_address (given in the assignment).
I also used flag_server which I was getting when I connected to vpn.
Initially, I tried sending couple of times but did not receive the flag back. Then I iterated it in the loop of 1000 times and then the server sent the flag back.
The flag was received through UDP port and I monitored it from Wireshark.
