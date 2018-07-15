from apscheduler.schedulers.blocking import BlockingScheduler
from app import periodic_task

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=5)
def timed_job():
    print(periodic_task.getnews())

sched.start()