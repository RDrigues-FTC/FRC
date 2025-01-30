#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import wpilib.drive

class MyRobot(wpilib.TimedRobot):
    """
    This is a demo program showing the use of the DifferentialDrive class.
    Runs the motors with tank steering.
    """

    def robotInit(self):
        """Robot initialization function"""

        leftFrontMotor = wpilib.PWMSparkMax(3)
        leftBackMotor = wpilib.PWMSparkMax(4)
        rightFrontMotor = wpilib.PWMSparkMax(0)
        rightBackMotor = wpilib.PWMSparkMax(1)
        self.robotDrive = wpilib.drive.DifferentialDrive(leftFrontMotor, leftBackMotor, rightFrontMotor,rightBackMotor)
        self.leftStick = wpilib.Joystick(0)
        self.rightStick = wpilib.Joystick(1)

        # We need to invert one side of the drivetrain so that positive voltages
        # result in both sides moving forward. Depending on how your robot's
        # gearbox is constructed, you might have to invert the left side instead.
        rightFrontMotor.setInverted(True)
        rightBackMotor.setInverted(True)

    def teleopPeriodic(self):
        self.robotDrive.tankDrive(-self.leftStick.getY(), -self.rightStick.getY())