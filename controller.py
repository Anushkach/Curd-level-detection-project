#!/usr/bin/env python3
from pyfirmata import Arduino, util
from time import sleep
 
board = Arduino('COM4') # Change to your port
# print("Start blinking D13")
def blink_LED_RED():
    while True:
        board.digital[8].write(1)
        sleep(0.5)
        board.digital[8].write(0)
        sleep(0.5)

def on_LED_RED():
    board.digital[8].write(1)
    sleep(0.01)
    
def off_LED_RED():
    board.digital[8].write(0)

def on_LED_GREEN():
    board.digital[2].write(1)
    sleep(0.01)

def on_LED_YEL():
    board.digital[3].write(1)
    sleep(0.01)

def off_LED_YEL():
    board.digital[3].write(0)
    sleep(0.01)



def off_LED_GREEN():
    board.digital[2].write(0)

def blink_LED_GREEN():
    while True:
        board.digital[2].write(1)
        sleep(0.5)
        board.digital[2].write(0)
        sleep(0.5)


