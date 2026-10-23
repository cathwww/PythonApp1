pitsa_hind = 12.90
jootraha_protsent = 0.10
inimesed_arv = int(input("Mitu inimest pitsat jagab? "))
kogusumma = pitsa_hind * (1 + jootraha_protsent)
igaüks_maksab = kogusumma / inimesed_arv

print(float(f"Pitsa koguhind koos jootrahaga on {kogusumma} €"))
print(float(f"Igaüks peab maksma: {igaüks_maksab} €"))