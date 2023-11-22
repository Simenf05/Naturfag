import random as r
import matplotlib.pyplot as plt

antall_terninger_list = []
antall_kast_list = []
antall_kast = 0

def kast(terninger, antall_kast):
    antall_kast_list.append(antall_kast)
    antall_terninger_list.append(terninger)
    terningliste = []
    for _ in range(terninger):
        terning = r.randint(1, 6)
        terningliste.append(terning)
    return terningliste



terninger = 1000
halvering = terninger / 2

while terninger > 0:
    terningliste = kast(terninger, antall_kast)
    antall_kast += 1
    terninger = terninger - terningliste.count(6)



print(antall_kast_list)
print(antall_terninger_list)
plt.plot(antall_kast_list, antall_terninger_list)
plt.axhline(halvering, color="red")
plt.ylabel("Antall terninger")
plt.xlabel("Antall kast")
plt.grid()
plt.show()