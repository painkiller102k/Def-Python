from Moodul import (
    registreeri_kasutaja, autoriseeri_kasutaja, muuda_parooli,
    unusta_parool, kontrolli_parooli, genereeri_parool,
    kasutajad, paroolid, lae_andmed
)

lae_andmed()
print("Tere tulemast!")

while True:
    try:
        print("Menu:")
        print("1. Uue kasutaja registreerimine")
        print("2. Kasutaja autoriseerimine")
        print("3. Parooli muutmine")
        print("4. Parooli taastamine")
        print("5. End")
        valik = input("Teie valik: ")

        if valik == "1":
            print("Uue kasutaja registreerimine:")
            username = input("Sisesta kasutajanimi: ")
            email = input("Sisesta e-mail: ")

            if username in kasutajad:
                print("Selle nimega kasutaja on juba olemas!")
            else:
                print("Valige parooli loomise meetod:")
                print("1. Automaatne salasõna genereerimine")
                print("2. Looge ise parool")
                password_choice = input("Teie valik (1/2): ")

                if password_choice == "1":
                    password = genereeri_parool(8)
                    print(f"Teie genereeritud parool: {password}")
                elif password_choice == "2":
                    while True:
                        password = input("Enter password: ")
                        if kontrolli_parooli(password):
                            break
                        else:
                            print("Parool peab sisaldama numbreid, suur- ja väiketähti ning erimärke.")
                else:
                    print("Vale valik")
                    continue

                if registreeri_kasutaja(username, password, email):
                    print("Kasutaja edukalt registreeritud! Parool saadeti e-mailile.")
                else:
                    print("Registreerimisviga!")

        elif valik == "2":
            print("Kasutaja autoriseerimine:")
            username = input("Enter username: ")
            password = input("Enter password: ")
            if autoriseeri_kasutaja(username, password):
                print("Autoriseerimine õnnestus!")
            else:
                print("Vale kasutajanimi või parool!")

        elif valik == "3":
            print("Parooli muutmine:")
            username = input("Enter username: ")
            old_password = input("Enter old password: ")
            email = input("Enter email: ")
            if autoriseeri_kasutaja(username, old_password):
                while True:
                    new_password = input("Sisestage uus parool: ")
                    if kontrolli_parooli(new_password):
                        if muuda_parooli(username, new_password, email):
                            print("Parool edukalt muudetud! Uus parool saadeti e-mailile.")
                            break
                        else:
                            print("Parooli muutmise viga!")
                    else:
                        print("Parool peab sisaldama numbreid, suur- ja väiketähti ning erimärke.")
            else:
                print("Vale kasutajanimi või vana parool!")

        elif valik == "4":
            print("Parool taastamine:")
            username = input("Enter username: ")
            email = input("Enter email: ")
            new_password = unusta_parool(username, email)
            if new_password:
                print("Uus parool saadeti teie e-mailile!")
            else:
                print("Kasutajat ei leitud!")

        elif valik == "5":
            print("Programm lõpetatud.")
            break
        else:
            print("Vale valik!")

    except ValueError:
        print("Sisestamisviga!")
