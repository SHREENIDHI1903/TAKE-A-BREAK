import time
import webbrowser
total_break=3
break_count=0

print("Program Started at"+ time.ctime())
print("Its time to take break....")

while(break_count<total_break):
      time.sleep(15)
      webbrowser.open("https://www.youtube.com/watch?v=Bxjzi6Vn-_E")
      break_count=break_count +1


