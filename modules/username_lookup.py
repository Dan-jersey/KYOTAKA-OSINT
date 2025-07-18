import requests

SITES = {
    "GitHub": "https://github.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "TikTok": "https://www.tiktok.com/@{}",
}

def run():
    username = input("Entrer le pseudo à rechercher : ").strip()
    print(f"┌─[ Recherche du pseudo : {username} ]")

    for site, url in SITES.items():
        try:
            res = requests.get(url.format(username), timeout=10)
            if res.status_code == 200:
                print(f"│ ✅ Trouvé sur {site} : {url.format(username)}")
            elif res.status_code == 404:
                print(f"│ ❌ Pas trouvé sur {site}")
            else:
                print(f"│ ⚠️ Statut {res.status_code} sur {site}")
        except Exception as e:
            print(f"│ ❌ Erreur sur {site} : {e}")

    print("└─────────────────────────────")
