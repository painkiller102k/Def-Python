from Moodul1 import add_inimene_palgad,delete_inimene_palgad,max_palk,min_palk,keskmine_palk,rich_poor_inimene,search_by_täht,eemalda_alla_keskmise,tulumaks,same_palg,JarjestaPalgad
palgad = [1200, 2500, 750, 395, 1001]
inimesed = ["Martin", "Roman", "Mark", "Marek", "Illia"]

while True:
    print("\nМеню:")
    print("1. Добавить человека и зарплату")
    print("2. Удалить человека и зарплату")
    print("3. Показать самую большую зарплату")
    print("4. Показать самую маленькую зарплату")
    print("5. Показать среднюю зарплату")
    print("6. Показать самого богатого и самого бедного человека")
    print("7. Найти имена на введённую букву и их зарплаты")
    print("8. Удалить людей с зарплатой ниже 1000")
    print("9. Рассчитать чистую зарплату после налога")
    print("10. Найти людей с одинаковой зарплатой")
    print("11. Упорядочить зарплаты по возрастанию и убыванию")
    print("12. Показать списки")
    print("13. Выйти")
    
    try:
        choice = int(input("Выберите действие: "))
        if choice == 1:
            nimi = input("Введите имя человека: ")
            palk = float(input("Введите зарплату: "))
            add_inimene_palgad(palgad, inimesed, nimi, palk)
            print("Данные успешно добавлены!")
        elif choice == 2:
            nimi = input("Введите имя человека, которого хотите удалить: ")
            delete_inimene_palgad(palgad, inimesed, nimi)
            print(f"Человек {nimi} и его зарплата успешно удалены!")
        elif choice == 3:
            nimi, palk = max_palk(palgad, inimesed)
            print(f"Самую большую зарплату {palk} получает {nimi}.")
        elif choice == 4:
            nimi, palk = min_palk(palgad, inimesed)
            print(f"Самую маленькую зарплату {palk} получает {nimi}.")
        elif choice == 5:
            keskmine = keskmine_palk(palgad, inimesed)
            print(f"Средняя зарплата всех людей: {keskmine:.2f}")
        elif choice == 6:
            rich_name, rich_salary, poor_name, poor_salary = rich_poor_inimene(palgad, inimesed)
            print(f"Самый богатый человек: {rich_name} с зарплатой {rich_salary}")
            print(f"Самый бедный человек: {poor_name} с зарплатой {poor_salary}")
        elif choice == 7:
            täht = input("Введите букву: ").strip()
            tulemused = search_by_täht(palgad, inimesed, täht)
            if tulemused:
                print("Имена и зарплаты, начинающиеся на букву", täht)
                for nimi, palk in tulemused:
                    print(f"{nimi} - {palk}")
            else:
                print(f"Нет имён, начинающихся на букву {täht}.")
        elif choice == 8:
            eemalda_alla_keskmise(palgad, inimesed, 1000)
            print("Люди с зарплатой ниже 1000 удалены из списков.")
        elif choice == 9:
            nimi = input("Введите имя человека: ")
            netopalk = tulumaks(palgad, inimesed, nimi)
            if netopalk is None:
                print(f"Человек с именем {nimi} не найден в списке.")
            else:
                print(f"Зарплата на руки для {nimi}: {netopalk:.2f}")
        elif choice == 10:
            results = same_palg(palgad, inimesed)
            for palk, nimed in results.items():
                if len(nimed) > 1:
                    print(f"Зарплата {palk} получают {len(nimed)} человека(человек): {', '.join(nimed)}")
        elif choice == 11:
            print("Зарплаты по возрастанию:")
            kasvav, kahanev = JarjestaPalgad(palgad, inimesed)
            print("По возрастанию:", kasvav)
            print("По убыванию:", kahanev)
        elif choice == 12:
            print("Список людей:", inimesed)
            print("Список зарплат:", palgad)
        elif choice == 13:
            print("Выход из программы.")
            break
        else:
            print("Ошибка: выберите корректный пункт меню.")
    except ValueError:
        print("Ошибка: введите корректное числовое значение.")