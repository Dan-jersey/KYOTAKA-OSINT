from modules import ip_lookup, domain_lookup, email_lookup, phone_lookup, username_lookup

def main():
    print("┌─[ KYOTAKA OSINT ]")
    print("│ Outil OSINT sombre et rapide")
    print("└──────────────────────────────")

    while True:
        print("\nChoisis un outil :")
        print("1. IP Lookup")
        print("2. Domain Lookup")
        print("3. Email Lookup")
        print("4. Phone Number Lookup")
        print("5. Username Lookup")
        print("6. Quitter")

        choix = input("> ").strip()

        if choix == "1":
            ip_lookup.run()
        elif choix == "2":
            domain_lookup.run()
        elif choix == "3":
            email_lookup.run()
        elif choix == "4":
            phone_lookup.run()
        elif choix == "5":
            username_lookup.run()
        elif choix == "6":
            print("Bye !")
            break
        else:
            print("Choix invalide, réessaie.")

if __name__ == "__main__":
    main()
