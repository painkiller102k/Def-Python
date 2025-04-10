from Moodul1 import add_inimene_palgad,delete_inimene_palgad,max_palk,min_palk,keskmine_palk,rich_poor_inimene,search_by_täht,eemalda_alla_keskmise,tulumaks,same_palg,JarjestaPalgad
palgad = [1200, 2500, 750, 395, 1001]
inimesed = ["Martin", "Roman", "Mark", "Marek", "Illia"]

while True:
    print("Menu:")
    print("1. Lisage inimene ja palk")
    print("2. Kustutada inimene ja palk")
    print("3. Näita kõrgeimat palka")
    print("4. Näita väikseimat palka")
    print("5. Näita keskmist palka")
    print("6. Näita kõige rikkamat ja vaesemat inimest")
    print("7. Leia sisestatud tähega nimed ja nende palgad.")
    print("8. Eemaldage inimesed, kelle palk on alla 1000")
    print("9. Arvutage netopalk pärast maksude mahaarvamist")
    print("10. Leia sama palgaga inimesed")
    print("11. Korraldage palgad kasvavas ja kahanevas järjekorras.")
    print("12. Näita nimekirju")
    print("13. Quit")
    
    try:
        choice = int(input("Valige tegevus: "))
        if choice == 1:
            nimi = input("Sisestage nimi: ")
            palk = float(input("Sisestage palk: "))
            add_inimene_palgad(palgad, inimesed, nimi, palk)
            print("Andmed edukalt lisatud!")
        elif choice == 2:
            nimi = input("Sisestage selle isiku nimi, keda soovite kustutada: ")
            delete_inimene_palgad(palgad, inimesed, nimi)
            print(f"Inimene {nimi} ja tema palk on edukalt kustutatud!")
        elif choice == 3:
            nimi, palk = max_palk(palgad, inimesed)
            print(f"Suurim palk {palk} saab {nimi}.")
        elif choice == 4:
            nimi, palk = min_palk(palgad, inimesed)
            print(f"Väikseim palk {palk} saab {nimi}.")
        elif choice == 5:
            keskmine = keskmine_palk(palgad, inimesed)
            print(f"Kõigi inimeste keskmine palk: {keskmine:.2f}")
        elif choice == 6:
            rich_name, rich_salary, poor_name, poor_salary = rich_poor_inimene(palgad, inimesed)
            print(f"Kõige rikkam mees {rich_name} palgaline {rich_salary}")
            print(f"Kõige vaesem mees {poor_name} palgaline {poor_salary}")
        elif choice == 7:
            täht = input("Sisestage täht ").strip()
            tulemused = search_by_täht(palgad, inimesed, täht)
            if tulemused:
                print("Tähega algavad nimed ja palgad", täht)
                for nimi, palk in tulemused:
                    print(f"{nimi} - {palk}")
            else:
                print(f"Ei ole nimesid, mis algavad tähega {täht}.")
        elif choice == 8:
            eemalda_alla_keskmise(palgad, inimesed, 1000)
            print("Inimesed, kelle palk on alla 1000, eemaldatakse nimekirjadest.")
        elif choice == 9:
            nimi = input("Sisestage nimi ")
            netopalk = tulumaks(palgad, inimesed, nimi)
            if netopalk is None:
                print(f"Mees, kellel on nimi {nimi} ei leitud.")
            else:
                print(f"Kättesaadav palk {nimi}: {netopalk:.2f}")
        elif choice == 10:
            results = same_palg(palgad, inimesed)
            for palk, nimed in results.items():
                if len(nimed) > 1:
                    print(f"Palk {palk} saab {len(nimed)} inimene: {', '.join(nimed)}")
        elif choice == 11:
            print("Palgad kasvavas järjekorras:")
            kasvav, kahanev = JarjestaPalgad(palgad, inimesed)
            print("Suurenevas järjekorras:", kasvav)
            print("Kahanevas järjekorras:", kahanev)
        elif choice == 12:
            print("Inimeste nimekiri:", inimesed)
            print("Palgad nimekiri:", palgad)
        elif choice == 13:
            print("Quit")
            break
        else:
            print("Viga: Valige õige menüüpunkt.")
    except ValueError:
        print("Viga")