import time
from pyev3.brick import LegoEV3
from pyev3.devices import Motor, Touch, Color


class Turbine():

    def __init__(self, motor, controller, color_sensor):
        self.motor = motor
        self.controller = controller
        self.color_sensor = color_sensor
        #Blockchain connection initialisieren

    def send_transaction(self):
        """Platzhalter für WEB3Code

        Während diese Methode läuft, zählt der Counter voraussichlich nicht weiter!
        TODO: Async?
        """
        
        print("SENDING 1ETH")
        pass

    def run(self):
        prev_angle = self.controller.angle
        previous_color = "default"

        angle = 0
        counter = 0
        motorspeed = 0

        motor.start()
        try:
            while True:
                # Motor controller
                if prev_angle != self.controller.angle:
                    angle = prev_angle - self.controller.angle
                    prev_angle = self.controller.angle
                    if -100 <= motorspeed <= 100:
                        motorspeed = (motorspeed + 2) if angle > 0 else (motorspeed - 2)
                    elif motorspeed <= 0:
                        motorspeed = -100
                    else:
                        motorspeed = 100
                self.motor.output = motorspeed
                
                color = self.color_sensor.output
                if previous_color != "red" and color == "red":
                    counter += 1
                    print(counter, end="\r")
                    if counter == 50:
                        self.send_transaction()
                        counter = 0
                previous_color = color
        except KeyboardInterrupt:
            self.motor.stop()
            myev3.close()
            print("stopped")


#SETUP
myev3 = LegoEV3(commtype='usb')
myev3.display_info()
motor = Motor(myev3, layer=1, port='D')
controller = Motor(myev3, layer=1, port='C')
color_sensor = Color(myev3, portnum=1, inputmode='color')

turbine = Turbine(motor, controller, color_sensor)

#RUN
turbine.run()