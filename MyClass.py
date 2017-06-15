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

bot = telepot.Bot('B')

def subject():
  import datetime
  day = datetime.date.today().strftime("%A")
  MondayS = {
      1:"Cryptography & Network Security",
      2:"Mobile Application Development Lab/Internet Programming Lab",
      3:"Mobile Application Development Lab/Internet Programming Lab",
      4:"Mobile Application Development Lab/Internet Programming Lab",
      5:"Comprehension",
      6:"Comprehension",
      7:"CDPD",
      8:"Mobile Application Development"
      }
  TuesdayS = {
      1:"Internet Programming",
      2:"Project Phase 1",
      3:"Project Phase 1",
      4:"Project Phase 1",
      5:"Mobile Application Development",
      6:"Cyber Forensics or XML and Web Services",
      7:"Mobile Computing",
      8:"TWM"
      }
  WednesdayS = {
      1:"Mobile Computing",
      2:"Cryptography & Network Security",
      3:"Software Testing",
      4:"Mobile Application Development",
      5:"Cryptography & Network Security",
      6:"Mobile Computing",
      7:"Software Testing",
      8:"Internet Programming"
      }
  ThursdayS = {
      1:"Software Testing",
      2:"Internet Programming",
      3:"Cyber Forensics or XML and Web Services",
      4:"Mobile Application Development",
      5:"Mobile Application Development Lab/Internet Programming Lab",
      6:"Mobile Application Development Lab/Internet Programming Lab",
      7:"Mobile Application Development Lab/Internet Programming Lab",
      8:"Seminar"
      }
  FridayS = {
      1:"Cyber Forensics or XML and Web Services",
      2:"Cryptography & Network Security",
      3:"Mobile Computing",
      4:"Seminar",
      5:"Internet Programming",
      6:"Software Testing",
      7:"Association",
      8:"Association"
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
        dayclas = subject()
        if time(8,45) <= in_time.time() <= time(9,34):
            rpy = dayclas[1]
        elif time(9,35) <= in_time.time() <= time(10,24):
            rpy = dayclas[2]
        elif time(10,25) <= in_time.time() <= time(10,44):
            rpy = "Break"
        elif time(10,45) <= in_time.time() <= time(11,34):
            rpy = dayclas[3]
        elif time(11,35) <= in_time.time() <= time(12,24):
            rpy = dayclas[4]
        elif time(12,25) <= in_time.time() <= time(13,24):
            rpy = "Lunch"
        elif time(13,25) <= in_time.time() <= time(14,14):
            rpy = dayclas[5]
        elif time(14,15) <= in_time.time() <= time(15,4):
            rpy = dayclas[6]
        elif time(15,5) <= in_time.time() <= time(15,14):
            rpy = "Break"
        elif time(15,15) <= in_time.time() <= time(16,4):
            rpy = dayclas[7]
        elif time(16,5) <= in_time.time() <= time(16,55):
            rpy = dayclas[8]
        else:
            rpy = "Coll mudinjuthu pa ... V2ku Poo!!!"
    else:
        rpy = "Coll illa pa, inaiku leave ... Poo!!!"
    return rpy


def staff():
    return "Yet To Add This Content :-) ..."

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
