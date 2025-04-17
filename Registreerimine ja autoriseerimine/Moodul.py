import random
import smtplib
from email.message import EmailMessage
import os

kasutajad = []
paroolid = []

FILENAME = "userss.txt"

def lae_andmed():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            for line in f:
                user, pwd = line.strip().split(";")
                kasutajad.append(user)
                paroolid.append(pwd)

def salvesta_andmed():
    with open(FILENAME, "w") as f:
        for user, pwd in zip(kasutajad, paroolid):
            f.write(f"{user};{pwd}\n")

def saada_email(to_email: str, subject: str, body: str):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "rossakovmartin@gmail.com"
    msg["To"] = to_email
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("rossakovmartin@gmail.com", "ruef afxj zzau whig")
            smtp.send_message(msg)
    except Exception as e:
        print("E-maili saatmise viga:", e)

def genereeri_parool(length: int) -> str:
    sümbolid = ".,:;!_*-+()/#¤%&"
    numbrid = '0123456789'
    kirju = 'qwertyuiopasdfghjklzxcvbnm'
    kirju_add = kirju.upper()
    all = sümbolid + numbrid + kirju + kirju_add
    return ''.join(random.choice(all) for i in range(length))

def kontrolli_parooli(password: str) -> bool:
    if (any(i.isdigit() for i in password) and
        any(i.islower() for i in password) and
        any(i.isupper() for i in password) and
        any(i in ".,:;!_*-+()/#¤%&" for i in password)):
        return True
    return False

def registreeri_kasutaja(username: str, password: str, email: str) -> bool:
    if username in kasutajad:
        return False
    kasutajad.append(username)
    paroolid.append(password)
    salvesta_andmed()
    saada_email(email, "Registreerimine õnnestus", f"Tere {username}, sinu parool on: {password}")
    return True

def autoriseeri_kasutaja(username: str, password: str) -> bool:
    if username in kasutajad:
        check = kasutajad.index(username)
        return paroolid[check] == password
    return False

def muuda_parooli(username: str, new_password: str, email: str) -> bool:
    if username in kasutajad:
        check = kasutajad.index(username)
        paroolid[check] = new_password
        salvesta_andmed()
        saada_email(email, "Parool muudetud", f"Tere {username}, sinu uus parool on: {new_password}")
        return True
    return False

def unusta_parool(username: str, email: str) -> str:
    if username in kasutajad:
        check = kasutajad.index(username)
        new_password = genereeri_parool(10)
        paroolid[check] = new_password
        salvesta_andmed()
        saada_email(email, "Parooli taastamine", f"Tere {username}, sinu uus parool on: {new_password}")
        return new_password
    return None
