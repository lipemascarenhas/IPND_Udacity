import webbrowser
import time

total_breaks = 3
break_count = 0

print ("This program started on"+time.ctime())
while break_count < total_breaks:
    time.sleep (25*60)
    webbrowser.open("https://www.youtube.com/watch?v=s4_xvNmgwsc&list=RDMMs4_xvNmgwsc")
    break_count += 1
