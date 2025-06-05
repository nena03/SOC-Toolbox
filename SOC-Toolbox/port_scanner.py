import socket
from datetime import datetime

def port_scan(target, port_range=(1, 1024)):
    print(f"[+] Pokrećem skeniranje za: {target}")
    print(f"[+] Vreme početka: {datetime.now()}")
    print(f"[+] Portovi: {port_range[0]}-{port_range[1]}")
    print("-" * 40)

    for port in range(port_range[0], port_range[1] + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Nepoznat servis"
                print(f"[OPEN] Port {port}: {service}")

    print("-" * 40)
    print(f"[+] Kraj skeniranja: {datetime.now()}")

if __name__ == "__main__":
    target_host = input("Unesi IP adresu ili domen za skeniranje: ").strip()
    port_scan(target_host, (1, 100))
