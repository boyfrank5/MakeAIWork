'''
====== Legal notices

Copyright (C) 2013 - 2021 GEATEC engineering

This program is free software.
You can use, redistribute and/or modify it, but only under the terms stated in the QQuickLicense.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY, without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the QQuickLicense for details.

The QQuickLicense can be accessed at: http://www.qquick.org/license.html

__________________________________________________________________________


 THIS PROGRAM IS FUNDAMENTALLY UNSUITABLE FOR CONTROLLING REAL SYSTEMS !!

__________________________________________________________________________

It is meant for training purposes only.

Removing this header ends your license.
'''
#!/usr/bin/env python

import time as tm
import traceback as tb
import math as mt
import sys as ss
import os
import socket as sc
import numpy as np
import tensorflow as tf

sonar_model_path = '/Users/boyfrankclaesen/MakeAIWork/simulations/car/control_client/s_ts_model'
lidar_model_path = '/Users/boyfrankclaesen/MakeAIWork/simulations/car/control_client/l_ts_model'

ss.path +=  [os.path.abspath (relPath) for relPath in  ('..',)] 

import socket_wrapper as sw
import parameters as pm

class DrivingAgent:
    def __init__ (self): # hier wordt het object gemaakt. Alle def functies die onder de class hangen gaan meee. 
        self.model = None
        self.steeringAngle = 0

        with open (pm.sampleFileName, 'w') as self.sampleFile:
            with sc.socket (*sw.socketType) as self.clientSocket:
                self.clientSocket.connect (sw.address)
                self.socketWrapper = sw.SocketWrapper (self.clientSocket)
                self.halfApertureAngle = False

                while True:
                    self.input () # komt vanuit de simulatie
                    self.sweep () # hier wordt het NN toegepast
                    self.output () # hier wordt de output gestuurd naar de output -> stuurhoek en snelheid.
                    #self.logTraining ()
                    tm.sleep (0.02)

    def input (self): #de input komt niet vanzelf binnen, deze wordt dmv deze def opgeroepen.
        sensors = self.socketWrapper.recv ()

        if not self.halfApertureAngle:
            self.halfApertureAngle = sensors ['halfApertureAngle']
            self.sectorAngle = 2 * self.halfApertureAngle / pm.lidarInputDim
            self.halfMiddleApertureAngle = sensors ['halfMiddleApertureAngle']
            
        if 'lidarDistances' in sensors:
            self.lidarDistances = sensors ['lidarDistances']
            if self.model == None:
                self.model = tf.keras.models.load_model(lidar_model_path) # probeer hier later nog eens naar te kijken. OOP gerelateerd.
        else:
            self.sonarDistances = sensors ['sonarDistances']
            if self.model == None:
                self.model = tf.keras.models.load_model(sonar_model_path) #naam aanpassen

#lidar             
    def lidarSweep (self):
        nearestObstacleDistance = pm.finity
        nearestObstacleAngle = 0
        
        nextObstacleDistance = pm.finity
        nextObstacleAngle = 0

        for lidarAngle in range (-self.halfApertureAngle, self.halfApertureAngle):
            lidarDistance = self.lidarDistances [lidarAngle]
            
            if lidarDistance < nearestObstacleDistance:
                nextObstacleDistance =  nearestObstacleDistance
                nextObstacleAngle = nearestObstacleAngle
                
                nearestObstacleDistance = lidarDistance 
                nearestObstacleAngle = lidarAngle

            elif lidarDistance < nextObstacleDistance:
                nextObstacleDistance = lidarDistance
                nextObstacleAngle = lidarAngle
           
        targetObstacleDistance = (nearestObstacleDistance + nextObstacleDistance) / 2

        self.steeringAngle = (nearestObstacleAngle + nextObstacleAngle) / 2
        self.targetVelocity = pm.getTargetVelocity (self.steeringAngle)

#sonar
    def sonarSweep (self):
        new_model = self.model.predict(np.array([self.sonarDistances])) # drie waarde voor sonar, worden gehaald uit SR
        self.steeringAngle = float(new_model[0][0]) 
        self.targetVelocity = pm.getTargetVelocity (self.steeringAngle)


    def sweep (self):
        if hasattr (self, 'lidarDistances'): # wordt gecreerd in de input. #73
            self.lidarSweep ()
        else:
            self.sonarSweep ()

    def output (self):
        actuators = {
            'steeringAngle': self.steeringAngle,
            'targetVelocity': self.targetVelocity
        }

        self.socketWrapper.send (actuators)

DrivingAgent()

