
from scapy.all import sniff, IP, Raw
def get_protocol_name(proto_num):
     protocols = {1: "ICMP", 6: "TCP", 17: "UDP"} 
     return protocols.get(proto_num, f"Other ({proto_num})")
def packet_callback(packet): 
    if packet.haslayer(IP): 
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst 
        protocol = get_protocol_name(packet[IP].proto)
        log_entry = f"[+] {protocol} | Source: {src_ip} -> Destination: {dst_ip}"
        if packet.haslayer(Raw): 
            payload = packet[Raw].load 
            log_entry += f" | Payload: {payload[:30]}" 
            print(log_entry)
            with open("sniffer_log.txt", "a") as f:
                 f.write(log_entry + "\n") 
print("Starting Network Sniffer...")
print("Press Ctrl+C to stop.\n")
sniff(prn=packet_callback, store=False) 

