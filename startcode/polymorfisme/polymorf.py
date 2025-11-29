from voertuig import Voertuig
from fiets import Fiets
from auto import Auto

# 1. Maak een lijst van voertuigen
lijst = [Voertuig("onbekend", 50) ,
         Fiets("trek", 10),
         Auto("tesla",150,300)
         ]
# 2. Overloop de lijst en roep voor elk voertuig de methode beweeg() op
for voertuig in lijst:
    print(voertuig.beweeg())