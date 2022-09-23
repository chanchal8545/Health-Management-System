#Healthy Programmer
# 9am - 5pm
# Water (3.5 litres) - Drank - Every 40 min
# Eyes - every 30 min 
# Physical activity - every - 45 min 

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("alarm.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5 #40*60
    exsecs = 20  #30*60
    eyessecs =  40 #45*60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'stop' to stop the alarm.")
            musiconloop('alarm.mp3', 'stop')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes >eyessecs:
            print("Eye exercise time. Enter 'stop' to stop the alarm.")
            musiconloop('alarm.mp3', 'stop')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'stop' to stop the alarm.")
            musiconloop('alarm.mp3', 'stop')
            init_exercise = time()
            log_now("Physical Activity done at")