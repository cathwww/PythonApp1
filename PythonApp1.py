import math
print("Hello world!")
print("Tere tulemast!")
print("Õpin",1,".kursusel") #sep=" " vaikimisi on tühik
print("Õpin",1,".kursusel", sep="###") #sep="" tähendab, et tühikut ei ole


#Parametrid sep ja end
print() #see on tühi rida
print("2026", "10", "01", sep="-")
print("Sama ", end="") #end="" tähendab, et reavahetust ei ole end="\"
print("rida")


#Muutujad
nimi = "Python" #str ehk sõne
print ("Tere,", nimi)
kursus=1
print("Õpin",kursus,".kursusel")



# input() funktsioon
nimi = input ("Sisesta oma nimi: ") #programm küsib ja ootab kasutaja sisestust
print ("Tere,", nimi)
kursus=int(input("Sisesta kursuse number: ")) #teisendab sõne arvuks
print("Õpin",kursus,".kursusel")
print("Järgmisel aastan õpin ",kursus+1,".kursusel") #kursus+1 tähendab, et kursuse number suureneb 1 võrra



print("Liitmine")
a = int(input("Esimene arv: "))
b = int(input("Teine arv: "))
print(a,"+",b,"=",a + b)


print("Lahutamine")
a = int(input("Esimene arv: "))
b = int(input("Teine arv: "))
print(a,"-",b,"=",a - b)


print("Astendamine")
a = int(input("Esimene arv: "))
b = int(input("Teine arv: "))
print(a,"**",b,"=",a ** b)


print("Korrutamine")
a = int(input("Esimene arv: "))
b = int(input("Teine arv: "))
print(a,"*",b,"=",a * b)


print("jagamine")
a = int(input("Esimene arv: "))
b = int(input("Teine arv: "))
print(a,"/",b,"=",a / b)
print("Ümardatud arv: ",round (a / b,2))


print("jagamise täisarvuline osa")
a = int(input("Esimene arv: "))
b = int(input("Teine arv: "))
print(a,"//",b,"=",a // b)


print("jagamisjääk")
a = int(input("Esimene arv: "))
b = int(input("Teine arv: "))
print(a,"%",b,"=",a % b)


#f-sõne formatimine
nimi ="Mari"
punktid = 87
print(f"{nimi} sai {punktid} punkti.")

a = int(input("Esimene arv: "))
tehe=input("Tehe: ")
b = int(input("Teine arv: "))

print(f"{a} {tehe} {b} 0 {eval(f'{a} {tehe} {b}')}")


#math moodul
print("Pii väärtus:", math.pi)
print("√16 =", math.sqrt(16))
print("sin(π/2) =", math.sin(math.pi / 2))
print("sin(30°) =", round(math.sin(math.radians(30)), 2))
print("5! =", math.factorial(5))