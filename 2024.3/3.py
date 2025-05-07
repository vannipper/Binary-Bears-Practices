import math 

def tick(sec, min, hour):
    sec += 1
    print(str(hour) + str(min) + str(sec))
    if sec == 60:
        min += 1
    if min == 60:
        hour += 1
    if hour == 12:
        hour = 0

def magicTime(sec, min, hour):
    print([(hour*5 % 60), ((min - hour*5) % 60), ((hour*5 - min) % 60)])
    if sec in [(hour*5 % 60), (60 - (hour*5 - min)) % 60, (hour*5 - min) % 60]: 
        return True
    else:
        return False
    
reps = int(input())
for _ in range(reps):
    time = input()
    hour = int(time[0:2])
    min = int(time[3:5])
    sec = int(time[6:])
    if magicTime(sec, min, hour):
        print("Look Andy, it's a magical time!")
    else:
        for time in range(1, 61):
            sec += 1
            if sec == 60:
                sec = 0
                min += 1
            if min == 60:
                min = 60
                hour += 1
            if hour == 12:
                hour = 0
            if magicTime(sec, min, hour):
                if time == 1:
                    print("The next magical time is " + str(time) + " second away.")
                else:
                    print("The next magical time is " + str(time) + " seconds away.")
                break