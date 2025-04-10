palgad=[1200,2500,750,395,1201]
inimesed=["Martin","Roman","Mark","Marek","Illia"]

def add_inimene_palgad(palgad: list, inimesed: list, nimi: str, palk: float):
    """Lisа inimene ja tema palk.
    """
    inimesed.append(nimi)
    palgad.append(palk)

def delete_inimene_palgad(palgad: list, inimesed: list, nimi: str):
    """Kustuta inimene ja tema palk.
    """
    if nimi in inimesed:
        index = inimesed.index(nimi)
        del inimesed[index]
        del palgad[index]
    else:
        print("Inimene ei leitud.")

def max_palk(palgad: list, inimesed: list):
    """Leiab suurima palga ja selle saaja.
    """
    max_palk = max(palgad)
    index = palgad.index(max_palk)
    return inimesed[index], max_palk

def min_palk(palgad: list, inimesed: list):
    """Leiab väikseima palga ja selle saaja.
    """
    min_palk = min(palgad)
    index = palgad.index(min_palk)
    return inimesed[index], min_palk

def keskmine_palk(palgad: list, inimesed: list) -> float:
    """Näitab keskmist palka, kui kasutaja sisestab nime.
    Отображает среднюю зарплату, когда пользователь вводит имя.
    """
    return sum(palgad) / len(palgad)

def rich_poor_inimene(palgad: list, inimesed: list):
    """Leiab kõige rikkama ja kõige vaesema inimese.
    Находит самого богатого и самого бедного человека.
    """
    max_index = palgad.index(max(palgad))
    min_index = palgad.index(min(palgad))
    return inimesed[max_index], palgad[max_index], inimesed[min_index], palgad[min_index]

def search_by_täht(palgad: list, inimesed: list, täht: str):
    """Leiab nimed, mis algavad antud tähega, ja nende palgad.
    Находит имена, начинающиеся на заданную букву, и их зарплаты.
    """
    tulemused = []
    for i in range(len(inimesed)):
        if inimesed[i].startswith(täht):
            tulemused.append((inimesed[i], palgad[i]))
    return tulemused

def eemalda_alla_keskmise(palgad: list, inimesed: list, piir: float = 1000):
    """Eemaldab inimesed, kelle palk on alla antud piiri.
    Удаляет людей, чья зарплата ниже средней
    """
    i = 0
    while i < len(palgad):
        if palgad[i] < piir:
            del palgad[i]
            del inimesed[i]
        else:
            i += 1


def tulumaks(palgad: list, inimesed: list, nimi: str) -> float:
    """Arvutab inimese netopalga pärast tulumaksu mahaarvamist.
    Рассчитывает чистую зарплату человека после вычета подоходного налога.
    """
    if nimi not in inimesed:
        return None 

    index = inimesed.index(nimi)
    brutopalk = palgad[index]
    netopalk = brutopalk * 0.8  # проходный налог 20% !!
    return netopalk

def JarjestaPalgad(palgad: list, inimesed: list):
    """
    Järjestab palgad kasvavas ja kahanevas järjekorras koos nimedega.
    показывает зарплаты по возрастанию и убыванию
    """
    kasvav = sorted(zip(palgad, inimesed))
    kahanev = sorted(zip(palgad, inimesed), reverse=True) # возвращает true для сортировки по убыванию
    return kasvav, kahanev

def same_palg(palgad: list, inimesed: list):
    """Et teada saada, kes saab sama palka, leidke, kui palju selliseid inimesi nende andmeid ekraanile kuvada.
    Узнать кто получает одинаковую зарплату
    """
    grupid = []
    for palk, nimi in zip(palgad, inimesed):
        for i in grupid:
            if i[0] == palk:
                i[1].append(nimi)
                break
        else:
            grupid.append([palk, [nimi]])
    return grupid
