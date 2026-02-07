import pywhatkit
from datetime import datetime, timedelta
now = datetime.now()
send_time = now + timedelta(minutes=3)
hour = send_time.hour
minute = send_time.minute
message = "hi this message is from PARAHELP"
pywhatkit.sendwhatmsg("+91 1234567890", message, hour, minute)
