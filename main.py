#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

#Объявляем моторы
motor_top = Motor(Port.A)
motor_bottom = Motor(Port.B)

#Объявляем датчики
colorSensor = ColorSensor(Port.S1)
touch = TouchSensor(Port.S2)

#Цвет, который мы хотим пропустить
#color = Color.Blue
#color = Color.RED
needColor = Color.Green

extraStop = 1

motor_top.reset_angle(0)

while True:
    
    #Если нажать датчик касания, то все заработает
    wait(1000)
    if touch.pressed():
        extraStop = 1
        
        #Защита, чтобы много раз не сработал датчик
        while touch.pressed()==1:
                pass

    while extraStop = 1:
        ev3.light.on(Color.GREEN)
        
        #Если нажать датчик касания, то все остановится
        if touch.pressed():
            extraStop = 0
            ev3.light.on(Color.RED)

            #Защита, чтобы много раз не сработал датчик
            while touch.pressed()==1:
                pass

        motor_bottom = Motor(Port.B)
        

        #Выкидываем ненужные цвета
        if colorSensor.color() != needColor:
            motor_top.run_angle(90,200)

        #Возвращаем обратно 
        if colorSensor.color() == needColor:
            motor_top.run_angle(-90,200)
    

        
