from MoodulDefTest import *
#arithmetic funktsiooni testimine
a=float(input("Sisesta esimene arv: "))
b=float(input("Sisesta teine arv: "))
c=input("Sisesta tehe: ")
v=arithmetic(a,b,c)
print(v)

#is_year_leap funktsiooni testimine
a=int(input("Sisesta aasta: "))
v=is_year_leap(a)
print(v)
if v==True:
    print("Liigaasta")
else:
    print("Tavaline aasta")

#square funktsiooni testimine
s,p,d=square(float(input("Sisesta ruudu kulg: ")))
print("Ruudu pindala on",s)
print("Ruudu ümbermõõt on",p)
print("Ruudu diagonaal on",d)


#season funktsiooni testimine
kuu=int(input("Sisesta kuu number: "))
v= season(kuu)
print(v)

#bank funktsiooni testimine
a=float(input("Sisesta summa: "))
b=int(input("Sisesta aastate arv: "))
v= bank(a, b)
print(v)

#is_prime funktsiooni testimine
a=int(input("Sisesta arv: "))
v=is_prime(a)
print(v)
if v==True:
    print("On algarv")
else:
    print("Ei ole algarv")

#date funktsiooni testimine
p=int(input("Sisesta päev: "))
k=int(input("Sisesta kuu: "))
a=int(input("Sisesta aasta: "))
v=date(p,k,a)
print(v)
if v==True:
    print("Kuupäev on õige")
else:
    print("Kuupäev on vale")

#xor funktsiooni testimine
