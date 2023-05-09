from datetime import datetime
import time

requests_timings = []
##################################################
# OpenAI has a limit of 3 requests per 60 seconds,
# so we need to keep track of the request times
# and sleep when there are more than 3 requests in 60 sec
##################################################
def sleep_if_needed():
  global requests_timings

  if len(requests_timings) < 3:
    return

  now_ = datetime.now()
  wait_time = 61. - (now_ - requests_timings[-3]).total_seconds()
  if wait_time <= 0.:
    return

  time.sleep(wait_time)

##################################################
def add_now():
  global requests_timings
  requests_timings.append(datetime.now())
