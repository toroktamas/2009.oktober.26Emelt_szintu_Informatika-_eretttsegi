#!/usr/bin/python3
#-*- coding:utf-8-*-
print("1. feladat")
"""Beimportalni az adatokat amik a forgalom.txt fajlban vannak amik a forgalomszamlalasrol szolnak.Szerintem szotarba kellene
beimportalni az adatokat ami a kovetkezo keppen nezne ki

forgalom{
hanyadik athalado auto{
"Behajtas ideje":datetime
"Kihajtas ideje":datetime
"Melyik varosbol jott":F vagy A
 }
}
"""
from datetime import datetime
n = 0
hanyadik = 0
forgalom = {}
osszesen = int()
with open("forgalom.txt", "rt+", encoding="utf-8") as f:
    for s in f:
        sor = s.replace("\n", "").split(" ")
        n+=1
        hanyadik+=1
        if n == 1:
            osszesen = sor
        if n!=1:    
            key = hanyadik - 1
            forgalom[key] = {}
            forgalom[key]["Behajtas ideje"] = datetime(1990, 1, 1, int(sor[0]), int(sor[1]), int(sor[2]))
            forgalom[key]["Kihajtas ideje"] = forgalom[key]["Behajtas ideje"].second + int(sor[3])
            
            if sor[4] == "F":
                forgalom[key]["Varosbol jon"] = "Felso"
            if sor[4] == "A":
                forgalom[key]["Varosbol jon"] = "Also"

            forgalom[key]["m/s"] = ((int(sor[3]) - int(sor[2]))/1000)

#print(forgalom)
print("2. feladat")
""" N edik hasznalo merre fele haladt de nekunk az van megadva hogy honnan erkezett"""

bekeres = int(input("Kerem adja meg hogy hanyadik jarmure kivancsi. "))

for k,v in forgalom.items():
    if k == bekeres:
        if v["Varosbol jon"] == "Felso":
            print("Ez a jarmu Also varos fele tart.")
        if v["Varosbol jon"] == "Also":
            print("Ez a jarmu Felso varos fele tart.")

print("3. feladat")
"""Ki kell irni a kepernyore hogy az utoso 2 F varos iranyaba tarto auto Hany masodperc kulonbseggel erte el a vizsgalt utszakasz kezdetet? """
F_varos_fele_tarto_kocsik = [v["Behajtas ideje"] for v in forgalom.values() if v["Varosbol jon"] == "Also"]
print("Az utoslso ket Felso varos iranyaba tarto kocsi kozott {} masodperc telt el.".format\
      (F_varos_fele_tarto_kocsik[-2].second - F_varos_fele_tarto_kocsik[-1].second))
print("4. feladat")
"""Orankent es iranyonkent meghatarozni hogy hany auto ment el a szakaszon. """
Felso_felol_jovok = 0
Also_felol_jovok = 0
elozo = int()
n = 0
for v in forgalom.values():    
    if v["Behajtas ideje"].hour == elozo and v["Varosbol jon"] == "Felso":
        Felso_felol_jovok+=1
    elif v["Behajtas ideje"].hour == elozo and v["Varosbol jon"] == "Also":
        Also_felol_jovok+=1
    else:
        print(elozo, Also_felol_jovok, Felso_felol_jovok) 
        elozo = v["Behajtas ideje"].hour
        Felso_felol_jovok = 0
        Also_felol_jovok = 0      
print(elozo, Also_felol_jovok, Felso_felol_jovok) 

print("5. feladat")
"""Belepes alapjan a 10 elgyorsabb jarmuvet meghatarozni.kiirni azok m/s sebesseget egy tizedes pontossagal sebbesseg szerint csokkeno sorrenben."""
""" belepes ideje,Also vagy felso, m/s 1 tizedes pontossagal"""
"""n=0
for v in forgalom.keys():
    for a in sorted(int(forgalom[v]["m/s"])):
        n+=1 
        if n <= 10:
            print(a)
"""
ms = [v["m/s"] for k,v in forgalom.items()]
mst = list()
asdsfds = list()
mst = sorted(ms)
asdsfds = mst.reverse()
szamlalo = 0
for a in forgalom.values():
    for ac in mst:
        if ac == a["m/s"]:
            szamlalo+=1
            if szamlalo <=10:
                print("Belepes ideje{0}:{1}:{2}, Varos: {3} Sebessege: {4:.1f}".format\
                      (a["Behajtas ideje"].hour, a["Behajtas ideje"].minute, a["Behajtas ideje"].second, a["Varosbol jon"], a["m/s"]))            
  

print("6. feladat")


with open("also.txt", "wt+", encoding="utf-8") as f:
    for a in forgalom.values():
        if a["Varosbol jon"] == "Felso":
            f.write("{0} {1} {2} {3}".format(a["Behajtas ideje"].hour, a["Behajtas ideje"].minute, a["Behajtas ideje"].second, "\n"))