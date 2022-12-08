#10
from math import *
a=float(input("Sisestab aja minutites: "))
t=a/60
print(f"Kell {t}")

#9
from math import *
print("Keskmist kiruus on 29,9 km/h, V=29,9 km/h, m=24, arvutage: t=24/60")
V=29,9
m=24
t=24/60
print(f"Vastus: t= {t}")

#8
from math import *
l=float(input("kütuse liitrid: "))
km=float(input("sisestab läbitud kilomeetrid: "))
S=(l/km)*100
print(f"leiab kütusekulu 100km kohta keskmiselt on {l}")

#7
from math import *
print ("suure pitsa hinnaga 12,90")
a=10 # see on 10%
b=12,90 # Hind
c=100 #100%
d=(a*b) #arvutage # siin mul on problemi, millal ma lõpsima sümbol / , nii ei tööta.
print(f"Vatus: peab igaüks maksma {d}")

#6
from math import *
from random import * # kaäsk jaoks random
a=randint(1,80)
b=randint(1,80)
c=randint(1,80)
print(f"Külg a= {a}\nKülg b={b}\nKülg c= {c}")
print(f"Kolmnurga ümbermõõt = {a+b+c}")

#5
print("   @..@") # lisa kolm tühik
print("  (----)")# lisa tühik
print(" ( \__/ )")#lisa tühik
print("  ^^ "" ^^")#lisa tühik

#4
from math import *
a=int(input("Kirjuta aritmeetilise jaoks a: ")) # küsi artimeetlise
b=int(input("Kirjuta aritmeetilise jaoks b:"))
c=int(input("Kirjuta aritmeetilise jaoks c:"))
d=int(input("Kirjuta aritmeetilise jaoks d:"))
e=int(input("Kirjuta aritmeetilise jaoks e:"))
Keskmine=5/(a+b+c+d+e)# arvutage
print(f"Vastus: {Keskmine}")# kirjuta vastus

#3
from math import * # lisa rida 
aeg=float(input("Mitu Tundi kulus sõiduks? "))# eemaldatud tühik
teepikkus=float(input("Mitu kilomeetrit sõitsid? "))# eemaldatud tühik
kiirus=aeg/teepikkus# eemaldatud tühik
print(f"Vastus: sinu kirrus oli {kiirus}, Kilomeetrir sõitsid round {teepikkus}")# lisa vastud. Print("Sinu kiirus oli {kirrus} "+str(kiirus)" km/h")

#2
from math import *
print("Arvutage diagonaal pikk")
N=float(input("siseta ristküliku 1. külje pikkus => "))
M=float(input("siseta ristküliku 2. külje pikkus => "))
d=sqrt(N**2+M**2)
print=(f"Maatüki on diagonaal on {d} m**2")# vastus

#1
from math import *
print("Puu ümbermõõdu arvutamine")# arvutage ümbermõõdu
C=float(input("Puu ümbermõõt"))# otsima C
d=2*(C/(2*pi))# arvutage diagonaal
print(f"Vastus:\nPuu läbimõõduga {C} ümbermõõt võrdub {d}")# vastus


