# show watch
sec=45
mint=32
hours=2
import time
while True:
        print(str(hours) +":" +str(mint)+ ":"+str(sec))
        sec=sec+1
        time.sleep(1)
        if sec==60:
                sec=0
                mint=mint+1
        if mint==60:
                mint=0
                hours=hours+1
~                                             
