#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import StopWatch, DataLog, wait

import random

# Initialize the EV3 brick.
ev3 = EV3Brick()
# Initialize a motor at port B.
motor = Motor(Port.D)
color_sensor = ColorSensor(Port.S1)

def Run(brick, motor, color_sensor, num_runs=3, runtime=10):
    stopwatch = StopWatch()
    log = DataLog("run", "counter", "motorspeed", "expected_count", timestamp=False, extension='csv', append=True)
    for i in range(num_runs):
        print("RUN {} of {}".format(i+1, num_runs))
        ev3.speaker.beep()
        counter = 0
        motor_speed = random.randrange(100, 500)
        expected_count = (motor_speed * runtime)/360 * 3
        print("Motor speed: {}".format(motor_speed))
        print("Expected count: {}".format(expected_count))
        motor.run(motor_speed)
        stopwatch.resume()
        previous_color = "default"
        while stopwatch.time() <= runtime*1000:
        
            color = str(color_sensor.color())
            
            if (previous_color != "Color.RED" or previous_color is None) and color == "Color.RED":
                counter += 1
            
            previous_color = color
        motor.stop()
        print("Realized count: {}".format(counter))
        stopwatch.pause()
        stopwatch.reset()
        log.log(i, counter, motor_speed, expected_count)
        print("log written")
    return None

Run(ev3, motor, color_sensor)