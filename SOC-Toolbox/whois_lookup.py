import socket

def whois_lookup(domain):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("whois.iana.org", 43))
    s.send((domain + "\r\n").encode())

    response = b""
    while True:
        data = s.recv(4096)
        if not data:
            break
        response += data
    s.close()
    print(response.decode())

if __name__ == "__main__":
    domain = input("Unesi domen za WHOIS proveru: ").strip()
    whois_lookup(domain)
