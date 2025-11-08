
#Speed = Distance / Time. Write a function such if any of two of the 
# Variables are given, the function should be able to give 
# the third variable (Physics - Mechanics) 
#Eg: If Speed and Time is given, Distance can be determined.

speed = int(input('speed ='))
distance = int(input('distance ='))
time = int(input('time ='))

if speed > 0 and distance > 0: 
    print('time:',speed/distance)

elif speed > 0 and time <= 60: 
    print('distance =', speed*time)

elif distance > 0 and time <= 60:
    print('speed =',distance/time)

else : 
    print('variables not given' )

    

