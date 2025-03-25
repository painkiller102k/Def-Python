def arithmetic(arv1: float, arv2: float, tehe: str) -> any:
    """ Lihtne kalkulaator
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float arv1: Sisend kasutajalt, mingi ujukomaarv arv
    :param float arv2: Sisend kasutajalt, mingi ujukomaarv arv
    :param str tehe: aritmeetiline tehe, mis valib kasutaja
    :rtype: var Määrata tuup ( float or str )
    """
    if tehe in ["+", "-", "*", "/"]:
        if arv2==0 and tehe=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(arv1)+tehe+str(arv2))
    else:
        vastus="Tundmatu tehe"
    return vastus

def is_year_leap(aasta:int)->bool:
    """Liigaasta leidmine 
    Tagastab True, kui liigaasta ja False kui on tavaline aasta.
    :param int aasta: aasta number
    :rtype: bool tagastab tõeväärsuses formaadis tulemus
    """
    if aasta%4==0:
        v=True
    else:
        v=False
    return v
    

def square(külg:float)->any:
    """(Ruut)
    Kirjutage ruutfunktsioon, "
    "mis võtab 1 argumendi, "
    "ruudu külje, ja tagastab 3 väärtust: "
    "ruudu ümbermõõt, ruudu pindala ja ruudu diagonaal."
    """
    S=külg**2
    P=külg*4
    d=(2)**(1/2)*külg
    return S,P,d
def square_list(külg:float)->list:
    """(Ruut)
    Kirjutage ruutfunktsioon, "
    "mis võtab 1 argumendi, "
    "ruudu külje, ja tagastab 3 väärtust: "
    "ruudu ümbermõõt, ruudu pindala ja ruudu diagonaal."
    """
    S=külg**2
    P=külg*4
    d=(2)**(1/2)*külg
    s_list=[S,P,d]
    return s_list

def season (kuu:int)->str:
    """(Aastaajad)
    Kirjutage funktsioon season, mis võtab argumendiks kuu numbri (1-12) ja tagastab, 
    millises aastaajas see kuu asub. 
    """
    if kuu in [12,1,2]:
        aastaaeg="Talv" # зима
    elif kuu in [3,4,5]:
        aastaaeg="Kevad" # весна
    elif kuu in [6,7,8]:
        aastaaeg="Suvi" # лето
    elif kuu in [9,10,11]:
        aastaaeg="Sügis" # осень
    else:
        aastaaeg="Tundmatu kuu" # неизвестный месяц
    return aastaaeg

def bank (a: float, years: int) -> float:
    """Pangahoius
    Kasutaja teeb euro suuruse hoiuse aastateks 10% aastas (igal aastal suureneb tema hoiuse suurus 10% võrra). 
    See raha lisandub hoiuse summale ja teenib ka järgmisel aastal intressi).
    """
    for i in range(years):
        a+=a*1.10
    return round(a,2)

def is_prime(n:int) -> bool:
    """(Kas on algarv?)
    Kirjutage funktsioon is_prime, mis võtab argumendiks ühe arvu ja tagastab tõeväärtuse vastavalt sellele, kas antud arv on algarv või mitte.
    """
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def date (p:int, k:int, a:int) -> str:
    """Kirjutage kuupäevafunktsioon, 
    mis võtab 3 argumenti - päev, kuu ja aasta.
    Tagastage True, kui selline kuupäev on meie kalendris ja muidu False.
    """
    try:
        import datetime
        datetime.date(a,k,p)
        return True
    except ValueError:
        return False
    

def X0R_cipher(s:int, k:int) -> str:
    """XOR_cipher
    Kirjutage XOR_cipher funktsioon, mis võtab 2 argumenti:
    krüpteeritav string ja krüpteerimisvõti, mis tagastab stringi, mis on krüpteeritud,
    rakendades XOR (^) funktsiooni stringi märkidele koos võtmega.
    """
    encrypted = ''.join([chr(ord(char) ^ k) for char in s])
    return encrypted

def XOR_uncipher(s: str, k: int) -> str:
    """XOR_cipher
    Kirjutage XOR_cipher funktsioon, mis võtab 2 argumenti:
    krüpteeritav string ja krüpteerimisvõti, mis tagastab stringi, mis on krüpteeritud,
    rakendades XOR (^) funktsiooni stringi märkidele koos võtmega.
    """
    decrypted = ''.join([chr(ord(char) ^ k) for char in s])
    return decrypted