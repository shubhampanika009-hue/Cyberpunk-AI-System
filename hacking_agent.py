# Ethical Hacking & Security Scan Agent
import socket

def basic_port_scan(target_ip):
    print(f"[Hacking Agent] लक्ष्य {target_ip} पर सुरक्षा पोर्ट स्कैन शुरू किया जा रहा है...")
    common_ports = [21, 22, 80, 443, 8080]
    
    for port in common_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"[+] पोर्ट {port}: खुला (Open)")
            else:
                print(f"[-] पोर्ट {port}: बंद (Closed)")
            sock.close()
        except Exception as e:
            print(f"त्रुटि: {e}")

if __name__ == "__main__":
    print("🛡️ Ethical Hacking Agent एक्टिव है।")
    target = "127.0.0.1"  # लोकल होस्ट
    basic_port_scan(target)
