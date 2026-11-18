import time
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C


class Startup:
    OLED_W = 128
    OLED_H = 64
    
    def __init__(
        self,
        scl_pin=15,
        sda_pin=14,
        i2c_freq=400000,
    ):
        self.i2c = I2C(1, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=i2c_freq)
        self.oled = SSD1306_I2C(self.OLED_W, self.OLED_H, self.i2c)
    
    def run(self):
        for dots in range(1, 4):
            self.oled.fill(0)
            self.oled.text("Loading" + "." * dots, 0, 0)
            self.oled.show()
            time.sleep(1)
