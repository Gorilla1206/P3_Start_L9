"""
Leerling - Subklasse van Karakter.
Demonstreert overerving en method overriding.
"""
from io import klass

from models.karakter import Karakter
from config import COLORS
import random


class Leerling(Karakter):
    """
    Leerling klasse - erft van Karakter.
    Dit is nog een SUBKLASSE: net als Leerkracht, maar met eigen uniek gedrag.
    """
    
    def __init__(self, naam: str, leeftijd: int, klas: str, x_tile: int, y_tile: int, dialoog: str):
        """
        Initialiseer een leerling.
        Ook hier gebruiken we super().__init__() voor code hergebruik.
        """
        # TODO Oefening 2a: Roep super().__init__() aan met COLORS["groen"] en sla klas op
        pass
        super().__init__(naam, leeftijd , x_tile, y_tile,COLORS["groen"],dialoog)
        self.klass =klass
        self.spel = spel

    def beschrijf(self) -> str:
        """
        Overschreven beschrijving voor leerling.
        METHOD OVERRIDING: elke subklasse kan zijn eigen versie hebben.
        """
        # TODO Oefening 2b: Roep super().beschrijf() aan en voeg klasinformatie toe

        basis = super().beschrijf()
        return f"{basis} - leerling {self.klass }"

    def verwerk_bericht(self, bericht: str, speler_inventory: list) -> str:
        """
        Verwerk bericht - speelt schaar-steen-papier als deze leerling een spel heeft.
        """
        # TODO Oefening 3: Implementeer schaar-steen-papier als self.spel == "schaar-steen-papier"
        if self.spel == "schaar-steen-papier":
            opties =  ["schaar", "steen", "papier"]

            keuze = bericht.lower().strip()

            npc_keuze = random.choice(opties)
            if keuze not in opties:
                 return f"{self.naam}: type schaar , steen of papier"
            # Bepaal winnaar
            if keuze == npc_keuze:
                return f"{self.naam} koos {npc_keuze}. Gelijkspel! Probeer opnieuw."
            elif (keuze == "schaar" and npc_keuze == "papier") or \
                    (keuze == "steen" and npc_keuze == "schaar") or \
                    (keuze == "papier" and npc_keuze == "steen"):
                # Speler wint! Voeg items direct toe aan speler inventory
                if "deo" not in speler_inventory:
                    speler_inventory.append("deo")
                if "doek" not in speler_inventory:
                    speler_inventory.append("doek")
                return f"{self.naam} koos {npc_keuze}. Jij wint! Je kreeg deo en een doek!"
            else:
                return f"{self.naam} koos {npc_keuze}. Je verliest! Probeer opnieuw."
