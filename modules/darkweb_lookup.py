import requests
from bs4 import BeautifulSoup

def darkweb_lookup():
    print("\n[🌑] Recherche sur le dark web via Ahmia")
    query = input("⤷ Mot-clé à rechercher : ").strip()

    if not query:
        print("[-] Aucun mot-clé fourni.")
        return

    print(f"[⏳] Recherche de « {query} » sur le dark web...")

    url = f"https://ahmia.fi/search/?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.find_all("a", href=True)

        onion_links = []

        for link in results:
            href = link['href']
            if ".onion" in href:
                onion_links.append(href)

        if onion_links:
            print(f"\n[✓] Résultats trouvés ({len(onion_links)} liens) :\n")
            for i, link in enumerate(set(onion_links), 1):
                print(f"{i}. {link}")
        else:
            print("[-] Aucun lien .onion trouvé.")

    except Exception as e:
        print(f"[!] Erreur lors de la recherche : {e}")

if __name__ == "__main__":
    darkweb_lookup()