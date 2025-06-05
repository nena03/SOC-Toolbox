import requests

def check_ip(ip):
    print(f"Provera reputacije IP adrese: {ip}")
    print("Napomena: Ovo je lažna provera (offline demo).")
    if ip.startswith("192.168.") or ip.startswith("10.") or ip.startswith("172."):
        print("Lokalna IP adresa – sigurno.")
    else:
        print("Nepoznata IP – reputacija nepoznata.")

if __name__ == "__main__":
    ip = input("Unesi IP adresu: ").strip()
    check_ip(ip)
