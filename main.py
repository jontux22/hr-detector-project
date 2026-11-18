from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
from startup import Startup
from button import Button


class HeartRateMonitor:
    OLED_W = 128
    OLED_H = 64
    
    def __init__(
        self,
        scl_pin=15,
        sda_pin=14,
        i2c_freq=400000
    ):
        self.i2c = I2C(1, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=i2c_freq)
        self.oled = SSD1306_I2C(self.OLED_W, self.OLED_H, self.i2c)
        
        self.startup = Startup()
    
    def run(self):
        self.startup.run()
        self.print_menu()
    
    def print_menu(self):
        self.oled.fill(0)
        self.oled.text("Task 1", 0, 0)
        self.oled.text("Task 2", 0, 8)
        self.oled.text("Task 3", 0, 16)
        self.oled.show()

if __name__ == "__main__":
    heartRateMonitor = HeartRateMonitor()
    heartRateMonitor.run()