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