import socket

def query_whois(domain):
    server = "whois.verisign-grs.com"  # serveur pour .com, .net etc.
    if domain.endswith(".org"):
        server = "whois.pir.org"
    elif domain.endswith(".io"):
        server = "whois.nic.io"
    # ajoute d'autres TLD si besoin

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(10)
        s.connect((server, 43))
        s.send((domain + "\r\n").encode())
        response = b""
        while True:
            data = s.recv(4096)
            if not data:
                break
            response += data
    return response.decode(errors="ignore")

def run():
    domain = input("Entrer le nom de domaine (ex: example.com) : ").strip()
    print("┌─[ Whois Résultat brut ]")
    try:
        result = query_whois(domain)
        print(result)
    except Exception as e:
        print("❌ Erreur :", e)
    print("└──────────────────────────")
