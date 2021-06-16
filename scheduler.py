import datetime
import time
start_time = time.time()

# date
res = []
def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

for i in range(0,28,7):
    x = next_weekday(datetime.date.today(), 3+i)
    day = x.strftime("%d")
    month = x.strftime("%b")
    year = x.strftime("%Y")
    # print(day+'-'+month+'-'+year)
    res.append(day+'-'+month+'-'+year)

import calendar
from datetime import datetime

for i in range(4):
    if i == 3:
        month = calendar.monthcalendar(datetime.today().year, 12)
    else:
        month = calendar.monthcalendar(datetime.today().year, datetime.today().month+1+i)
    thrusday = max(month[-1][calendar.THURSDAY], month[-2][calendar.THURSDAY])
    day = str(thrusday)
    if i == 3:
        currentmonth = datetime.strptime(str(12), "%m").strftime("%b")
    else:
        currentmonth = datetime.strptime(str(datetime.today().month+1+i), "%m").strftime("%b")
    year = str(datetime.today().year)
    res.append(day+'-'+currentmonth+'-'+year)

print(res)

# API
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

# Authorize the API
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
]
file_name = 'client_key.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
client = gspread.authorize(creds)

# Fetch data from sheet
print("start")

for i in range(1,9):
    sheet1 = client.open('ISB shareable-'+str(i)).worksheet('ISB OPTION CHAIN - NIFTY')
    print("Opened sheet", i, "NIFTY")
    sheet1.update_cell(2, 2, res[i-1])
    print("Updated sheet", i, "NIFTY")
    sheet2 = client.open('ISB shareable-'+str(i)).worksheet('ISB OPTION CHAIN - BANK NIFTY')
    print("Opened sheet", i, "BANKNIFTY")
    sheet2.update_cell(2, 2, res[i-1])
    print("Updated sheet", i, "BANKNIFTY")

print("done")

print("--- %s seconds ---" % (time.time() - start_time))