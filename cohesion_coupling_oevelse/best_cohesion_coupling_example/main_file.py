import time

from neopixel_ring import NeoPixelRing
from button import Button
from potentiometer import Potentiometer
"""
Problemer med dette design:

Lav cohesion:

Klassen AllInOne har for mange ansvarsområder
(LED-kontrol, potentiometer-læsning, og knaphåndtering),
hvilket gør den svær at forstå og vedligeholde.

Høj coupling:

Alle komponenter er tæt forbundet inden for samme klasse,
hvilket gør det svært at ændre eller teste individuelle dele af systemet.

Øvelse:

koden skal omstruktureres (re-formateres).
Det meste af koden fra eksemplet kan genbruges for at løse øvelsen, men det skal flyttes rundt.

1. prøv at skabe høj cohesion ved at oprette en ny klasse til hvert ansvarsområde
    - Navngiv hver klasse fornuftigt efter PEP8
    - Hver klasse skal have sin egen constructor (__init__) og instantiere de objekter der
        kræves for at den kan fungere.
    - Lav nu et objekt for hver af klasserne, til potmeter, neopixel-ring og et til hver trykknap.
    - Behold hver klassse i samme fil og test at koden virker
    - Gem dette program i en mappe kalde "better_cohesion" og navngiv filen "better_cohesion_example.py"
"""

def main():
    np_ring = NeoPixelRing(26, 12)
    pot = Potentiometer(34)

    def button1_handler(pin):
        np_ring.set_color((0, 255, 0))
        time.sleep(1)

    def button2_handler(pin):
        np_ring.set_color((0, 0, 255))
        time.sleep(1)

    button1 = Button(0, button1_handler)
    button2 = Button(4, button2_handler)

    while True:
        pot_value = pot.read_value()
        brightness = pot_value // 4
        np_ring.set_color((brightness, 0, 0))
        time.sleep(0.1)

if __name__ == "__main__":
    main()
