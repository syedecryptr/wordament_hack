# For setup:
# adb -d forward tcp:1080 tcp:1080
# adb -d shell monkey --port 1080

import sys
import time
import telnetlib

tn = telnetlib.Telnet("localhost", 1080 , 5)
x1 = 180                   # X coordinate of column 1 (in pixels)
x2=544                   # X coordinate of column 2 (in pixels)
x3=895                   # X coordinate of column 3 (in pixels)

y1=707                   # Y coordinate of row 1 (in pixels)
y2=1068                   # Y coordinate of row 2 (in pixels)
y3=1425                   # Y coordinate of row 3 (in pixels)


s1 = "touch down " +str(x2) +" " +str(y1)+"\r\n"

s2 = "touch move " +str(x3) +" "+str(y3)+"\r\n"

s3 = "touch move " +str(x3)+" "+str(y1)+"\r\n"
s4 = "touch up " +str(x3) +" "+ str(y1)+"\r\n"

s5 = ""
s = s1+s2+s3+s4+s5

tn.write(s)

# Horizontal scroll right
while True:
    tn.write("touch down 180 707\r\ntouch move 544 707\r\ntouch down 544 707\r\ntouch move 895 707\r\ntouch down 895 707\r\ntouch move 
        895 1068\r\ntouch down 895 1068")
    time.sleep(0.2)
    tn.write("sleep 1000\r\n")

# Vertical scroll down
# while True:
#     tn.write("touch down 200 500\r\n")
#     tn.write("touch move 200 300\r\n")
#     tn.write("touch up 200 300\r\n")
#     tn.write("sleep 3000\r\n")
#     time.sleep(3)

tn.close        