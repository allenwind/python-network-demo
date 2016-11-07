import os

from scapy.all import *

captured_data = dict()

end_port = 100

def monitor(pkt):
	if IP in pkt:
		if pkt[IP].src not in captured_data:
			captured_data[pkt[IP].src] = []

	if TCP in pkt:
		if pkt[TCP].sport <= end_port:
			if not str(pkt[TCP].sport) in captured_data([pkt[IP].src]:
			captured_data[pkt[IP].src].append(str(pkt[TCP].sport))
