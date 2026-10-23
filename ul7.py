from random import randint


arv1=randint(1,100)
arv2=randint(1,100)
arv3=randint(1,100)
arv4=randint(1,100)
arv5=randint(1,100)
summa=arv1+arv2+arv3+arv4+arv5
keskmine=summa/5
print(f"Summa: {summa}, Keskmine: {keskmine}")
try:
    jagaja=int(input("Sisesta arv, millega jagada: "))
    tulemus=summa/jagaja
    print("Tulemus", tulemus)
    print("Täisarvuline osa:", int(tulemus))
    print("Jääk:", summa % jagaja)
except ValueError:
    print("Palun sisesta kehtiv number.")