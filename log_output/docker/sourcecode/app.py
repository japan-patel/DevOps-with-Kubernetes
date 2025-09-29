import random
import string
import datetime
import time



def random_string_generator():
    length = 12
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k = length))
    date = datetime.datetime.now()
    print(date.strftime('%d/%m/%y %H:%M:%S.%f'),":",random_string, flush = True)
    
while True:
    random_string_generator()
    time.sleep(5)
  
