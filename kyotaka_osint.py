from modules import ip_lookup, domain_lookup, email_lookup, phone_lookup, username_lookup
import os
import time

def banner():
    os.system('clear')
    print("\033[1;31m")
    print("╔════════════════════════════════════════════╗")
    print("║    \033[1;37mＫＹＯＴＡＫＡ ＯＳＩＮＴ - Terminal Hacker\033[1;31m    ║")
    print("╠════════════════════════════════════════════╣")
    print("║ \033[1;37mOutil OSINT sombre et rapide (by Dan Jersey)\033[1;31m ║")
    print("╚════════════════════════════════════════════╝\033[0m")
    time.sleep(0.8)

def menu():
    print("\n\033[1;32m[ MENU DES OUTILS ]\033[0m")
    print("\033[1;34m1\033[0m - IP Lookup")
    print("\033[1;34m2\033[0m - Domain Lookup")
    print("\033[1;34m3\033[0m - Email Lookup")
    print("\033[1;34m4\033[0m - Phone Number Lookup")
    print("\033[1;34m5\033[0m - Username Lookup")
    print("\033[1;31m6\033[0m - Quitter\n")

def main():
    banner()
    while True:
        menu()
        choix = input("\033[1;33m>>> \033[0m").strip()
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
            print("\n\033[1;31m[+] Fermeture de KYOTAKA OSINT...\033[0m")
            time.sleep(0.5)
            break
        else:
            print("\033[1;31m[!] Choix invalide, réessaie.\033[0m")

if __name__ == "__main__":
    main()