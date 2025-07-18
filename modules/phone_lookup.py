# modules/phone_lookup.py
import phonenumbers
from phonenumbers import geocoder, carrier, timezone as tz

def run():
    raw = input("Entrer le numéro (ex: +243833389567) : ").strip()

    try:
        num = phonenumbers.parse(raw, None)
    except phonenumbers.NumberParseException:
        print("❌ Numéro invalide (format invalide)")
        return

    valid = phonenumbers.is_valid_number(num)
    if not valid:
        print("❌ Numéro non valide.")
        return

    intl = phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    country = geocoder.description_for_number(num, "fr")
    oper = carrier.name_for_number(num, "fr")
    zones = tz.time_zones_for_number(num)

    print("┌─[ Résultat Phone Lookup ]")
    print(f"│ Numéro international : {intl}")
    print(f"│ Valide               : {valid}")
    print(f"│ Pays/Localisation    : {country}")
    print(f"│ Opérateur            : {oper or 'N/A'}")
    print(f"│ Fuseau(x) horaire    : {', '.join(zones) or 'N/A'}")
    print("└─────────────────────────")
