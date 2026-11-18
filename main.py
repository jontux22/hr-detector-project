from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from filefifo import Filefifo
import time
from slope_inspection import SlopeInspection
from sine_display import SineWaveDisplay
from freq_display import FrequencyDisplay
from button import Button


class HeartRateMonitor:
    def __init__(
        self,
        sw_0_pin=9,
        sw_1_pin=8,
        sw_2_pin=7,
        scl_pin=15,
        sda_pin=14,
        i2c_freq=400000,
        oled_w=128,
        oled_h=64,
    ):
        self.i2c = I2C(1, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=i2c_freq)
        self.oled = SSD1306_I2C(oled_w, oled_h, self.i2c)
        
        self.sw_0 = Button(sw_0_pin)
        self.sw_1 = Button(sw_1_pin)
        self.sw_2 = Button(sw_2_pin)
        
        self.slope_inspection = SlopeInspection()
        self.sine_display = SineWaveDisplay(1)
        self.freq_display = FrequencyDisplay(2)
    
    def run(self):
        self.print_menu()
        
        while True:
            self.select_page()
    
    def select_page(self):
        if self.sw_2.pressed():
            self.slope_inspection.run()
        
        if self.sw_1.pressed():
            self.sine_display.run()
        
        if self.sw_0.pressed():
            self.freq_display.run()
    
    def print_menu(self):
        self.oled.fill(0)
        self.oled.text("Task 1", 0, 0)
        self.oled.text("Task 2", 0, 8)
        self.oled.text("Task 3", 0, 16)
        self.oled.show()

if __name__ == "__main__":
    heartRateMonitor = HeartRateMonitor()
    heartRateMonitor.run()