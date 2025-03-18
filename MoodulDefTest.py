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

def is_year_leap(aasta: int) -> bool:
    """ Liigaasta leidmine
    Tagastab True, kui aasta on liigaasta ja False kui on tavaline aasta
    :param int aasta: aasta number
    :rtype: bool True or False
    """
    if aasta%4==0:
        v= True # or return True
    else:
        v= False # or return False
        return v
    

def square(kulg=1:float) -> any:
""" Ruut
Kirjutage ruutfunktsioon, "
"mis võtab 1 argumendi, "
"ruudu külje, ja tagastab 3 väärtust: "
"ruudu ümbermõõt, ruudu pindala ja ruudu diagonaal."
    """
s=kulg**2
p=4*kulg
d=(2)**(1/2)*kulg
return s,p,d
