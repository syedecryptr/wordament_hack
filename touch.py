# For setup:
# adb -d forward tcp:1080 tcp:1080
# adb -d shell monkey --port 1080

import sys
import time
import telnetlib
import main

tn = telnetlib.Telnet("localhost", 1080 , 5)

x=[140, 396, 680, 940]
y=[402, 680, 946, 1197]

# list_of_words = [[(x[0], y[0]), (x[0], y[1]), (x[0], y[2]), (x[0], y[3]), (x[3], y[3]) ]]
list_of_words, list_of_strings = main.syed_afshan()

# for word in list_of_words:
for i in range(0,len(list_of_words)):
    word = list_of_words[i];
    string = list_of_strings[i]
    print string, word
    s = ""
    s += "touch down " +str(word[0][0]) +" " +str(word[0][1])+"\r\n"
    for coordinates in word:

        s += "touch move " +str(coordinates[0]) +" "+str(coordinates[1])+"\r\n"

    s += "touch up " +str(word[-1][0]) +" "+ str(word[-1][1])+"\r\n"

    tn.write(s)
    time.sleep(0.1)
