#
try:
    p=int(input("Mis päev täna on "))
except:
    print("Ei, see on viga!")
if  p==1:
    print("Esmaspäev")
elif p==2:
    print("Teisepäev")
elif p==3:
    print("Kolmapäev")
elif p==4:
    print("Neljapäev")
elif p==5:
    print("Reede")
elif p==6:
    print("Laupäev")
elif p==7:
    print("Puhapäev")
else:
    print("Vale!")


#12/12/22 Valikud
try:
    hinne=int(input("Mis hinne täna sai koolis: "))
except:
    print("!!")
if hinne==5:
    print("Tubli!")
elif hinne==4:
    print("Hea! ")
elif hinne==3:
    print("Rahuldav!")
elif hinne==2 or hinne==1:
    print("Mitte rahuldav!")
else:
    print("Viga!")






#10
from math import *
try:
    a=float(input("Sisestab aja minutites: "))
except: ("VALE!")
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
try:
    l=float(input("kütuse liitrid: "))
except:
    ("Viga!")
try:
    km=float(input("sisestab läbitud kilomeetrid: "))
except:
    ("Viga!")
S=(l/km)*100
print(f"leiab kütusekulu 100km kohta keskmiselt on {l}")

#7
from math import *
print ("suure pitsa hinnaga 12,90")
b=12,90*10/100 # Hind
print(f"Jotraha maksb {b} ")
p=1,29/3
print(f"Iga õks maksb {p} ")

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
try:
    a=int(input("Kirjuta aritmeetilise jaoks a: ")) # küsi artimeetlise
except:
    ("Vale andmetüpp!  ")
    a=0
try:
    b=int(input("Kirjuta aritmeetilise jaoks b:"))
except:
    ("Vale andmetüpp!  ")
try:
    c=int(input("Kirjuta aritmeetilise jaoks c:"))
except:
    ("Vale andmetüpp!  ")
try:
    d=int(input("Kirjuta aritmeetilise jaoks d:"))
except:
    ("Vale andmetüpp!  ")
try:
    e=int(input("Kirjuta aritmeetilise jaoks e:"))
except:
    ("Vale andmetüpp!  ")
Keskmine=5/(a+b+c+d+e)# arvutage
print(f"Vastus: {Keskmine}")# kirjuta vastus

#3
from math import * # lisa rida 
aeg=float(input("Mitu Tundi kulus sõiduks? "))# eemaldatud tühik
teepikkus=float(input("Mitu kilomeetrit sõitsid? "))# eemaldatud tühik
kiirus=aeg/teepikkus# eemaldatud tühik
print(f"Vastus: sinu kirrus oli {kiirus}, Kilomeetrir sõitsid round {teepikkus}")# lisa vastud. Print("Sinu kiirus oli {kirrus} "+str(kiirus)" km/h")

#2
print("Arvutage diagonaal pikk")
try:
    N=float(input("siseta ristküliku 1. külje pikkus => "))
except:
    ("Vale!")
try:
    M=float(input("siseta ristküliku 2. külje pikkus => "))
except:
    ("Vale!")
d=sqrt(N**2+M**2)
print=(f"Maatüki on diagonaal on {d} m**2")# vastus

#1
print("Puu ümbermõõdu arvutamine")# arvutage ümbermõõdu
C=float(input("Puu ümbermõõt"))# otsima C
d=2*(C/(2*pi))# arvutage diagonaal
print(f"Vastus:\nPuu läbimõõduga {C} ümbermõõt võrdub {d}")# vastus


