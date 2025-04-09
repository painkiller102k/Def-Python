def inimesed():
    name = []
    height = []

    while True:
        print("Добавление данных о человеке:")
        nimi = input("Введите имя человека (или напишите 'end' для завершения): ")
        if nimi.lower() == "end":
            break
        if nimi in name:
            print("Человек с таким именем уже существует. Попробуйте другое имя.")
            continue
        try:
            kasv = float(input(f"Введите рост {nimi} (в сантиметрах): "))
            name.append(nimi)
            height.append(kasv)
        except ValueError:
            print("Ошибка: рост должен быть числом. Попробуйте снова.")

def menu():
    print("Меню:")
    print("1. Удалить человека и его рост из списка")
    print("2. Отобразить список людей и их рост в алфавитном порядке")
    print("3. Найти самого высокого и самого низкого человека")
    print("4. Найти средний рост выбранных людей")
    print("5. Выход")

