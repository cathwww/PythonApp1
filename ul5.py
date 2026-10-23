import math
N =float(input("Sisesta ristkuliku esimene kulg (n): "))
M =float(input("Sisesta ristkuliku teine kulg (m): "))

diagonaal=round(math.sqrt(N**2 + M**2), 1)
print(f"Ristkuliku diagonaal on {diagonaal}.")