# modules/email_lookup.py
import requests

API_KEY = "A77Fe6C8ACD9F6BC2E9A74460D1E4579"

def run():
    email = input("Entrer l'adresse email : ").strip()
    url = f"http://apilayer.net/api/check?access_key={API_KEY}&email={email}&smtp=1&format=1"

    try:
        res = requests.get(url)
        data = res.json()

        if "email" not in data:
            print("❌ Erreur dans la réponse de l'API.")
            return

        print("┌─[ Résultat Email Lookup ]")
        print(f"│ Email            : {data.get('email')}")
        print(f"│ Format valide    : {data.get('format_valid')}")
        print(f"│ Domaine          : {data.get('domain')}")
        print(f"│ SMTP check       : {data.get('smtp_check')}")
        print(f"│ MX trouvé        : {data.get('mx_found')}")
        print(f"│ Disposable       : {data.get('disposable')}")
        print(f"│ Email de rôle    : {data.get('role')}")
        print(f"│ Email gratuit    : {data.get('free')}")
        print(f"│ Catch-All        : {data.get('catch_all')}")
        suggestion = data.get('did_you_mean')
        if suggestion:
            print(f"│ Suggestion       : {suggestion}")
        print(f"│ Score fiabilité  : {data.get('score')}")
        print("└─────────────────────────────")

    except Exception as e:
        print("❌ Erreur :", e)
