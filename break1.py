import time
import webbrowser

total_breaks = 3
break_count = 0

print time.ctime()
while (break_count <total_breaks):
    time.sleep(10)
    webbrowser.open ("https://www.google.com")
    break_count = break_count +1
    

