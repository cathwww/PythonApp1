from random import * #randint
kommide_arv=randint(1,100)        #int(input("Kommide arv: "))
print(f"Laud on {kommide_arv} kommi.")
while True:
 try:
    kommid=int(input("Mitu kommi soovid ära võtta? "))
    kommide_arv -= kommid
    print(f"Laud on nüüd {kommide_arv} kommi. ")
    break 
 except ValueError:
    print("Palun sisesta number")
