from apscheduler.schedulers.blocking import BlockingScheduler
from app import apis

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    apis.getnews()

sched.start()