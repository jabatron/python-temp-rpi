import schedule
import time

def thing_you_wanna_do():
   print (time.asctime())
   return

schedule.every().minute.do(thing_you_wanna_do)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
