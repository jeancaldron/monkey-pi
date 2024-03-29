#! /usr/bin/env python

from dobot import Dobot
from camara import ColorTracker
import time

speed = 400
acceleration = 300

# dobot = Dobot('/dev/ttyACM0',debug=False)
dobot = Dobot('COM7',debug=False)
tracker = ColorTracker(debug=False)

dobot.Gripper(208) # abrir
dobot.Wait(0.10)

busquedas = ["amarillo","rojo"]



for color in busquedas:
    UbicacionColor = tracker.FindColor(color)

    print("*** El objeto esta en: {0}".format(UbicacionColor))

    ejeX = UbicacionColor[0]

    if (400 <= ejeX <= 450):
        print("*** {0} esta a la izquierda".format(color))
        dobot.MoveWithSpeed(230, -45, 110, acceleration) #izquierda arriba
        dobot.MoveWithSpeed(230, -40, 70, acceleration) #izquierda
    elif (300 <= ejeX <= 350):
        print("*** {0} esta en el centro".format(color))
        dobot.MoveWithSpeed(230, 0, 110, acceleration) #centro arriba
        dobot.MoveWithSpeed(230, 0, 70, acceleration) #centro
    elif (150 <= ejeX <= 250):
        print("*** {0} esta a la derecha".format(color))
        dobot.MoveWithSpeed(230, 45, 110, acceleration) #derecha arriba
        dobot.MoveWithSpeed(230, 40, 70, acceleration) #derecha

    dobot.Gripper(480) # cerrar
    dobot.Wait(0.10)

    dobot.MoveWithSpeed(210.9, 0, 238, acceleration) # voler al medio

    dobot.MoveWithSpeed(0, -150, 238, acceleration) #dar en la mano

    dobot.Gripper(208) # abrir
    dobot.Wait(0.10)

    dobot.MoveWithSpeed(210.9, 0, 238, acceleration) # voler al medio





# # dobot.MoveWithSpeed(210.9, 0, 238, acceleration) # volver al medio

# dobot.Gripper(208) # abrir
# dobot.Wait(0.10)

# dobot.MoveWithSpeed(230, 45, 110, acceleration) #derecha arriba
# dobot.MoveWithSpeed(230, 40, 70, acceleration) #derecha

# dobot.Gripper(480) # cerrar
# dobot.Wait(0.10)

# dobot.MoveWithSpeed(210.9, 0, 238, acceleration) # voler al medio

# dobot.MoveWithSpeed(0, -150, 238, acceleration) #dar en la mano

# dobot.Gripper(208) # abrir
# dobot.Wait(0.10)

# dobot.MoveWithSpeed(210.9, 0, 238, acceleration) # voler al medio

# dobot.MoveWithSpeed(230, -45, 110, acceleration) #izquierda arriba
# dobot.MoveWithSpeed(230, -40, 70, acceleration) #izquierda

# dobot.Gripper(480) # cerrar
# dobot.Wait(0.10)

# dobot.MoveWithSpeed(210.9, 0, 238, acceleration) # voler al medio

# dobot.MoveWithSpeed(0, -150, 238, acceleration) #dar en la mano

# dobot.Gripper(208) # abrir
# dobot.Wait(0.10)

# dobot.MoveWithSpeed(210.9, 0, 238, acceleration) # voler al medio

# dobot.MoveWithSpeed(230, 0, 110, acceleration) #izquierda arriba
# dobot.MoveWithSpeed(230, 0, 70, acceleration) #izquierda

# dobot.Gripper(480) # cerrar
# dobot.Wait(0.10)

# dobot.MoveWithSpeed(210.9, 0, 238, acceleration) # voler al medio

# dobot.MoveWithSpeed(0, -150, 238, acceleration) #dar en la mano

# dobot.Gripper(208) # abrir
# dobot.Wait(0.10)