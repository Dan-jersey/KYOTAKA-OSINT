import requests
import os

def get_network_info():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()

        ip = data.get("ip", "N/A")
        hostname = data.get("hostname", "N/A")
        city = data.get("city", "N/A")
        region = data.get("region", "N/A")
        country = data.get("country", "N/A")
        org = data.get("org", "N/A")
        loc = data.get("loc", "N/A")

        result = f"""
╭─[ 📡 KYOTAKA HOST FINDER ]─╮
├ IP        : {ip}
├ HOSTNAME  : {hostname}
├ ORGANISME : {org}
├ LOCALISATION : {city}, {region}, {country}
├ COORDONNÉES  : {loc}
╰────────────────────────────╯
"""

        print(result)

    except Exception as e:
        print(f"[❌] Erreur : {e}")

if __name__ == "__main__":
    os.system("clear")
    print("📡 Récupération des données réseau...")
    get_network_info()