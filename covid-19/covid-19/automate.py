from classes import data
from apscheduler.schedulers.blocking import BlockingScheduler
from win10toast import ToastNotifier

toaster = ToastNotifier()

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', seconds=10)
def summarise():
    summ = data.Summary()
    toaster.show_toast("COVID-19 STATS", str(summ), icon_path="C:\\Users\\Nate\\Code\\covid-19\\covid-19\\COVID_19.ico", duration=5)
    
scheduler.start()
    

