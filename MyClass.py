import telepot
import urllib3
import datetime
from datetime import time
from datetime import datetime
from pytz import timezone
import time

# You can leave this bit out if you're using a paid PythonAnywhere account
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
# end of the stuff that's only needed for free accounts

bot = telepot.Bot('Add Bot API Token Here')

def details():
  import datetime
  day = datetime.date.today().strftime("%A")
  MondayS = {
      1:["Cryptography & Network Security","Sruthi"],
      2:["Mobile Application Development Lab/Internet Programming Lab","HariHaraGopal/ Kanagaraj"],
      3:["Mobile Application Development Lab/Internet Programming Lab","HariHaraGopal/ Kanagaraj"],
      4:["Mobile Application Development Lab/Internet Programming Lab","HariHaraGopal/ Kanagaraj"],
      5:["Comprehension","Kanagaraj"],
      6:["Comprehension","Kanagaraj"],
      7:["CDPD","HariHaraGopal"],
      8:["CDPD","HariHaraGopal"]
      }
  TuesdayS = {
      1:["Internet Programming","Kanagaraj"],
      2:["Project Phase 1","Padmavathy"],
      3:["Project Phase 1","Padmavathy"],
      4:["Project Phase 1","Padmavathy"],
      5:["Mobile Application Development","Vinotha"],
      6:["Cyber Forensics or XML and Web Services","Mathivanan/Padmavathy"],
      7:["Mobile Computing","HariHaraGopal"],
      8:["TWM","Hari/Kanagaraj/Aruna"]
      }
  WednesdayS = {
      1:["Mobile Computing","HariHaraGopal"],
      2:["Cryptography & Network Security","Sruthi"],
      3:["Software Testing","Mathivanan"],
      4:["Cryptography & Network Security","Sruthi"],
      5:["Mobile Application Development","Vinotha"],
      6:["Mobile Computing","HariHaraGopal"],
      7:["Software Testing","Mathivanan"],
      8:["Internet Programming","Kanagaraj"]
      }
  ThursdayS = {
      1:["Software Testing","Mathivanan"],
      2:["Internet Programming","Kanagaraj"],
      3:["Cyber Forensics or XML and Web Services","Mathivanan/Padmavathy"],
      4:["Mobile Application Development","Vinotha"],
      5:["Mobile Application Development Lab/Internet Programming Lab","HariHaraGopal/ Kanagaraj"],
      6:["Mobile Application Development Lab/Internet Programming Lab","HariHaraGopal/ Kanagaraj"],
      7:["Mobile Application Development Lab/Internet Programming Lab","HariHaraGopal/ Kanagaraj"],
      8:["Mobile Application Development","Vinotha"]
      }
  FridayS = {
      1:["Cyber Forensics or XML and Web Services","Mathivanan/Padmavathy"],
      2:["Cryptography & Network Security","Sruthi"],
      3:["Mobile Computing","HariHaraGopal"],
      4:["Seminar","Kanagaraj"],
      5:["Internet Programming","Kanagaraj"],
      6:["Software Testing","Mathivan"],
      7:["Association","HariHaraGopal"],
      8:["Association","HariHaraGopal"]
      }
  if day == 'Monday':
      daysub = MondayS.copy()
  elif day == 'Tuesday':
      daysub = TuesdayS.copy()
  elif day == 'Wednesday':
      daysub = WednesdayS.copy()
  elif day == 'Thursday':
      daysub = ThursdayS.copy()
  elif day == 'Friday':
      daysub = FridayS.copy()
  return daysub

def wclass():
    import datetime
    day = datetime.date.today()
    day = day.strftime("%A")
    from datetime import datetime
    from pytz import timezone
    india = timezone('Asia/Calcutta')
    in_time = datetime.now(india)
    from datetime import time
    if (day != 'Saturday' or day != 'Sunday'):
        dayclas = details()
        if time(8,45) <= in_time.time() <= time(9,34):
            rpy = dayclas[1][0]
        elif time(9,35) <= in_time.time() <= time(10,24):
            rpy = dayclas[2][0]
        elif time(10,25) <= in_time.time() <= time(10,44):
            rpy = "Break"
        elif time(10,45) <= in_time.time() <= time(11,34):
            rpy = dayclas[3][0]
        elif time(11,35) <= in_time.time() <= time(12,24):
            rpy = dayclas[4][0]
        elif time(12,25) <= in_time.time() <= time(13,24):
            rpy = "Lunch"
        elif time(13,25) <= in_time.time() <= time(14,14):
            rpy = dayclas[5][0]
        elif time(14,15) <= in_time.time() <= time(15,4):
            rpy = dayclas[6][0]
        elif time(15,5) <= in_time.time() <= time(15,14):
            rpy = "Break"
        elif time(15,15) <= in_time.time() <= time(16,4):
            rpy = dayclas[7][0]
        elif time(16,5) <= in_time.time() <= time(16,55):
            rpy = dayclas[8][0]
        else:
            rpy = "Coll mudinjuthu pa ... V2ku Poo!!!"
    else:
        rpy = "Coll illa pa, inaiku leave ... Poo!!!"
    return rpy


def staff():
    import datetime
    day = datetime.date.today()
    day = day.strftime("%A")
    from datetime import datetime
    from pytz import timezone
    india = timezone('Asia/Calcutta')
    in_time = datetime.now(india)
    from datetime import time
    if (day != 'Saturday' or day != 'Sunday'):
        dayclas = details()
        if time(8,45) <= in_time.time() <= time(9,34):
            rpy = dayclas[1][1]
        elif time(9,35) <= in_time.time() <= time(10,24):
            rpy = dayclas[2][1]
        elif time(10,25) <= in_time.time() <= time(10,44):
            rpy = "Break"
        elif time(10,45) <= in_time.time() <= time(11,34):
            rpy = dayclas[3][1]
        elif time(11,35) <= in_time.time() <= time(12,24):
            rpy = dayclas[4][1]
        elif time(12,25) <= in_time.time() <= time(13,24):
            rpy = "Lunch"
        elif time(13,25) <= in_time.time() <= time(14,14):
            rpy = dayclas[5][1]
        elif time(14,15) <= in_time.time() <= time(15,4):
            rpy = dayclas[6][1]
        elif time(15,5) <= in_time.time() <= time(15,14):
            rpy = "Break"
        elif time(15,15) <= in_time.time() <= time(16,4):
            rpy = dayclas[7][1]
        elif time(16,5) <= in_time.time() <= time(16,55):
            rpy = dayclas[8][1]
        else:
            rpy = "Coll mudinjuthu pa ... V2ku Poo!!!"
    else:
        rpy = "Coll illa pa, inaiku leave ... Poo!!!"
    return rpy

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text':
        if msg["text"] == '/subject' or msg["text"] == '/subject@MyClassSquare_Bot':
            ans = wclass()
            bot.sendMessage(chat_id, "Current Period : '{}'".format(ans))
        elif msg["text"] == '/staff' or msg["text"] == '/staff@MyClassSquare_Bot':
            ans = staff()
            bot.sendMessage(chat_id, "This hour Staff is : '{}'".format(ans))
        elif msg["text"] == '/start' or msg["text"] == '/start@MyClassSquare_Bot':
            bot.sendMessage(chat_id, "Hi, Hope Day is going Great !!!... Send /subject or /staff to get the current period")
        else:
            bot.sendMessage(chat_id, "Ohh Hoooo ... Invalid Option")

bot.message_loop(handle)

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)

