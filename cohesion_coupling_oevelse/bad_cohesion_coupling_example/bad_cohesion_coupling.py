import machine
import neopixel
import time

"""
Example of code with high coupling and low cohesion

The code reads a potentiometer value to control brightness of a neopixel ring

The program includes 2 pushbuttons that can be pushed to change color on neopixel ring

Everything is combined in one class an one module that handles all the functionality 
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
