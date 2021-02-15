from datetime import datetime
from datetime import date
now = datetime.now()
today = date.today()

nowTime = now.strftime("%H:%M:%S")
nowDate = today.strftime("%d/%m/%Y")

print("Last Updated at:", nowTime, "on",nowDate)
