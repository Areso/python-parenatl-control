import ntplib
from time import ctime
import datetime
Network = 0
Delimeter = ':'
LocalTime = str(datetime.datetime.now())
#print(str(LocalTime))
DelPosLocalTime = LocalTime.find(Delimeter)
LocalTimeHours = int(LocalTime[DelPosLocalTime-2:DelPosLocalTime])
LocalTimeMinutes = int(LocalTime[DelPosLocalTime+1:DelPosLocalTime+3])
print(str(LocalTimeHours))
print(str(LocalTimeMinutes))
c = ntplib.NTPClient()
try:
    #Response = c.request('europe.pool.ntp.org', version=3)
    Response = c.request('pool.ntp.org')
    NetworkTime = datetime.datetime.utcfromtimestamp(response.tx_time)
    Network = 1
except:
    Network = 0

#print(newtime)
#print(ctime(response.tx_time))
#print(response.offset)

