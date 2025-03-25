import random

kasutajad = []
paroolid = [] 

def genereeri_parool(length: int) -> str: #генерация пароля
    """Genereerib parooli
    """
    sümbolid = ".,:;!_*-+()/#¤%&"
    numbrid = '0123456789'
    kirju = 'qwertyuiopasdfghjklzxcvbnm'
    kirju_add = kirju.upper()
    all = sümbolid + numbrid + kirju + kirju_add
    return ''.join(random.choice(all) for i in range(length))

def kontrolli_parooli(password: str) -> bool: #проверка пароля
    """Kontrollib, kas parool vastab nõuetele.
    """
    if (any(i.isdigit() for i in password) and
        any(i.islower() for i in password) and
        any(i.isupper() for i in password) and
        any(i in ".,:;!_*-+()/#¤%&" for i in password)):
        return True #пароль соответствует требованиям
    return False

def registreeri_kasutaja(username: str, password: str) -> bool: #регистрация пользователя
    """Registreerib uue kasutaja.
    """
    if username in kasutajad:
        return False  # пользователь уже есть
    kasutajad.append(username)
    paroolid.append(password)
    return True

def autoriseeri_kasutaja(username: str, password: str) -> bool: #авторизация пользователя
    """Autoriseerib kasutaja.
    """
    if username in kasutajad:
        check = kasutajad.index(username)
        return paroolid[check] == password
    return False

def muuda_parooli(username: str, new_password: str) -> bool: #изменение пароля
    """Muudab kasutaja parooli.
    """
    if username in kasutajad:
        check = kasutajad.index(username)
        paroolid[check] = new_password
        return True #пароль изменен
    return False #пользователь не найден

def unusta_parool(username: str) -> str: #восстановление пароля
    """Luuakse kasutajale uus parool.
    """
    if username in kasutajad:
        check = kasutajad.index(username)
        new_password = genereeri_parool(10)
        paroolid[check] = new_password
        return new_password
