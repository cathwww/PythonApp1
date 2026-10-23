
print("Tere maailm!")
nimi=input("Sisesta oma nimi: ")
print(f"Tere maailm! Tervitan sind {nimi}!")
while True:
    try:
     vanus=int(input("Sisesta oma vanus: "))
     print(f"Tere maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")
     break
    except ValueError:
     print("Palun sisesta kehtiv number vanuse jaoks")