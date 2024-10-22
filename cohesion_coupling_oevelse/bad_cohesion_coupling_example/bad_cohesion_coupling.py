import machine
import neopixel
import time

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

kopier kodeeksemplet ind i en ny mappe kaldet "best_cohesion_and_coupling_example"

2. prøv derefter at skabe low coupling ved at lave et nyt modul til hver klasse (trykknap, neopixel-ring, potmeter)
    - Gem hver klasse med korrekt navngivning i et modul for sig
    - Sørg for at de nødvendige klasser importeres i hvert modul
    - Opret derefter en main fil og importer hver modul derinde og lav et objekt fra hver klasse
        (et til potmeter, og et til neopixel-ring og et til hver trykknap)
    - sørg for at main filen starter main() funktionen og test at koden fungerer
    - gem main filen i mappen "best_cohesion_and_coupling_example", og navngiv den "best_cohesion_and_coupling.py"
    - lav en lib mappe inde i denne mappe og indsæt de klasserne til neopixel-ringen, potmeteret og tryknapperne deri
    
"""

class AllInOne:
    def __init__(self, led_pin, num_pixels, pot_pin, button1_pin, button2_pin):
        self.np = neopixel.NeoPixel(machine.Pin(led_pin), num_pixels)
        self.num_pixels = num_pixels
        self.pot = machine.ADC(machine.Pin(pot_pin))
        self.pot.atten(machine.ADC.ATTN_11DB)
        self.pot.width(machine.ADC.WIDTH_10BIT)
        self.button1 = machine.Pin(button1_pin, machine.Pin.IN, machine.Pin.PULL_UP)
        self.button2 = machine.Pin(button2_pin, machine.Pin.IN, machine.Pin.PULL_UP)
        self.button1.irq(trigger=machine.Pin.IRQ_FALLING, handler=self.button1_handler)
        self.button2.irq(trigger=machine.Pin.IRQ_FALLING, handler=self.button2_handler)

    def update_leds(self):
        pot_value = self.pot.read()
        brightness = pot_value // 4
        for i in range(self.num_pixels):
            self.np[i] = (brightness, 0, 0)
        self.np.write()

    def button1_handler(self, pin):
        for i in range(self.num_pixels):
            self.np[i] = (0, 255, 0)
        self.np.write()
        time.sleep(1)

    def button2_handler(self, pin):
        for i in range(self.num_pixels):
            self.np[i] = (0, 0, 255)
        self.np.write()
        time.sleep(1)

def main():
    aio = AllInOne(26, 12, 34, 0, 4)
    while True:
        aio.update_leds()
        time.sleep(0.1)

if __name__ == "__main__":
    main()
