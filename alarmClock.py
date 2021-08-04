from datetime import datetime
from playsound import playsound
alarm_time = input("Set up the alarm:HH:MM:SS:AP\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting Alarm...")
while True:
    now = datetime.now()
    current_hour = now.strftime("%H")
    current_minute = now.strftime("%M")
    current_second = now.strftime("%S")
    current_period = now.strftime("%p")
    if alarm_time == current_period:
        if alarm_time == current_hour:
            if alarm_time == current_minute:
                if alarm_time == current_second:
                    print("Wake UP!!")
                    playsound('Extra Loud Ringtone Mp3 Free Download')
                    break

