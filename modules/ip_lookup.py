# modules/ip_lookup.py
import requests

API_KEY = "7ae032e10ed34bd4ac31b0dbc1299376"

def run():
    ip = input("Entrer l'adresse IP : ").strip()
    url = f"https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip={ip}"
    try:
        res = requests.get(url)
        data = res.json()
        if "message" in data:
            print(f"❌ Erreur API : {data['message']}")
            return

        print("┌─[ Résultat IP ]")
        print(f"│ IP           : {data.get('ip')}")
        print(f"│ Pays         : {data.get('country_name')} ({data.get('country_code2')})")
        print(f"│ Région       : {data.get('state_prov')}")
        print(f"│ Ville        : {data.get('city')}")
        print(f"│ Code postal  : {data.get('zipcode')}")
        print(f"│ Latitude     : {data.get('latitude')}")
        print(f"│ Longitude    : {data.get('longitude')}")
        print(f"│ Fuseau horaire : {data.get('time_zone', {}).get('name')}")
        print(f"│ ASN          : {data.get('asn')}")
        print(f"│ Organisation : {data.get('organization')}")
        print(f"│ ISP          : {data.get('isp')}")
        print(f"│ Domaine      : {data.get('domain')}")
        currency = data.get('currency', {})
        print(f"│ Currency     : {currency.get('name')} ({currency.get('code')})")
        print(f"│ Map          : https://www.google.com/maps/search/?api=1&query={data.get('latitude')},{data.get('longitude')}")
        print("└───────────────────────")

    except Exception as e:
        print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    run()
