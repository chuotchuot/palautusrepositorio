#tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"Lukujen {x} ja {y} summa on {summa(x, y)}")
print(f"Lukujen {x} ja {y} erotus on {erotus(x, y)}")

logger("lopetetaan")
print("goodbye!")
