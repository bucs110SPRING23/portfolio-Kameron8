from adviceslip import AdviceSlipAPI
from sunset import SunsetAPI
from temperature import TemperatureAPI
from controller import Controller
import requests

def main():
    controller = Controller()
    controller.mainloop()

main()